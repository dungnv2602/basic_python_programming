from flask_examples.config import Config
from flask import Flask

from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

bcrypt = Bcrypt()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from demo_migration.migrations.person import db

    db.init_app(app)

    migrate.init_app(app, db)

    bcrypt.init_app(app)

    return app
