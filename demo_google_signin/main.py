from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from oauth2client.client import credentials_from_clientsecrets_and_code
from google.oauth2 import id_token as oauth2_id_token
from google.auth.transport import requests as transport_requests

from flask import Flask, render_template, request, redirect, make_response, session, url_for
from flask.json import jsonify
import requests
import httplib2
import os
import json
import string
import random


# Use the client_secret.json file to identify the application requesting
# authorization. The client ID (from that file) and access scopes are required.
'''
client_id	Required. The client ID for your application. You can find this value in the API Console. In Python, call the from_client_secrets_file method to retrieve the client ID from a client_secret.json file. (You can also use the from_client_config method, which passes the client configuration as it originally appeared in a client secrets file but doesn't access the file itself.)

redirect_uri	Required. Determines where the API server redirects the user after the user completes the authorization flow. The value must exactly match one of the redirect_uri values listed for your project in the API Console. Note that the http or https scheme, case, and trailing slash ('/') must all match.

scope	Required. A list of scopes that identify the resources that your application could access on the user's behalf. These values inform the consent screen that Google displays to the user.
Scopes enable your application to only request access to the resources that it needs while also enabling users to control the amount of access that they grant to your application. Thus, there is an inverse relationship between the number of scopes requested and the likelihood of obtaining user consent. In Python, use the same method you use to set the client_id to specify the list of scopes.

access_type	Recommended. Indicates whether your application can refresh access tokens when the user is not present at the browser. Valid parameter values are online, which is the default value, and offline.

Set the value to offline if your application needs to refresh access tokens when the user is not present at the browser. This is the method of refreshing access tokens described later in this document. This value instructs the Google authorization server to return a refresh token and an access token the first time that your application exchanges an authorization code for tokens.
'''

# This variable specifies the name of a file that contains the OAuth 2.0
# information for this application, including its client_id and client_secret.
# Use for DEMO ONLY, YOU SHOULD NEVER STORE SECRET INSIDE YOUR PROJECT FOLDER --> USE ENV VARIABLES INSTEAD
CLIENT_SECRETS_FILE = "client_secrets.json"

# Use for DEMO ONLY, YOU SHOULD NEVER STORE SECRET INSIDE YOUR PROJECT FOLDER --> USE ENV VARIABLES INSTEAD
fb_app_id = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_id']
fb_app_secret = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_secret']

# Use for DEMO ONLY, YOU SHOULD NEVER STORE SECRET INSIDE YOUR PROJECT FOLDER --> USE ENV VARIABLES INSTEAD
github_client_id = json.loads(open('github_client_secrets.json', 'r').read())['web']['client_id']
github_client_secret = json.loads(open('github_client_secrets.json', 'r').read())['web']['client_secret']

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
# Use for DEMO ONLY, YOU SHOULD NEVER STORE SECRET INSIDE YOUR PROJECT FOLDER --> USE ENV VARIABLES INSTEAD
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/userinfo.profile']
API_SERVICE_NAME = 'drive'
API_VERSION = 'v2'
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

