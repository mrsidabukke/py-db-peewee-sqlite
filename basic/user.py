import random , datetime
from peewee import *

sqlite_db = SqliteDatabase('user.db')

# Create a User model
class User(Model):
    name = CharField()
    email = CharField()
  

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([User], safe=True)# safe=True will not throw an error if the table already exists


#inserting data
#User.create(name='John Doe',email="lamhot@gmail.com")

#User.insert(name='John Doe2',email="lamhot2@gmail.com").execute()

# user = User(name='John Doe3',email="lamhot3@gmail.com")
# user.save()

# dont forget to add .execute() if you are using insert method
# .save && .execute method will return the id of the inserted data

# inserting multiple data
# users = [
#         {'name':'John Doe4','email':'lamhot4@gmail.com'},
#          {'name':'John Doe5','email':'lamhot5@gmail.com'},
# ]

# User.insert_many(users).execute()

#with this method below you can specify the fields that you want to insert
# fields = [User.name, User.email]

# data = {
#     ('sudung','sudung@gmail.com'),
#     ('sudung2','sudung2@gmail.com')
# }

# User.insert_many(data, fields=fields).execute()


# #selecting data
# user1 = User.get(User.id == 1)
# print(user1.name)

# uset = User[3]
# print(uset.name)

#selecting many data
# to transorm it into dictionary just add .dicts()
# query = User.select()
# for user in query:
#     print(user.name)

# #filtering data
# users = User.select().where((User.name == 'John Doe') | (User.name == 'sudung'))
# for user in users:
#     print(user.name)

# users = User.select().where(User.name.contains('John'))
# for user in users:
#     print(user.name)
