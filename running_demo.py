# from demo import db, User, Post
from OFSConnect import db
from OFSConnect.models import User, Post

db.create_all()
user1=User(username='admin',email='admin@gmail',password='admin')
db.session.add(user1)

user2=User(username='milind',email='milind@gmail',password='milind')
db.session.add(user2)

db.session.commit()

print(User.query.all())

post1=Post(title='First Title',content='my first content',author=user2)
post2=Post(title='second Title',content='my second content',author=user2)

db.session.add(post1)
db.session.add(post2)
db.session.commit()

for post in user2.posts:
    print(post)