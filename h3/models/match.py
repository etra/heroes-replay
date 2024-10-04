from h3.db import db
from slugify import slugify
from typing import List

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
    def create_item(name):
        item = Color.query.filter_by(name=name).first()
        if not item:
            item_id = slugify(name)
            item = Color(id=item_id, name=name)
        return item


class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)

    player_id = db.Column(db.String(60), nullable=False)
    town_id = db.Column(db.String(32), nullable=False)
    hero_id = db.Column(db.String(32), nullable=False)
    color_id = db.Column(db.String(12), nullable=False)

    opponents = db.relationship('MatchOpponent', backref='match', lazy=True)

    link = db.Column(db.String(512), nullable=False)

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

class MatchOpponent(db.Model):
    __tablename__ = 'match_opponents'

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    player_id = db.Column(db.String(60), nullable=False)
    town_id = db.Column(db.String(32), nullable=False)
    hero_id = db.Column(db.String(32), nullable=False)
    color_id = db.Column(db.String(12), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "game_match_id": self.game_match_id,
            "player_id": self.player_id,
            "town_id": self.town_id,
            "hero_id": self.hero_id,
            "color_id": self.color_id,
            
            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_time": self.updated_time.strftime("%Y-%m-%d %H:%M:%S"),
            }