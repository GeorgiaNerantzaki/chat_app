from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.database import db

class Chat(db.Model):
    __tablename__ = "Chats"
    id = db.Column(db.Integer, primary_key=True)
    user_id1 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id2 = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    #username = db.Column(db.String(80), nullable= False)
    

    user1 = db.relationship('Users', foreign_keys=[user_id1])
    user2 = db.relationship('Users', foreign_keys=[user_id2])
    message_in_chat= db.relationship('Message', back_populates = 'chat')
    def __repr__(self):
        return f'<Chat {self.id}>'