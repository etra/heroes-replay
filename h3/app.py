import click
from flask import Flask
from flask.cli import with_appcontext
from dotenv import load_dotenv
from h3.db import db
from h3.models import *
from flask_migrate import Migrate
from h3.generate import generate_data, create_db, backup_command, restore_command, export_to_ui_command



def create_app():
    app = Flask(__name__)
    app.config.from_object("h3.config")

    db.init_app(app)
    app.db = db

    migrate = Migrate(app, db)

    # from yourapplication.model import db
    # db.init_app(app)

    # from yourapplication.views.admin import admin
    # from yourapplication.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)
    app.cli.add_command(generate_data)
    app.cli.add_command(create_db)
    app.cli.add_command(backup_command)
    app.cli.add_command(restore_command)
    app.cli.add_command(export_to_ui_command)


    return app


