import datetime
from peewee import *

db = SqliteDatabase('tweet.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now) 

# show realtion data
# query = Tweet.select().join(User)
# for tweet in query:
#     print(tweet.message)

# query = Tweet.select().join(User).where(User.username == 'alex')
# for tweet in query:
#     print(tweet.message)

alexTweet = User.get(User.username == 'alex')
for tweet in alexTweet.tweets:
    print(tweet.message)

# db.create_tables([User, Tweet])

# data =(
#     ('alex',('I am alex','this is my second tweet')),
#     ('ei',('I am ei','i like alex')),
#     ('lisa',('I am lisa','this is my second tweet'))
# )

# for username, tweets in data:
#     user = User.create(username=username)
#     for tweet in tweets:
#             Tweet.create(user=user, message=tweet)