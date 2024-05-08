import random , datetime
from peewee import *

sqlite_db = SqliteDatabase('admin.db')

# Create a User model
class Admin(Model):
    # name = CharField()
    # email = CharField()
    username = CharField()
    point = IntegerField()
    join_at = DateTimeField(default=datetime.datetime.now)


    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([Admin], safe=True)# safe=True will not throw an error if the table already exists
# asc && desc
# if you dont use desc() it will be asc by default
# admin = Admin.select().order_by(Admin.point.desc())
# for ad in admin:
#     print(ad.username,ad.point)

# update data
# admin = Admin.select().where(Admin.username == 'alex').get()
# admin.username = 'alex sandro'
# admin.save()

# Admin.update(point=1000).where(Admin.username == 'alex sandro').execute()

# delete data
# admin = Admin.get(Admin.id == 4)
# admin.delete_instance()

# Admin.delete().where(Admin.point < 1000).execute()

# limit data
# count is used to count the data
# print(Admin.select().count())
# admin = Admin.select().limit(2)
# for ad in admin:
#     print(ad.username)

# admins = Admin.select().paginate(1,2)
# for ad in admins:
#     print(ad.username)



# def get_rand():
#     return random.randint(1,1000)

# data = [
#     {'username':'jean','point':get_rand()},
#     {'username':'keqing','point':get_rand()},
    
#     {'username':'mona','point':get_rand()}
# ]

# Admin.insert_many(data).execute()


