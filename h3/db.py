from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
db: SQLAlchemy = SQLAlchemy()
session: Session = db.session
