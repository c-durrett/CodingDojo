from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.user import User

class Car():
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.user = None

    @classmethod
    def create_car(cls, data):
        query = 'INSERT INTO cars (price, model, make, year, description, users_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(users_id)s);'

        result = MySQLConnection('car_dealz_schema').query_db(query, data)

        return result

    @classmethod
    def get_all_cars(cls):

        query = 'SELECT * FROM cars JOIN users ON cars.users_id = users.id;'

        results = MySQLConnection('car_dealz_schema').query_db(query)

        cars = []

        for item in results:
            car = Car(item)
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
            car.user = user
            cars.append(car)

        return cars

    @classmethod
    def get_car_by_id(cls, data):

        query = 'SELECT * FROM cars JOIN users ON cars.users_id = users.id WHERE cars.id = %(id)s;'

        result = MySQLConnection('car_dealz_schema').query_db(query, data)

        car = Car(result[0])
        user_data = {
            'id': result[0]['users_id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password': result[0]['password'],
            'created_at': result[0]['users.created_at'],
            'updated_at': result[0]['users.updated_at']
        }
        car.user = User(user_data)

        return car

    @classmethod
    def update_car(cls, data):

        query = 'UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE id = %(id)s;'

        MySQLConnection('car_dealz_schema').query_db(query, data)

    @classmethod
    def delete_car(cls, data):
        
        query = 'DELETE FROM cars WHERE id = %(id)s;'

        return MySQLConnection('car_dealz_schema').query_db(query, data)

    @staticmethod
    def car_validator(data):
        is_valid = True

        if len(data['price']) < 1:
            flash("Price must be greater than 0")
            is_valid = False

        if len(data['model']) < 3 or len(data['model']) > 45:
            flash("Model should be 3 to 45 characters")
            is_valid = False

        if len(data['make']) < 3 or len(data['make']) > 45:
            flash("Make should be 3 to 45 characters")
            is_valid = False

        if len(data['year']) < 4 or len(data['year']) > 4:
            flash("Year must be a four digit value 'yyyy'.")
            is_valid = False

        if len(data['year']) < 1:
            flash("Year must be greater than 0.")

        if len(data['description']) < 3 or len(data['description']) > 1000:
            flash("Car description should be 3 to 1000 characters")
            is_valid = False

        return is_valid