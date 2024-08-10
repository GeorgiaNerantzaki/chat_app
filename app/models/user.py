from app.database import db
from flask_security import UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    
    contact_user1 = db.relationship('Contact', foreign_keys='Contact.user_id1', back_populates='user1')
    contact_user2 = db.relationship('Contact', foreign_keys='Contact.user_id2', back_populates='user2')
    message_from_user = db.relationship('Message', back_populates='user')
    
    # chat_user1 = db.relationship('Chat', back_populates='user1', foreign_keys='Chat.user_id1')
    # chat_user2 = db.relationship('Chat', back_populates='user2', foreign_keys='Chat.user_id2')
    
    def __repr__(self):
        return f'<User "{self.username}">'