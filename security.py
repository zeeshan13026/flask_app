from werkzeug.security import safe_str_cmp
from resources.user import UserModel

# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# ]

'''Not need now we are creating users in db using test.py'''
# users = [
#     User(1,'bob','asdf')
# ]

# username_mapping = {
#     'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }

'''Not need now we are creating users in db using test.py'''
# username_mapping = {u.username : u for u in users}

# userid_mapping = {
#     1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }

'''Not need now we are creating users in db using test.py'''
# userid_mapping = {u.id : u for u in users}

def authenticate(username,password):
    # user = username_mapping.get(username,None)
    user = UserModel.find_user_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_user_by_id(user_id)
    # return userid_mapping.get(user_id,None)