from h3.db import db
from slugify import slugify

class Town(db.Model):
    __tablename__ = "towns"
    id = db.Column(db.String(length=32), primary_key=True)
    name = db.Column(db.String(length=32))
    heroes = db.relationship("Hero", backref="town", lazy=True)
    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            }
    
    @staticmethod
    def from_dict(data):
        town = Town.query.get(data.get("id"))
        if not town:
            town = Town(
            id=data.get("id"),
            name=data.get("name"),
            created_time=data.get("created_time"),
            updated_time=data.get("updated_time")
            )

        return town
    

    @staticmethod
    def create_town(name):
        town = Town.query.filter_by(name=name).first()
        if not town:
            town_id = slugify(name)
            town = Town(id=town_id, name=name)
            
        return town
        

    def __repr__(self):
        return f"<Town {self.name}>"
