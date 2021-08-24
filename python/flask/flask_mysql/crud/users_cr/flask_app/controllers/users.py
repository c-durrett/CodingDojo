from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("users.html", users=users)

@app.route('/user/new')
def new():
    return render_template("user_new.html")

@app.route('/user/create', methods=['POST'])
def add_user():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    print(request.form)
    User.save(data)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("user_show.html", user=User.get_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("user_edit.html", user=User.get_one(data))

@app.route('/user/update/<int:id>', methods=['POST'])
def update(id):
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    User.destroy(data)
    return redirect('/users')