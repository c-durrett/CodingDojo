from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.user import User
class Recipe():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_thirty_minutes = data['under_thirty_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.user = None

    @classmethod
    def create_recipe(cls, data):
        query = 'INSERT INTO recipes (name, description, instructions, date, under_thirty_minutes, users_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_thirty_minutes)s, %(users_id)s);'

        result = MySQLConnection('recipes_schema').query_db(query, data)

        # result is the ID of what's created
        return result

    @classmethod
    def get_all_recipes(cls):

        query = 'SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;'

        results = MySQLConnection('recipes_schema').query_db(query)

        recipes = []

        for item in results:
            recipe = Recipe(item)
            user_data = {
                'id': item['users_id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']
            }
            user = User(user_data)
            recipe.user = user
            recipes.append(recipe)

        return recipes

    @classmethod
    def get_recipe_by_id(cls, data):

        query = 'SELECT * FROM recipes JOIN users ON recipes.users_id = users.id WHERE recipes.id = %(id)s;'

        result = MySQLConnection('recipes_schema').query_db(query, data)

        recipe = Recipe(result[0])
        user_data = {
                'id': result[0]['users_id'],
                'first_name': result[0]['first_name'],
                'last_name': result[0]['last_name'],
                'email': result[0]['email'],
                'password': result[0]['password'],
                'created_at': result[0]['users.created_at'],
                'updated_at': result[0]['users.updated_at']
            }
        recipe.user = User(user_data)

        return recipe

    @classmethod
    def update_recipe(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_thirty_minutes = %(under_thirty_minutes)s WHERE id = %(id)s;'

        MySQLConnection('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        MySQLConnection('recipes_schema').query_db(query, data)


    @staticmethod
    def recipe_validator(data):
        is_valid = True

        if len(data['name']) < 3 or len(data['name']) > 100:
            flash("Recipe name should be 3 to 100 characters")
            is_valid = False

        if len(data['date']) != 10:
            flash("Please provide a valid date")
            is_valid = False

        if len(data['description']) < 3 or len(data['description']) > 1000:
            flash("Recipe description should be 3 to 1000 characters")
            is_valid = False

        if len(data['instructions']) < 3 or len(data['instructions']) > 10000:
            flash("Recipe instructions should be 3 to 10,000 characters")
            is_valid = False

        return is_valid