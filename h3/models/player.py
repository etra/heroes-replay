from h3.db import db
from slugify import slugify

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.String(length=64), primary_key=True)
    name = db.Column(db.String(length=64))
    
    youtube = db.Column(db.String(100))
    twitch = db.Column(db.String(100))
    discord = db.Column(db.String(100))

    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "youtube": self.youtube,
            "twitch": self.twitch,
            "discord": self.discord,
            
            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_time": self.updated_time.strftime("%Y-%m-%d %H:%M:%S"),
            }


    @staticmethod
    def create_item(name):
        player = Player.query.filter_by(name=name).first()
        if not player:
            player_id = slugify(name)
            player = Player(id=player_id, name=name)
            
        return player