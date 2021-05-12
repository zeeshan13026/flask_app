from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item_model import ItemModel


# items =[]
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        required=True,
                        type=float,
                        help='This field can\'t be blank')

    parser.add_argument('store_id',
                        required=True,
                        type=int,
                        help='Every item needs a store id')

    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item

        '''Now fetch data from database'''
        # item = next(filter(lambda x: x['name'] == name,items),None) # next will return the first matched item
        # return {'item': item}, 200 if item is not None else 404
        '''Now we have a method find_item_by_name()'''
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items WHERE name = ?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()
        #
        # if row:
        #     return {'item':{'name' : row[0], 'price' : row[1]}},200

        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 400

    '''Moved to item_model.py'''

    # @classmethod
    # def find_item_by_name(cls,name):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     query = "SELECT * FROM items WHERE name = ?"
    #     result = cursor.execute(query, (name,))
    #     row = result.fetchone()
    #
    #     if row:
    #         return {'item': {'name': row[0], 'price': row[1]}}, 200

    def post(self, name):
        # if next(filter(lambda x:x['name']==name, items),None) is not None:
        #     return {'message' : "An item with name {} already exist, Please try with different name.".format(name)},400

        if ItemModel.find_item_by_name(name):
            return {'message': "An item with name {} already exist, Please try with different name.".format(name)}, 400

        data = Item.parser.parse_args()
        # data = request.get_json()

        # item = {
        #     "name" : name,
        #     "price" : data['price']
        # }

        # item = ItemModel(name, data['price'],data['store_id'])
        item = ItemModel(name, **data)

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES(?,?)"
        # cursor.execute(query,(item['name'],item['price']))
        #
        # connection.commit()
        # connection.close()
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500
        # items.append(item)
        return item.json(), 201

    '''Moved to item_model.py'''

    # @classmethod
    # def insert(cls,item):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     query = "INSERT INTO items VALUES(?,?)"
    #     cursor.execute(query, (item['name'], item['price']))
    #
    #     connection.commit()
    #     connection.close()

    def delete(self, name):
        '''Now we user DB instead of list'''
        # global items
        # items = list(filter(lambda x:x['name']!=name,items))
        # return {'message' : 'Item deleted'}

        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}, 200

        '''Now we use item_model to delete'''
        # if ItemModel.find_item_by_name(name) is None:
        #     return {'message': "An item with name {} is not exist, Please try with different name.".format(name)}, 400
        #
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "DELETE FROM items where name = ?"
        #
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()
        # return {'message' : 'Item deleted'},200

        '''Another way to delete item with error handling'''
        # item = next(filter(lambda x:x['name'] == name,items),None)
        # if item:
        #     items.remove(item)
        #     return {'message': 'Item deleted'}, 200
        # return {'message': 'Item Not found'},404

    def put(self, name):
        # item = next(filter(lambda x:x['name']==name,items),None)

        data = Item.parser.parse_args()
        # data = request.get_json()

        item = ItemModel.find_item_by_name(name)
        # updated_item = ItemModel(name,data['price'])
        # updated_item = {
        #     'name': name,
        #     'price': data['price']
        # }

        if item is None:
            item = ItemModel(name, data['price'],data['store_id'])
            # try:
            #     #items.append(item)
            #     # ItemModel.insert(updated_item)
            #     updated_item.insert()
            #     # return item
            # except:
            #     return {'message' : 'An error occurred inserting the item'},500
        else:
            item.price = data['price']
            # try:
            #     # item.update(data)
            #     # ItemModel.update(updated_item)
            #     updated_item.update()
            # except:
            #     return {'message' : 'An error occurred updating the item'},500
        item.save_to_db()
        return item.json()
        # return updated_item.json()

    # @classmethod
    # def update(cls,item):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "UPDATE items SET price = ? WHERE name= ?"
    #
    #     cursor.execute(query, (item['price'],item['name']))
    #     connection.commit()
    #     connection.close()
    #
    #     # '''Another way of updating item'''
    #     # global items
    #     # items = list(filter(lambda x:x['name']!=name,items))
    #     # data = request.get_json()
    #     # item = {
    #     #         "name" : name,
    #     #         "price" : data['price']
    #     #     }
    #     # items.append(item)
    #     # return {'item' : item},200


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}  # it is another way

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})
        # connection.close()
        # return {'items':items},200
        # # return {"items":items},200
