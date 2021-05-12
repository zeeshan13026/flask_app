import sqlite3
from flask_restful import Resource, reqparse
from models.user_model import UserModel


'''Moved this class to user_model.py'''
# class User:
#     def __init__(self, _id, username, password):
#         self.id = _id
#         self.username = username
#         self.password = password
#
#     @classmethod
#     def find_user_by_username(cls, username):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         query = "SELECT * FROM user WHERE username= ?"
#         result = cursor.execute(query, (username,))
#         row = result.fetchone()
#         if row:
#             user = cls(*row)
#         else:
#             user = None
#         connection.close()
#         return user
#
#     @classmethod
#     def find_user_by_id(cls, _id):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         query = "SELECT * FROM user WHERE id = ?"
#         result = cursor.execute(query, (_id,))
#         row = result.fetchone()
#
#         if row:
#             user = cls(*row)
#         else:
#             user = None
#         return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field can\'t be blank'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field can\'t be blank'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_user_by_username(data['username']):
            return {'message': 'User already exist'}, 400

        # UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully'}, 200
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO user VALUES(NULL,?,?)"
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()
        # return {'message': 'User created successfully'}, 200



