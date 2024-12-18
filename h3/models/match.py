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
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from urllib.parse import urlparse, parse_qs
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

    #todo: fix prefill - does not work
    # def on_form_prefill(self, form, id):
    #     # Get the existing MatchOpponent from the database
    #     match_opponent = MatchOpponent.query.get(id)
    #     print(f"match_opponent: {match_opponent}")
    #     # Ensure each form field is populated with the actual values from the database
    #     form.player_id.data = Player.query.get(match_opponent.player_id)
    #     form.town_id.data = Town.query.get(match_opponent.town_id)
    #     form.hero_id.data = Hero.query.get(match_opponent.hero_id)
    #     form.color_id.data = Color.query.get(match_opponent.color_id)

    #     super(MatchOpponentInline, self).on_form_prefill(form, id)

    def on_model_change(self, form, model, is_created):
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
    player: Mapped["Player"] = db.relationship(primaryjoin="foreign(MatchOpponent.player_id) == Player.player_id", uselist=False)
    town_id = db.Column(db.String(32), nullable=False)
    town: Mapped["Town"] = db.relationship(primaryjoin="foreign(MatchOpponent.town_id) == Town.id", uselist=False)
    hero_id = db.Column(db.String(32), nullable=False)
    hero: Mapped["Hero"] = db.relationship(primaryjoin="foreign(MatchOpponent.hero_id) == Hero.id", uselist=False)
    color_id = db.Column(db.String(12), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "match_id": self.match_id,
            "player_id": self.player_id,
            "player": self.player.to_dict(),
            "town_id": self.town_id,
            "town": self.town.to_dict(),
            "hero_id": self.hero_id,
            "hero": self.hero.to_dict(),
            "color_id": self.color_id,
        }

class MatchModelView(ModelView):
    def on_form_prefill(self, form, id):
        # Get the existing Match from the database
        match = Match.query.get(id)
        if match:
            # Ensure each form field is populated with the actual values from the database
            form.template_id.data = match.template_id
            form.tournament_id.data = match.tournament_id
            form.player_id.data = Player.query.get(match.player_id)
            form.town_id.data = Town.query.get(match.town_id)
            form.hero_id.data = Hero.query.get(match.hero_id)
            form.color_id.data = Color.query.get(match.color_id)
            form.match_type_id.data = MatchType.query.get(match.match_type_id)
            current_app.logger.info(f"match: {match.opponents}")
            if match.opponents:
                for inline_form, opponent in zip(form.opponents.entries, match.opponents):
                    inline_form.form.player_id.data = Player.query.get(opponent.player_id)
                    inline_form.form.town_id.data = Town.query.get(opponent.town_id)
                    inline_form.form.hero_id.data = Hero.query.get(opponent.hero_id)
                    inline_form.form.color_id.data = Color.query.get(opponent.color_id)
                    inline_form.form.id.data = opponent.id
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
        model.template_id = form.template_id.data.id if form.template_id.data else None
        model.tournament_id = form.tournament_id.data.id if form.tournament_id.data else None
        model.player_id = form.player_id.data.player_id if form.player_id.data else None
        model.town_id = form.town_id.data.id if form.town_id.data else None
        model.hero_id = form.hero_id.data.id if form.hero_id.data else None
        model.color_id = form.color_id.data.id if form.color_id.data else None
        model.match_type_id = form.match_type_id.data.id if form.match_type_id.data else None

        left_opponents = []
        for opponent_form in form.opponents.entries:
            print(opponent_form.object_data)
            if opponent_form._should_delete:
                db.session.delete(opponent_form.object_data)
            elif opponent_form.object_data is not None:
                model.opponents = [opponent_form.object_data]
                
        db.session.commit()
        return super(MatchModelView, self).on_model_change(form, model, is_created)
    
    column_list = ('id', 'match_type_id', 'player_id', 'link', 'created_time', 'updated_time')
    form_columns = (
        'match_type_id',

        'link', 'video_title', 'videos_short_description',
        
        
        'template_id', 'tournament_id', 
        
        'player_id', 'town_id', 'hero_id', 'color_id', 
        'opponents'
        )


class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #match information
    match_type_id = db.Column(db.String(12), nullable=True)
    template_id = db.Column(db.String(64), nullable=False)
    tournament_id = db.Column(db.String(64), nullable=True)

    
    #video info
    link = db.Column(db.String(512), nullable=False)
    video_title = db.Column(db.String(512), nullable=True)
    videos_short_description = db.Column(db.String(512), nullable=True)

    #POV information
    player_id = db.Column(db.String(60), nullable=False)
    player: Mapped["Player"] = db.relationship(primaryjoin="foreign(Match.player_id) == Player.player_id", uselist=False)
    town_id = db.Column(db.String(32), nullable=True)
    town: Mapped["Town"] = db.relationship(primaryjoin="foreign(Match.town_id) == Town.id", uselist=False)
    hero_id = db.Column(db.String(32), nullable=True)
    hero: Mapped["Hero"] = db.relationship(primaryjoin="foreign(Match.hero_id) == Hero.id", uselist=False)
    color_id = db.Column(db.String(12), nullable=True)

    #opponents information
    opponents = db.relationship('MatchOpponent', backref='match', lazy=True)

    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def video_id(self):
        # import re
        # Parse the URL and check if it contains 'v' as a query parameter
        parsed_url = urlparse(self.link)
        if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
            query_params = parse_qs(parsed_url.query)
            if 'v' in query_params:
                return query_params['v'][0]
    
        # Check for youtu.be short URL format
        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]  # Remove the leading '/'

        # If no match is found, return None
        return None

    @property
    def thumbnail(self):
        return f"https://i.ytimg.com/vi_webp/{self.video_id}/sddefault.webp"

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "player": self.player.to_dict(),
            "town_id": self.town_id,
            "town": self.town.to_dict(),
            "hero_id": self.hero_id,
            "hero": self.hero.to_dict(),
            "color_id": self.color_id,
            "link": self.link,
            "video_title": self.video_title,
            "thumbnail": self.thumbnail,
            "video_id": self.video_id,
            "opponents": [opponent.to_dict() for opponent in self.opponents],

            

            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_time": self.updated_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
