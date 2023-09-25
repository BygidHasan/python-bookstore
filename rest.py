from db import books

def create_book(title, author, genre):
    book = {
        "title" : title,
        "author": author,
        "genre" : genre
    }
    post = books.insert_one(book)
    print(f"book with id: {post.inserted_id} is successfull")

def find_book(title):
    book = books.find_one({"title": title})
    if book:
        print(book)
    else:
        print("book not found")

def update_book(title, new_data):
    new_info = books.update_one({"title": title}, {"$set": new_data})

    if new_info.modified_count > 0:
        print(f"book {title} updated")
    else:
        print(f"book {title} not found")

def delete_book(title):
    deleted = books.delete_one({"title": title})

    if deleted.deleted_count > 0:
        print(f"book {deleted} has been removed")
    else:
        print("book not found")

def list_books():
    allbooks = books.find()
    print("books info's available in this bookstore:\n")
    
    for book in allbooks:
        print(book)

