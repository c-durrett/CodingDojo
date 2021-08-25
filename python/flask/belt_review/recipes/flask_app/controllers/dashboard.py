from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.recipes import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to view this page.')
        return redirect('/')
    recipes = Recipe.get_all_recipes()
    return render_template('dashboard.html', recipes = recipes)

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        flash('Please log in to view this page.')
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    print(request.form)
    if Recipe.recipe_validator(request.form):
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions': request.form['instructions'],
            'date': request.form['date'],
            'under_thirty_minutes': request.form['under_thirty_minutes'],
            'users_id': session['user_id']
        }
        Recipe.create_recipe(data)
        return redirect('/dashboard')
    # validate recipe data
    # create recipe
    # if not good, redirect back to new recipe form
    return redirect('/recipes/new')

@app.route('/recipes/<int:recipe_id>')
def recipe_information(recipe_id):

    recipe = Recipe.get_recipe_by_id({'id': recipe_id})

    return render_template('recipe_data.html', recipe = recipe)

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):

    recipe = Recipe.get_recipe_by_id({'id': recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/dashboard')
    
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    recipe = Recipe.get_recipe_by_id({'id': recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/dashboard')

    data = {
        'id': recipe_id,
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions': request.form['instructions'],
            'date': request.form['date'],
            'under_thirty_minutes': request.form['under_thirty_minutes']
        }

    Recipe.update_recipe(data)

    return redirect(f'/recipes/{recipe.id}')

@app.route('/recipes/<int:recipe_id>/delete')
def delete_recipe(recipe_id):
    recipe = Recipe.get_recipe_by_id({'id': recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/dashboard')

    return render_template('confirm_delete.html', recipe = recipe)

@app.route('/recipes/<int:recipe_id>/confirm_delete')
def confirm_delete(recipe_id):
    recipe = Recipe.get_recipe_by_id({'id': recipe_id})

    if recipe.user.id != session['user_id']:
        return redirect('/dashboard')

    Recipe.delete_recipe({'id': recipe_id})

    return redirect('/dashboard')