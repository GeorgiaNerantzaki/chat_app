from app.auth import bp
from flask import render_template,request,redirect,url_for,flash
from app.auth.forms import LoginForm,RegisterForm
from app.models.user import Users
from app.auth.utils import hash_pass,verify_pass
from flask_login import login_user,current_user,logout_user
from app.database import db


@bp.route('/login',methods = ['GET','POST'])
def login():
    loginform  = LoginForm()
    if 'login' in request.form:
        email = request.form['email']
        password = request.form['password']
        print(f"Login attempt: email={email}, password={password}")
        user = Users.query.filter_by(email = email).first()
        if user:
            print(f"User found: {user}")
        else:
            print("No user found with this email.")
        if user.password == password:
            login_user(user)
            print(f"Logged in user: {user.email}")  # Check user details
            flash('You logged in successfully!', 'success')
            return redirect(url_for('main.allchats', user_id  = user.id))
        else:
            print("Login failed. Invalid email or password.")
            flash('Invalid email or password', 'error')
            
        if not current_user.is_authenticated:
            flash('Invalid email or password',"error")
            return render_template('auth/login.html', form=loginform)
        else:
            return render_template('main/allchats.html')

        
    return render_template('auth/login.html', form = loginform)






@bp.route('/register',methods = ['GET','POST'])
def register():
    registerform  = RegisterForm()
    if 'register' in request.form:
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        firstname = request.form['first_name']
        lastname = request.form['last_name'] 
        username  = request.form['username']

        user = Users.query.filter_by(email = email).first()
        if user and verify_pass(password, user.password) :
            flash('User with this email exists','error')
            return redirect(url_for('auth.register'))
        user = Users.query.filter_by(username= username).first()
        if user :
            flash('User with this username exists','error')
            return redirect(url_for('auth.register'))
        
        user  = Users(email = email, username = username,password = password,first_name = firstname,last_name = lastname)
        user.active = True
        db.session.add(user)
        db.session.commit()

    return render_template('auth/register.html',form = registerform)
 
 
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
        