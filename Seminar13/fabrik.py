import json
from main import User
from exception import LevelException, AccessException


class UserWorkShop:
    user_list = set()

    def __init__(self):
        UserWorkShop.load_users()
        pass

    @staticmethod
    def load_users(path: str = 'index.json'):
        with open(path, 'r' , encoding = 'UTF-8') as file:
            user_dict = json.load(file)
        for level, user_list in user_dict.items():
            for uid, name in user_list.items():
                UserWorkShop.user_list.add(User(name, uid, level))

    def login(self, name: str, uid: str):
        login_user = User(name, uid)
        for user in UserWorkShop.user_list:
            if login_user == user:
                return user.level
        else:
            raise AccessException(name)
    
    def create(self, name: str, uid: str, level: str):
        cur_name, cur_uid = input("Введите имя и ID через пробел: ").split()
        if current_level := self.login(cur_name, cur_uid):
            if int(current_level) > int(level):
                return User(name, uid, level)
            else:
                raise LevelException(current_level, level)

baza = UserWorkShop()

print(baza.login('User_04', '456'))
print(baza.create('STONE', '17', 3))