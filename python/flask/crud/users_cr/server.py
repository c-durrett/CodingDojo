from flask import Flask, render_template, request, redirect
from users import User

app=Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template("users.html", users=users)

@app.route('/new')
def add_user():
# next step is adding the form to create new users

if __name__=="__main__":
    app.run(debug=True)