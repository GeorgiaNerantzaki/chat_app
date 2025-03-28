from flask import render_template,request,session
from app.main import bp
from flask_login import current_user
from flask import redirect,url_for
from app.main.forms import AddContactForm, CreateChatForm, MessageForm
from app.models.user import Users
from app.models.contact import Contact
from app.models.chat import Chat
from app.models.message import Message
from datetime import datetime
from app.database import db
from sqlalchemy import or_, and_

#default url
@bp.route('/')
def route_default():
    return redirect(url_for('auth.login'))



#@bp.route('/index')
#def index():
 # return render_template('main/index.html')
#url for adding contacts
@bp.route('/addcontact',methods = ['GET','POST'])
def addcontact():
  addcontactform = AddContactForm()     
  if request.method == 'POST':
        email = request.form['contact_email']
        user = Users.query.filter_by(email = email).first() 
        if user:
         newcontact = Contact(user_id1 = current_user.id , user_id2 = user.id, since = datetime.now())
         db.session.add(newcontact)
         db.session.commit()
  return  render_template('main/addcontact.html', form  = addcontactform)
#url for viewing all contatcs to initalize chats or send a message
@bp.route('/allcontacts')
def allcontact():
  form = CreateChatForm()
  allcontacts = Contact.query.filter(or_(Contact.user_id1 == current_user.id, Contact.user_id2 == current_user.id)).all()
  return render_template('main/allcontacts.html', allcontacts = allcontacts, form = form)         

#url to initiate or create chats and redirect to messages 
@bp.route('/createchat/<int:user_id>',methods = ["GET","POST"])
def createchat(user_id):
  #messageform = MessageForm()
  if request.method == "POST":
       user = Contact.query.get(user_id)
       user2 = Users.query.get(user_id)
       #message = request.form.get['message_text']
       existing_chat = Chat.query.filter(or_(and_(Chat.user_id1 == current_user.id, Chat.user_id2 == user_id),and_(Chat.user_id1 == user_id, Chat.user_id2 == current_user.id))).first()
       if existing_chat:
        return redirect(url_for('main.new_message', chat_id = existing_chat.id))
       else:
        newchat = Chat(user_id1= current_user.id, user_id2 = user_id, date = datetime.now())
       #new_message = Message(user_id = current_user.id, chat_id = newchat.id,message_text = message)
        db.session.add(newchat)
       #db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('main.new_message', chat_id = newchat.id))
  #return render_template('main/newmessageform.html')

#urlfor sending messages in a new or existing chat  
@bp.route('/newmessage/<int:chat_id>', methods = ["GET","POST"])
def new_message(chat_id):
     chat = Chat.query.get(chat_id)
     user = current_user.id
     messages = Message.query.filter_by(chat_id = chat_id).all()
     messageform = MessageForm()
     if current_user.id == chat.user_id1:
            other_user = Users.query.get(chat.user_id2)
     else:
           other_user = Users.query.get(chat.user_id1)
     if request.method == "POST":
       message = request.form['message_text']
       new_message = Message(user_id = current_user.id, chat_id = chat_id,message_text = message)
       db.session.add(new_message)
       db.session.commit()
      

     return render_template('main/newmessageform.html', form = messageform, chat = chat, messages = messages, other_user=other_user, user = user)
   
#url for viewing all chats
@bp.route('/allchats/<int:user_id>')
def allchats(user_id):
      user_id = current_user.id
      all_chats = Chat.query.filter(or_(Chat.user_id1 == user_id,Chat.user_id2==user_id)).all()
      return render_template('main/allchats.html', all_chats = all_chats)
    
    
#@bp.route('/chat/<int:chat_id>', methods = ['GET','POST'])
#def chat(chat_id):
      #if request.method == 'POST':
            #form = MessageForm()
            #chat = Chat.query.get(chat_id)
            #messages = Message.query.filter_by(chat_id = chat_id)
            #return render_template('chat.html', chat_id = chat_id, form = form, messages = messages)
      

      
