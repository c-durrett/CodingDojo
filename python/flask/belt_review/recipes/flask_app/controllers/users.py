from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_bcrypt import Bcrypt

from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register_user():
    # validate user
    if (User.validate_registration(request.form)) == True:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        User.create_user(data)
        flash("You've registered, please log in!")
    # if user is valid, create record in DB
    # redirect back to index
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def login_user():

    # check if user exists
    users = User.get_user_by_email(request.form)
    if len(users) != 1:
        flash('Email is incorerct.')
        return redirect('/')

    user = users[0]

    # if user exists, check password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is incorrect.')
        return redirect('/')

    # save data in session and redirect to the success page
    session['user_id'] = user.id
    session['user_first_name'] = user.first_name
    session['user_last_name'] = user.last_name
    session['user_email'] = user.email
    return redirect('/dashboard')


@app.route('/users/logout')
def logout():
    session.clear()
    flash("You've logged out successfully.")
    return redirect('/')

