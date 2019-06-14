from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from threading import Lock
import time
import random
import os

# HTML main page. This page has 16 iframes, each of which causes
# the browser to send an additional request to this server.
# Each iframe will display the number of currently active requests.
html = '''<!DOCTYPE html>
<title>Things!</title>
<style>iframe { width: 23%; border: 0 }</style>
<iframe src="/frame0"></iframe> <iframe src="/frame1"></iframe>
<iframe src="/frame2"></iframe> <iframe src="/frame3"></iframe>
<iframe src="/frame4"></iframe> <iframe src="/frame5"></iframe>
<iframe src="/frame6"></iframe> <iframe src="/frame7"></iframe>
<iframe src="/frame8"></iframe> <iframe src="/frame9"></iframe>
<iframe src="/framea"></iframe> <iframe src="/frameb"></iframe>
<iframe src="/framec"></iframe> <iframe src="/framed"></iframe>
<iframe src="/framee"></iframe> <iframe src="/framef"></iframe>
'''

# Track the number of requests that are in progress.
# This variable will get +1 every time a handler starts processing
# a request, and -1 every time it finishes.
inflight = 0

# To protect the inflight variable from being changed from multiple
# request handlers at once, we need to use a lock.
lock = Lock()


class Parallelometer(BaseHTTPRequestHandler):
    def do_GET(self):
        global inflight, lock
        with lock:
            # We're starting to handle a request.
            inflight += 1
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        if self.path.startswith('/frame'):
            # This request is for iframe contents.
            time.sleep(random.random())  # Slow down by 0-1 seconds.
            self.wfile.write('{} requests in flight'.format(inflight).encode())
        else:
            # This request is for the main page.
            self.wfile.write(html.encode())
            self.wfile.flush()
        with lock:
            # We're done handling a request.
            inflight -= 1


class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    server_address = ('', int(os.environ.get('PORT', '8000')))
    httpd = ThreadHTTPServer(server_address, Parallelometer)
    httpd.serve_forever()
