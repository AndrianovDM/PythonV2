import json

class User:
    def __init__(self, name: str, user_id: int, level = 0):
        self.name = name
        self.user_id = user_id
        self.level = level
    
    def __str__(self):
        return f'!!UID: {self.user_id}, Name: {self.name}, level: {self.level} !!'
    
    def __repr__(self):
        return f'!!UID: {self.user_id}, Name: {self.name}, level: {self.level} !!'

    def __hash__(self):
        return hash(self.name) + hash(self.user_id)
    
    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

work_group = set()

def load_user(path: str = 'index.json'):
    with open(path, 'r' , encoding = 'UTF-8') as file:
        user_dict = json.load(file)
    for level, user_list in user_dict.items():
        for uid, name in user_list.items():
            work_group.add(User(name, uid, level))

load_user()
print(work_group)
