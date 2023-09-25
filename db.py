import pymongo

client = pymongo.MongoClient('localhost', 27017)

#get database
db = client.bookstore

#make collections
books = db.books
users = db.users