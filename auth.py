import hashlib
import os
from db import users

def hash_password(password):
    return password

def login(username, password):
    user = users.find_one({"username": username})
    
    if user and user["password"] == hash_password(password):
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

