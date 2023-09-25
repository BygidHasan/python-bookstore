import bcrypt
from db import users

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verifypw(input, hashed):
    return bcrypt.checkpw(input.encode('utf-8'), hashed)

def login(username, password):
    user = users.find_one({"username": username})
    
    if user and verifypw(password, user["password"]):
        return True
    else:
        return False

def signup(username, password):
    existing_user = users.find_one({"username": username})

    if existing_user:
        return False
    else:
        users.insert_one({"username": username, "password":hash_password(password)})
        return True

