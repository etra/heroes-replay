from h3.db import db
from slugify import slugify
from typing import List
from h3.models.player import Player
from h3.models.town import Town
from h3.models.heroes import Hero
from h3.models.template import Template
from h3.models.tournament import Tournament
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.fields import  QuerySelectField 
from flask_admin.model.form import InlineFormAdmin
from flask import current_app

class MatchType(db.Model):
    __tablename__ = 'match_types'

    id = db.Column(db.String(length=12), primary_key=True)
    name = db.Column(db.String(12), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            }

    @staticmethod
    def from_dict(data):
        item = MatchType.query.get(data.get("id"))
        if not item:
            item = MatchType(
            id=data.get("id"),
            name=data.get("name")
            )

        return item

    @staticmethod
    def create_item(name):
        item = MatchType.query.filter_by(name=name).first()
        if not item:
            item_id = slugify(name)
            item = MatchType(id=item_id, name=name)
        return item


class Color(db.Model):
    __tablename__ = 'colors'

    id = db.Column(db.String(length=12), primary_key=True)
    name = db.Column(db.String(12), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            }

    @staticmethod
    def from_dict(data):
        item = Color.query.get(data.get("id"))
        if not item:
            item = Color(
            id=data.get("id"),
            name=data.get("name")
            )

        return item

    @staticmethod
    def create_item(name):
        item = Color.query.filter_by(name=name).first()
        if not item:
            item_id = slugify(name)
            item = Color(id=item_id, name=name)
        return item

class MatchOpponentInline(InlineFormAdmin):
    # form_columns = ['player_id', 'town_id', 'hero_id', 'color_id']
    form_extra_fields = {
        'player_id': QuerySelectField(
            'Player',
            query_factory=lambda: Player.query.all(),
            get_label='name',
            get_pk=lambda x: x.player_id
        ),
        'town_id': QuerySelectField(
            'Town',
            query_factory=lambda: Town.query.all(),
            get_label='name',
            get_pk=lambda x: x.id
        ),
        'hero_id': QuerySelectField(
            'Hero',
            query_factory=lambda: Hero.query.all(),
            get_label=lambda x: f"{x.town.name} {x.name}",
            get_pk=lambda x: x.id
        ),
        'color_id': QuerySelectField(
            'Color',
            query_factory=lambda: Color.query.all(),
            get_label='name',
            get_pk=lambda x: x.id
        )
    }

    def on_form_prefill(self, form, id):
        # Get the existing MatchOpponent from the database
        match_opponent = MatchOpponent.query.get(id)
        # Ensure each form field is populated with the actual values from the database
        form.player_id.data = match_opponent.player_id
        form.town_id.data = match_opponent.town_id
        form.hero_id.data = match_opponent.hero_id
        form.color_id.data = match_opponent.color_id

        super(MatchOpponentInline, self).on_form_prefill(form, id)

    def on_model_change(self, form, model, is_created):
        current_app.logger.info(f"form: {form.data}")
        current_app.logger.info(f"form: {model}")
        model.player_id = form.player_id.data.player_id if form.player_id.data else None
        model.town_id = form.town_id.data.id if form.town_id.data else None
        model.hero_id = form.hero_id.data.id if form.hero_id.data else None
        model.color_id = form.color_id.data.id if form.color_id.data else None
        return super(MatchOpponentInline, self).on_model_change(form, model, is_created)

class MatchOpponent(db.Model):
    __tablename__ = 'match_opponents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    player_id = db.Column(db.String(60), nullable=False)
    town_id = db.Column(db.String(32), nullable=False)
    hero_id = db.Column(db.String(32), nullable=False)
    color_id = db.Column(db.String(12), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "match_id": self.match_id,
            "player_id": self.player_id,
            "town_id": self.town_id,
            "hero_id": self.hero_id,
            "color_id": self.color_id,
        }

class MatchModelView(ModelView):
    def on_form_prefill(self, form, id):
        # Get the existing Match from the database
        match = Match.query.get(id)
        # Ensure each form field is populated with the actual values from the database
        form.template_id.data = match.template_id
        form.tournament_id.data = match.tournament_id
        form.player_id.data = match.player_id
        form.town_id.data = match.town_id
        form.hero_id.data = match.hero_id
        form.color_id.data = match.color_id
        form.match_type_id.data = match.match_type_id

        super(MatchModelView, self).on_form_prefill(form, id)

    form_extra_fields = {
        'template_id': QuerySelectField(
            'Template',
            query_factory=lambda: Template.query.all(),
            get_label='name',
            get_pk=lambda x: x.id
        ),
        'tournament_id': QuerySelectField(
            'Tournament',
            query_factory=lambda: Tournament.query.all(),
            get_label='name',
            get_pk=lambda x: x.id,
            allow_blank=True,
            blank_text='None'
        ),
        'player_id': QuerySelectField(
            'Player',
            query_factory=lambda: Player.query.all(),
            get_label='name',
            get_pk=lambda x: x.player_id
        ),
        'town_id': QuerySelectField(
            'Town',
            query_factory=lambda: Town.query.all(),
            get_label='name',
            get_pk=lambda x: x.id
        ),
        'hero_id': QuerySelectField(
            'Hero',
            query_factory=lambda: Hero.query.all(),
            get_label=lambda x: f"{x.town.name} {x.name}",
            get_pk=lambda x: x.id
        ),
        'color_id': QuerySelectField(
            'Color',
            query_factory=lambda: Color.query.all(),
            get_label='name',
            get_pk=lambda x: x.id
        ),
        'match_type_id': QuerySelectField(
            'MatchType',
            query_factory=lambda: MatchType.query.all(),
            get_label='name',
            get_pk=lambda x: x.id
        )
    }

    inline_models = (MatchOpponentInline(MatchOpponent),)

    def on_model_change(self, form, model, is_created):
        current_app.logger.info(f"form: {form.data}")
        current_app.logger.info(f"form: {model}")
        model.template_id = form.template_id.data.id if form.template_id.data else None
        model.tournament_id = form.tournament_id.data.id if form.tournament_id.data else None
        model.player_id = form.player_id.data.player_id if form.player_id.data else None
        model.town_id = form.town_id.data.id if form.town_id.data else None
        model.hero_id = form.hero_id.data.id if form.hero_id.data else None
        model.color_id = form.color_id.data.id if form.color_id.data else None
        model.match_type_id = form.match_type_id.data.id if form.match_type_id.data else None
        return super(MatchModelView, self).on_model_change(form, model, is_created)
    
    column_list = ('id', 'match_type_id', 'player_id', 'link', 'created_time', 'updated_time')
    form_columns = (
        'match_type_id',

        'link', 'template_id', 'tournament_id', 
        
        'player_id', 'town_id', 'hero_id', 'color_id', 
        'opponents'
        )


class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    #match information
    link = db.Column(db.String(512), nullable=False)
    match_type_id = db.Column(db.String(12), nullable=True)
    template_id = db.Column(db.String(64), nullable=False)
    tournament_id = db.Column(db.String(64), nullable=True)

    
    #POV information
    player_id = db.Column(db.String(60), nullable=False)
    town_id = db.Column(db.String(32), nullable=True)
    hero_id = db.Column(db.String(32), nullable=True)
    color_id = db.Column(db.String(12), nullable=True)
    


    #opponents information
    opponents = db.relationship('MatchOpponent', backref='match', lazy=True)

    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "town_id": self.town_id,
            "hero_id": self.hero_id,
            "color_id": self.color_id,
            "link": self.link,

            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_time": self.updated_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
