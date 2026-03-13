class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        book_id = input("Enter book id: ")
        book = Book(title, author, book_id)
        self.books.append(book)
        print("Book added")

    def add_member(self):
        name = input("Enter member name: ")
        member_id = input("Enter member id: ")
        member = Member(name, member_id)
        self.members.append(member)
        print("Member added")

    def lend_book(self):
        book_id = input("Enter book id: ")
        member_id = input("Enter member id: ")

        for book in self.books:
            if book.book_id == book_id and book.available:
                for member in self.members:
                    if member.member_id == member_id:
                        book.available = False
                        member.borrowed.append(book)
                        print("Book lent successfully")
                        return
        print("Book not available")

    def return_book(self):
        book_id = input("Enter book id: ")

        for member in self.members:
            for book in member.borrowed:
                if book.book_id == book_id:
                    book.available = True
                    member.borrowed.remove(book)
                    print("Book returned")
                    return
        print("Book not found")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(book.title, "-", book.author, "-", book.book_id, "-", status)


lib = Library()

while True:
    print("\n1.Add Book")
    print("2.Add Member")
    print("3.Lend Book")
    print("4.Return Book")
    print("5.Display Books")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.add_member()
    elif choice == 3:
        lib.lend_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        lib.display_books()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
