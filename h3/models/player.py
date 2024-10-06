from h3.db import db
from slugify import slugify
from flask_admin.contrib.sqla import ModelView

class PlayerModelView(ModelView):
    form_columns = ['name', 'youtube', 'twitch', 'discord']
    column_list = ['player_id', 'name', 'youtube', 'twitch', 'discord']

    def on_model_change(self, form, model, is_created):
        if 'name' in form:
            model.player_id = slugify(form.name.data)

class Player(db.Model):
    __tablename__ = 'players'

    player_id = db.Column(db.String(length=64), primary_key=True)
    name = db.Column(db.String(length=64))
    
    youtube = db.Column(db.String(100))
    twitch = db.Column(db.String(100))
    discord = db.Column(db.String(100))

    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "youtube": self.youtube,
            "twitch": self.twitch,
            "discord": self.discord,
            
            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_time": self.updated_time.strftime("%Y-%m-%d %H:%M:%S"),
            }

    @staticmethod
    def from_dict(data):
        player = Player.query.get(data.get("player_id"))
        
        if not player:
            player = Player(
            player_id=data.get("player_id"),
            name=data.get("name"),
            youtube=data.get("youtube"),
            twitch=data.get("twitch"),
            discord=data.get("discord"),
            created_time=data.get("created_time"),
            updated_time=data.get("updated_time")
            )
        return player

    @staticmethod
    def create_item(name):
        player = Player.query.filter_by(name=name).first()
        if not player:
            player_id = slugify(name)
            player = Player(id=player_id, name=name)
            
        return player