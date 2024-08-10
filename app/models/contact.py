from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.database import db

class Contact(db.Model):
    __tablename__ = "Contacts"
    id = db.Column(db.Integer, primary_key=True)
    user_id1 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user_id2 = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    since = db.Column(db.Date, nullable=False)

    user1 = db.relationship('Users', foreign_keys=[user_id1], back_populates='contact_user1')
    user2 = db.relationship('Users', foreign_keys=[user_id2], back_populates='contact_user2')
    
    def __repr__(self):
      return f'<Friendship {self.id}>'