app = Flask(__name__)
# Note: A secret key is included in the sample so that it works.
# If you use this code in your application, replace this with a truly secret
# key. See http://flask.pocoo.org/docs/0.12/quickstart/#sessions.
app.secret_key = 'REPLACE ME - this value is here as a placeholder.'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/google_signin')
def google_signin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    session['state'] = state

    return render_template('google_signin.html', state=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # protect against CSRF attacks.
    if not request.headers.get('X-Requested-With'):
        response = make_response(json.dumps('Not include an `X-Requested-With` header.'), 403)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Validate state token
    if request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code
    code = request.data

    # Exchange auth code for access token, refresh token, and ID token
    credentials = credentials_from_clientsecrets_and_code(CLIENT_SECRETS_FILE, ['profile', 'email'], code)

    # check `iss`
    if credentials.id_token['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        response = make_response(json.dumps('Invalid `iss`.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the id token is valid.
    idinfo = oauth2_id_token.verify_oauth2_token(credentials.id_token_jwt, transport_requests.Request(), CLIENT_ID)
    # check `iss`
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        response = make_response(json.dumps('Invalid `iss`.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    session['access_token'] = credentials.access_token
    session['gplus_id'] = gplus_id

    '''# Get user info
    http_auth = credentials.authorize(httplib2.Http())
    client = build('oauth2', 'v2', http=http_auth)

    userinfo = client.userinfo().get().execute()'''

    # Get profile info from ID token
    userid = credentials.id_token['sub']
    session['userid'] = userid
    print(userid)

    email = credentials.id_token['email']
    session['email'] = email
    print(email)

    name = credentials.id_token['name']
    session['name'] = name
    print(name)

    picture = credentials.id_token['picture']
    session['picture'] = picture
    print(picture)

    # ADD PROVIDER TO LOGIN SESSION
    session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    '''user_id = getUserID(userinfo["email"])
    if not user_id:
        user_id = createUser(session)
    session['user_id'] = user_id'''
    return email


@app.route('/fb_signin')
def fb_signin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    session['state'] = state

    return render_template('facebook_signin.html', state=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    # protect against CSRF attacks.
    if not request.headers.get('X-Requested-With'):
        response = make_response(json.dumps('Not include an `X-Requested-With` header.'), 403)
        response.headers['Content-Type'] = 'application/json'
        return response

    if request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = request.data
    access_token = access_token.decode()

    print("access token received %s " % access_token)

    # call API to get long-lived access_token
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (fb_app_id, fb_app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    # get long-lived access_token from result
    access_token = data["access_token"]

    print("token received %s " % access_token)

    url = 'https://graph.facebook.com/v3.2/me?access_token=%s&fields=name,id,email' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    print("data received %s " % data)

    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    session['username'] = data["name"]
    session['email'] = data["email"]
    session['facebook_id'] = data["id"]

    session['provider'] = 'facebook'

    # The token must be stored in the session in order to properly logout
    session['access_token'] = access_token

    # Get user picture
    url = 'https://graph.facebook.com/v3.2/me/picture?access_token=%s&redirect=0&height=200&width=200' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    picture_url = data["data"]["url"]

    print("picture received %s " % picture_url)

    session['picture'] = picture_url

    '''# see if user exists
    user_id = getUserID(session['email'])
    if not user_id:
        user_id = createUser(session)
    session['user_id'] = user_id'''

    output = ''
    output += '<h1>Welcome, '
    output += session['username']

    output += '!</h1>'
    output += '<img src="'
    output += session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    return output


@app.route('/github_signin')
def github_signin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    session['state'] = state

    return render_template('github_signin.html', state=state)


@app.route('/github_authorize')
def github_authorize():
    if request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    session['state'] = state

    url = f"https://github.com/login/oauth/authorize?scope=read:user&client_id={github_client_id}&state={state}"

    return redirect(url)


@app.route('/github_callback')
def github_callback():
    if request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    code = request.args.get('code')

    # Exchange this code for an access token
    url = "https://github.com/login/oauth/access_token"
    url_headers = {"Accept": "application/json"}
    parameters = {"client_id": github_client_id, "client_secret": github_client_secret, "code": code}

    result = requests.post(url, params=parameters, headers=url_headers)
    data = result.json()
    print(data)

    # check if the needed scope is granted
    if data["scope"] != "read:user":
        response = make_response(json.dumps('Needed scope was not provided by User.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Use the access token to access the API
    access_token = data["access_token"]
    token_header = f"token {access_token}"
    url = "https://api.github.com/user"
    url_headers = {"Authorization": token_header}

    result = requests.get(url, headers=url_headers)
    data = result.json()

    # store data
    session['username'] = data["name"]
    session['email'] = data["email"]
    session['github_id'] = data["id"]
    session['picture'] = data["avatar_url"]

    session['provider'] = 'github'

    # The token must be stored in the session in order to properly logout
    session['access_token'] = access_token

    '''# see if user exists
    user_id = getUserID(session['email'])
    if not user_id:
        user_id = createUser(session)
    session['user_id'] = user_id'''

    return jsonify(**data)


@app.route('/test')
def test_api_request():
    if 'credentials' not in session:
        return redirect('authorize')

    # Load credentials from the session.
    credentials = Credentials(**session['credentials'])

    drive = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    files = drive.files().list().execute()

    # Save credentials back to session in case access token was refreshed.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    session['credentials'] = credentials_to_dict(credentials)

    return jsonify(**files)


@app.route('/profile')
def client_profile():
    if 'credentials' not in session:
        return redirect('authorize')

    # Load credentials from the session.
    credentials = Credentials(**session['credentials'])

    client = build('oauth2', 'v2', credentials=credentials)

    userinfo = client.userinfo().get().execute()

    # Save credentials back to session in case access token was refreshed.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    session['credentials'] = credentials_to_dict(credentials)

    return jsonify(**userinfo)


@app.route('/authorize')
def authorize():
    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)

    flow.redirect_uri = url_for('oauth2callback', _external=True)

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    session['state'] = state

    return redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    state = session['state']

    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return redirect(url_for('test_api_request'))


@app.route('/revoke')
def revoke():
    if 'credentials' not in session:
        return ('You need to <a href="/authorize">authorize</a> before ' +
                'testing the code to revoke credentials.')

    credentials = Credentials(**session['credentials'])

    revoke = requests.post('https://accounts.google.com/o/oauth2/revoke',
                           params={'token': credentials.token},
                           headers={'content-type': 'application/x-www-form-urlencoded'})

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        return render_template('index.html', message='Credentials successfully revoked.')
    else:
        return render_template('index.html', message='An error occurred.')


@app.route('/clear')
def clear_credentials():
    if 'credentials' in session:
        del session['credentials']
    return render_template('index.html', message='Credentials have been cleared.')


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification.
    # ACTION ITEM for developers:
    #     When running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Specify a hostname and port that are set as a valid redirect URI
    # for your API project in the Google API Console.
    app.run('localhost', 8080, debug=True)
