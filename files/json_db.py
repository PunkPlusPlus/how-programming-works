from io import TextIOWrapper
import json
import pathlib


class Database:
    path: pathlib.Path
    f: TextIOWrapper

    def __init__(self):
        self.path = pathlib.Path('json_files', 'db.txt')

    def read_all(self):
        f = open(str(path))

        raw_data = f.readline()
        f.close()

        data = json.loads(raw_data)
        return data
    
    def update_user(user: dict):
        # read file
        # decode from json to dict
        # find in data user where id == user['id']
        # replace this user to income user
        # rewrite to file
        pass
    
    def add_user(user: dict):
        f = open(str(path))

        raw_data = f.readline()
        f.close()

        data = json.loads(raw_data)
        data.append(user)
        json_data = json.dumps(data)

        f = open(str(path), 'w')
        f.write(json_data)
        f.close()





path = pathlib.Path('json_files', 'db.txt')

# unique id +
# add data +
# edit data +
# read data +
# delete data +

db = Database()

data = db.readAll()

print(data)

user = {
    "id": 3,
    "name": 'Natasha'
}

db.update_user(user)



