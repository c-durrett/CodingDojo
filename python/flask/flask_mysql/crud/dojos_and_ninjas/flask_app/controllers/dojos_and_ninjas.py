from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("both.html", dojos = dojos)

@app.route("/ninjas")
def users():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos = dojos)

@app.route("/dojos/<int:num>")
def single_dojo(num):
    data = {
        "id": num
    }
    dojo = Dojo.single_dojo_w_ninjas(data)
    print(dojo)
    return render_template("dojos.html", dojo = dojo)

@app.route('/ninjas/add', methods=['POST'])
def create_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form['last_name'],
        "age" : request.form["age"]
    }
    Ninja.add_ninja(data)
    dojo_id = request.form["dojo_id"]
    link = f'/dojos/{dojo_id}'
    return redirect(link)

@app.route('/dojos/add', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['new_dojo']
    }
    Dojo.add_dojo(data)
    return redirect("/dojos")


