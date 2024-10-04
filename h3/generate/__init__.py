import click
from flask.cli import with_appcontext
from h3.generate.towns import generate_static_data
from h3.generate.back_restore import backup, restore
from flask import current_app as app

@click.command(name="generate")
@with_appcontext
def generate_data():
    generate_static_data()

@click.command(name="create_db")
@with_appcontext
def create_db():
    from h3.db import db
    db.drop_all()
    db.create_all()    

@click.command(name="backup")
@with_appcontext
def backup_command():
    backup()

@click.command(name="restore")
@with_appcontext
def restore_command():
    restore()

