from settings import db
from sqlalchemy import Column, Integer, Text
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60) )
    email = db.Column(db.String(60))
    password = db.Column(db.String(500))
    mobile_number = db.Column(db.String(300))
    create_at = db.Column(
        db.TIMESTAMP,
        default=datetime.utcnow,
        nullable=False
      )

    def __str__(self):
        return self.name + self.email + str(self.mobile_number)

