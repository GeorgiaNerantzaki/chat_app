from flask import Flask
from config import Config
from app.database import db
from app.auth.forms import LoginForm,RegisterForm
from flask_login import LoginManager
from app.models.user import Users
#from app.models.contact import Contact
#from app.models.chat import Chat
import os
from dotenv import load_dotenv
from flask_socketio import SocketIO

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(config_class=Config):
    
    
    load_dotenv(os.path.join(basedir, '.my_env'))
    
    print(f"SECRET_KEY: {os.environ.get('SECRET_KEY')}")
    print(f"DATABASE_URI: {os.environ.get('DATABASE_URI')}")
    app = Flask(__name__)
    socketio = SocketIO(app)
    app.config.from_object(config_class)
    
    app.secret_key = app.config['SECRET_KEY']
    
    login_manager = LoginManager()
    # Initialize Flask extensions here
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
        
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix = '/auth')
    
    if __name__ == "main":
        socketio.run(app, debug = True) 
   
    return app


