from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.database import db


class Message(db.Model):
    __tablename__ = "Messages"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('Chats.id'), nullable=False)
    message_text = db.Column(db.Text, nullable=True)
    
    
    user = db.relationship('Users', back_populates='message_from_user')
    chat = db.relationship('Chat', back_populates='message_in_chat')
    def __repr__(self):
        return f'<Message "{self.message_text}">'