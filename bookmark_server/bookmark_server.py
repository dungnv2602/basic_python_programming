#!/usr/bin/env python3
#
# A *bookmark server* or URI shortener.

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import requests
import os
from urllib.parse import unquote, parse_qs
from http import cookies
from html import escape as html_escape


memory = {}

form = '''<!DOCTYPE html>
<title>Bookmark Server</title>
<dev>
    <form method="POST">
        <label>Long URI:
            <input name="longuri">
        </label>
        <br>
        <label>Short name:
            <input name="shortname">
        </label>
        <br>
        <button type="submit">Save it!</button>
    </form>
</dev>
<dev>
    <form method="POST">
    <label>What's your name again?
    <input type="text" name="yourname">
    </label>
    <br>
    <button type="submit">Tell me!</button>
    </form>
</dev>
<p>URIs I know about:
<pre>
{}
</pre>
'''


def CheckURI(uri, timeout=5):
    '''Check whether this URI is reachable, i.e. does it return a 200 OK?

    This function returns True if a GET request to uri returns a 200 OK, and
    False if that GET request returns any other response, or doesn't return
    (i.e. times out).
    '''
    try:
        r = requests.get(uri, timeout=timeout)
        # If the GET request returns, was it a 200 OK?
        return r.status_code == 200
    except requests.RequestException:
        # If the GET request raised an exception, it's not OK.
        return False


class Shortener(BaseHTTPRequestHandler):
    def do_GET(self):
        # A GET request will either be for / (the root path) or for /some-name.
        # Strip off the / and we have either empty string or a name.
        name = unquote(self.path[1:])

        if name:
            if name in memory:
                # We know that name! Send a redirect to it.
                self.send_response(303)
                self.send_header('Location', memory[name])
                self.end_headers()
            else:
                # We don't know that name! Send a 404 error.
                self.send_response(404)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write("I don't know '{}'.".format(name).encode())
        else:
            # Root path. Send the form.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # List the known associations in the form.
            known = "\n".join("{} : {}".format(key, memory[key])
                              for key in sorted(memory.keys()))
            self.wfile.write(form.format(known).encode())

    def do_POST(self):
        # Decode the form data.
        length = int(self.headers.get('Content-length', 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)
        longuri = params["longuri"][0]
        shortname = params["shortname"][0]

        if CheckURI(longuri):
            # This URI is good!  Remember it under the specified name.
            memory[shortname] = longuri

            # Serve a redirect to the form.
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            # Didn't successfully fetch the long URI.
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(
                "Couldn't fetch URI '{}'. Sorry!".format(longuri).encode())


class NameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the post data?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the post data
        data = self.rfile.read(length).decode()
        yourname = parse_qs(data)["yourname"][0]

        # Create cookie
        c = cookies.SimpleCookie()
        c['yourname'] = yourname
        c['yourname']['domain'] = 'localhost'
        c['yourname']['max-age'] = 60

        # Send a 303 back to the root page, with a cookie!
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.send_header('Set-Cookie', c['yourname'].OutputString())
        self.end_headers()

    def do_GET(self):
        # Default message if we don't know a name.
        message = "I don't know you yet!"

        if 'cookie' in self.headers:
            try:
                # Extract and decode the cookie.
                c = cookies.SimpleCookie(self.headers['cookie'])
                name = c['yourname'].value

                # Craft a message, escaping any HTML special chars in name.
                message = "Hey there, {}".format(html_escape(name))
            except (KeyError, cookies.CookieError) as e:
                message = "I'm not sure who you are!"
                print(e)

        # 1st, send 200 OK response
        self.send_response(200)

        # Then send headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        message = form.format(message)

        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('', int(os.environ.get('PORT', '8000')))
    httpd = ThreadingHTTPServer(server_address, NameHandler)
    httpd.serve_forever()
