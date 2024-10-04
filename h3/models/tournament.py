from h3.db import db
from slugify import slugify

class Tournament(db.Model):
    __tablename__ = "tournaments"

    id = db.Column(db.String(length=64), primary_key=True)

    name = db.Column(db.String(length=64), nullable=False)

    website = db.Column(db.String(length=512), nullable=False)
    
    created_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "website": self.website,
            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_time": self.updated_time.strftime("%Y-%m-%d %H:%M:%S"),
            }

    def __repr__(self):
        return f"<Tournament {self.name}>"

    @staticmethod
    def create_item(name, website):
        item = Tournament.query.filter_by(name=name).first()
        if not item:
            item_id = slugify(name)
            item = Tournament(id=item_id, name=name, website=website)
            
            
        return item