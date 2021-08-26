from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.cars import Car

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to view this page.')
        return redirect('/')
    cars = Car.get_all_cars()
    return render_template('dashboard.html', cars = cars)

@app.route('/cars/new')
def new_car():
    if 'user_id' not in session:
        flash('Please log in to view this page.')
        return redirect('/')
    return render_template('new_car.html')

@app.route('/cars/create', methods=['POST'])
def create_car():
    print(request.form)
    if Car.car_validator(request.form):
        data = {
            'price': request.form['price'],
            'model': request.form['model'],
            'make': request.form['make'],
            'year': request.form['year'],
            'description': request.form['description'],
            'users_id': session['user_id']
        }
        Car.create_car(data)
        return redirect('/dashboard')
    
    return redirect('/cars/new')

@app.route('/cars/<int:car_id>')
def car_information(car_id):

    car = Car.get_car_by_id({'id': car_id})

    return render_template('car_data.html', car = car)

@app.route('/cars/<int:car_id>/edit')
def edit_car(car_id):

    car = Car.get_car_by_id({'id': car_id})

    if car.user.id != session['user_id']:
        return redirect('/dashboard')
    
    return render_template('edit_car.html', car = car)

@app.route('/cars/<int:car_id>/update', methods=['POST'])
def update_car(car_id):
    car = Car.get_car_by_id({'id': car_id})

    if car.user.id != session['user_id']:
        return redirect('/dashboard')
    
    if Car.car_validator(request.form):
        data = {
            'id': car_id,
            'price': request.form['price'],
            'model': request.form['model'],
            'make': request.form['make'],
            'year': request.form['year'],
            'description': request.form['description']
        }
        Car.update_car(data)
        return redirect('/dashboard')

@app.route('/cars/<int:car_id>/delete')
def delete_car(car_id):
    data = {
        'id':car_id
    }
    Car.delete_car(data)
    return redirect('/dashboard')

@app.route('/cars/purchases')
def user_purchases():
    if 'user_id' not in session:
        flash('Please log in to view this page.')
        return redirect('/')
    return render_template('user_purchases.html')