import db
import auth
import rest

def storemenu():
    while True:
        print("\n")
        print("1. Create Book")
        print("2. Find Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. List Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            rest.create_book(title, author, genre)

        elif choice == "2":
            title = input("Enter book title to find: ")
            rest.find_book(title)

        elif choice == "3":
            title = input("Enter book title to update: ")
            new_title = input("Enter new title (or press Enter to keep the same): ")
            new_author = input("Enter new author (or press Enter to keep the same): ")
            new_genre = input("Enter new genre (or press Enter to keep the same): ")
            new_data = {}
            if new_title:
                new_data["title"] = new_title
            if new_author:
                new_data["author"] = new_author
            if new_genre:
                new_data["genre"] = new_genre
            rest.update_book(title, new_data)

        elif choice == "4":
            title = input("Enter book title to delete: ")
            rest.delete_book(title)

        elif choice == "5":
            rest.list_books()

        elif choice == "6":
            break

while True:
    print("________________Welcome to our bookstore________________\n")
    print("Please select all values with the corresponding number:\n")
    print("login or signup(if you have not logged in) to create/update/delete books info, guests only view books\n")
    print("1.Guest     2.Login     3.Signup")
    
    input1 = int(input())
    
    if input1 == 1:
        print("Welcome asa guest, Here are all books available:\n")
        rest.list_books()
        break

    elif input1 == 2:
        username = input("please enter username: ")
        password = input("please enter password: ")

        if auth.login(username, password):
            print(f"Welcome {username}")
            storemenu()
        else:
            print("wrong credentials. Please try again")
    
    elif input1 == 3:
        username = input("please enter new username: ")
        password = input("please enter new password: ")

        if auth.signup(username, password):
            print("Signup successfull")
            storemenu()
        else:
            print("username already exists.Use a different username")



