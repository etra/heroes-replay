from h3.db import db
from h3.models.town import Town
from slugify import slugify

class HeroClass(db.Model):
    __tablename__ = "hero_classes"

    id = db.Column(db.String(length=32), primary_key=True)

    name = db.Column(db.String(length=32), nullable=False)
    heroes = db.relationship("Hero", backref="hero_class", lazy=True)
    
    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<HeroClass {self.name}>"

    @staticmethod
    def create_item(name):
        item = HeroClass.query.filter_by(name=name).first()
        if not item:
            item_id = slugify(name)
            item = HeroClass(id=item_id, name=name)
            
        return item


class Hero(db.Model):
    __tablename__ = "heroes"

    id = db.Column(db.String(length=32), primary_key=True)

    name = db.Column(db.String(length=32), nullable=False)

    hero_class_id = db.Column(db.String(length=32), db.ForeignKey('hero_classes.id'), nullable=False)
    town_name = db.Column(db.String(length=32), db.ForeignKey('towns.id'), nullable=False)
    
    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<Hero {self.name} of {self.town.name}>"

    @staticmethod
    def create_item(name, hero_class_name, town_name):
        #todo: Improve reading from databse instead of filter_by use what ever is needed to point directly to primary key
        item = Hero.query.filter_by(name=name).first()
        if not item:
            item_id = slugify(name)
            hero_class_id = slugify(hero_class_name)
            hero_class = HeroClass.query.filter_by(id=hero_class_id).first()
            town_id = slugify(town_name)
            town = Town.query.filter_by(id=town_id).first()

            item = Hero(id=item_id, name=name, hero_class=hero_class, town=town)
            
        return item