from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()
a=bcrypt.generate_password_hash('testing')
print(a)
hashed_password=a.decode('utf-8')
print(hashed_password)
print(bcrypt.check_password_hash(hashed_password,'testing'))

from OFSConnect.models import User
users=User.query.all()
print(users)

for user in users :
    print(user.password)