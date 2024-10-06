import click
from flask import Flask
from flask.cli import with_appcontext
from dotenv import load_dotenv
from h3.db import db
from h3.models import Player, Match, MatchOpponent
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from h3.models.player import PlayerModelView
from h3.models.match import MatchModelView
from h3.models.tournament import Tournament



def create_app():
    app = Flask(__name__)
    app.config.from_object("h3.config")
    app.config.from_object("h3backend.config")

    db.init_app(app)
    app.db = db

    app.logger.info("App created")
    app.logger.info(app.config.get("TEST_OVERWRITE"))
    
    admin = Admin(app, name='h3', template_mode='bootstrap4')
    
    admin.add_view(ModelView(Tournament, db.session))
    admin.add_view(PlayerModelView(Player, db.session))
    admin.add_view(MatchModelView(Match, db.session))
    # admin.add_view(ModelView(Post, db.session))
     
    return app


