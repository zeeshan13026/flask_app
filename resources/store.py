from flask_restful import Resource
from models.stores_model import StoreModel

class Store(Resource):

    def get(self,name):
        store = StoreModel.find_item_by_name(name=name)
        if store :
            return store.json()
        else:
            return {'message' : 'Store not found'},404

    def post(self,name):
        if StoreModel.find_item_by_name(name=name):
            return {'message':'Store with the name {} is already exist'.format(name)}

        store = StoreModel(name)
        try :
            store.save_to_db()
        except:
            return {'message':'An error occurred while adding store into DB'},400
        return store.json()

    def delete(self,name):
        store = StoreModel.find_item_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):

    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}
        # return {'stores': list(map(lambda store:store.json(),StoreModel.query.all()))}