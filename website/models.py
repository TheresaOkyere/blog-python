from . import db 
from flask_login import UserMixin
from sql_alchemy.sql import func

class user(db.model, UserMixin):
    id = db.column(db.Interger, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    username = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.Date(timezone=True), default=func.now())