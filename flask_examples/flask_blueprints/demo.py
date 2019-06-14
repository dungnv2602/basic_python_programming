from flask import Flask

app = Flask(__name__)

from api.routes import mod
from site.routes import mod

app.register_blueprint(api.routes.mode, url_prefix='/api')
app.register_blueprint(site.routes.mode)