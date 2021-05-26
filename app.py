import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList

from db import db

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    # from db import db
    # db.init_app(app)
    app.run(port=5000, debug=True)
# items =[]
#
# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#                         required=True,
#                         type=float,
#                         help='This field can\'t be blank')
#
#     @jwt_required()
#     def get(self,name):
#         # for item in items:
#         #     if item['name'] == name:
#         #         return item
#         item = next(filter(lambda x: x['name'] == name,items),None) # next will return the first matched item
#         return {'item': item}, 200 if item is not None else 404
#
#     def post(self,name):
#         if next(filter(lambda x:x['name']==name, items),None) is not None:
#             return {'message' : "An item with name {} already exist, Please try with different name.".format(name)},400
#
#         data = Item.parser.parse_args()
#         #data = request.get_json()
#         item = {
#             "name" : name,
#             "price" : data['price']
#         }
#         items.append(item)
#         return item,201
#
#     def delete(self,name):
#         global items
#         items = list(filter(lambda x:x['name']!=name,items))
#         return {'message' : 'Item deleted'}
#
#         '''Another way to delete item with error handling'''
#         # item = next(filter(lambda x:x['name'] == name,items),None)
#         # if item:
#         #     items.remove(item)
#         #     return {'message': 'Item deleted'}, 200
#         # return {'message': 'Item Not found'},404
#
#     def put(self,name):
#         item = next(filter(lambda x:x['name']==name,items),None)
#         data = Item.parser.parse_args()
#         # data = request.get_json()
#         if item is None:
#             item = {
#                 'name' : name,
#                 'price' : data['price']
#             }
#             items.append(item)
#             return item
#         else:
#             item.update(data)
#         return item
#
#         # '''Another way of updating item'''
#         # global items
#         # items = list(filter(lambda x:x['name']!=name,items))
#         # data = request.get_json()
#         # item = {
#         #         "name" : name,
#         #         "price" : data['price']
#         #     }
#         # items.append(item)
#         # return {'item' : item},200
#
#
# class ItemList(Resource):
#     def get(self):
#         return {"items":items},200

