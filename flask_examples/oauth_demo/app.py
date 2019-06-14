import sys
from flask import Flask, render_template, redirect, url_for, session, flash
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.contrib.github import make_github_blueprint, github
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized, oauth_error
from sqlalchemy.orm.exc import NoResultFound
from flask_caching import Cache

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY-KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oauth_demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


cache = Cache(config={'CACHE_TYPE': 'redis'})
db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    picture_url = db.Column(db.String)


class OAuth(OAuthConsumerMixin, db.Model):
    # user_id of provider. In this case is github user_id
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


login_manager = LoginManager()
login_manager.login_view = 'github.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


"""
Parameters:
client_id (str) – The client ID for your application on GitHub.
client_secret (str) – The client secret for your application on GitHub
scope (str, optional) – comma-separated list of scopes for the OAuth token
redirect_url (str) – the URL to redirect to after the authentication dance is complete
redirect_to (str) – if redirect_url is not defined, the name of the view to redirect to after the authentication dance is complete. The actual URL will be determined by flask.url_for()
login_url (str, optional) – the URL path for the login view. Defaults to /github
authorized_url (str, optional) – the URL path for the authorized view. Defaults to /github/authorized.
session_class (class, optional) – The class to use for creating a Requests session. Defaults to OAuth2Session.
backend – A storage backend class, or an instance of a storage backend class, to use for this blueprint. Defaults to SessionBackend.
"""
github_blueprint = make_github_blueprint(
    # scope='user:email' --> can no scope
    client_id='533aacc30aa0ac0ad83d', client_secret='ffc6b920b49603523a175afed4c831be58d8fa9e')

app.register_blueprint(github_blueprint, url_prefix="/login")

github_blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)


"""
This signal is sent when the OAuth provider indicates that there was an error with the OAuth dance. This can happen if your application is misconfigured somehow. The user will be redirected to the redirect_url anyway, so it is your responsibility to hook into this signal and inform the user that there was an error.
"""
@oauth_error.connect_via(github_blueprint)
def github_error(blueprint, error, error_description=None, error_uri=None):
    msg = (
        "OAuth error from {name}! "
        "error={error} description={description} uri={uri}"
    ).format(
        name=blueprint.name,
        error=error,
        description=error_description,
        uri=error_uri,
    )
    flash(msg, category="error")


"""
This signal is sent before redirecting to the provider login page. The signal is sent with a url parameter specifying the redirect URL. This signal is mostly useful for doing things like session construction / de-construction before the user is redirected.

@oauth_before_login.connect_via(github_blueprint)
def before_login(blueprint, url):
    session["i_was_here_before"] = "the_login"
    print("i_was_here_before_the_login")
    print(url)
    # if "facebook" in url:
    # do facebook stuff
"""

"""
Returning False from this signal handler indicates to Flask-Dance that it should not try to store the OAuth token for you.

If you return False from a oauth_authorized signal handler, and you do not store the OAuth token in your database, the OAuth token will be lost, and you will not be able to use it to make API calls in the future!

However, notice that the OAuth model has a field called provider_user_id, which is used to store the user ID of the GitHub user. The example code uses that ID to check if we’ve already saved an OAuth token in the database for this GitHub user.
"""
# create/login local user on successful OAuth login
@oauth_authorized.connect_via(github_blueprint)
def github_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with GitHub.", category="error")
        return False

    resp = blueprint.session.get("/user")
    if not resp.ok:
        msg = "Failed to fetch user info from GitHub."
        flash(msg, category="error")
        return False

    github_info = resp.json()
    github_user_id = str(github_info["id"])

    # Find this OAuth token in the database, or create it
    query = OAuth.query.filter_by(
        provider=blueprint.name,
        provider_user_id=github_user_id,
    )
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=github_user_id,
            token=token,
        )

    if oauth.user:
        # If this OAuth token already has an associated local account,
        # log in that local user account.
        # Note that if we just created this OAuth token, then it can't
        # have an associated local account yet.
        login_user(oauth.user)
        flash("Successfully signed in with GitHub.")

    else:
        # If this OAuth token doesn't have an associated local account,
        # create a new local user account for this user. We can log
        # in that account as well, while we're at it.
        user = User(
            # Remember that `email` can be None, if the user declines
            # to publish their email address on GitHub!
            name=github_info["name"],
            username=github_info["login"],
            email=github_info["email"],
            picture_url=github_info["avatar_url"]
        )
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)
        flash("Successfully signed in with GitHub.")

    # Since we're manually creating the OAuth model in the database,
    # we should return False so that Flask-Dance knows that
    # it doesn't have to do it. If we don't return False, the OAuth token
    # could be saved twice, or Flask-Dance could throw an error when
    # trying to incorrectly save it for us.
    return False


@app.route('/logout')
@login_required
def logout():
    """
    token=blueprint.token["access_token"]
    resp=google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    if resp.ok and resp.text:
        logout_user()
    """

    logout_user()
    return redirect(url_for('home'))


@app.route("/")
def index():
    return render_template("home.html")


# hook up extensions to app
db.init_app(app)
login_manager.init_app(app)
cache.init_app(app)


if __name__ == '__main__':
    if "--setup" in sys.argv:
        with app.app_context():
            db.create_all()
            db.session.commit()

    app.run(debug=True)
