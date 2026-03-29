# Practical 09, Lab Assignment 2
# Library management system with Book, Member, and Library classes.

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available Copies: {self.available_copies}/{self.total_copies}")
        print('-' * 30)


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def display(self):
        print(f"Member Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Borrowed Books: {self.borrowed_books}")
        print('-' * 30)


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added to library.")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member '{member.name}' added to system.")

    def display_books(self):
        print('\nLibrary Books:')
        for book in self.books.values():
            book.display()

    def lend_book(self, isbn, member_id):
        if isbn not in self.books:
            print('Book not found.')
            return
        if member_id not in self.members:
            print('Member not found.')
            return
        book = self.books[isbn]
        member = self.members[member_id]
        if book.available_copies < 1:
            print('No copies are currently available.')
            return
        book.available_copies -= 1
        member.borrowed_books.append(book.title)
        print(f"Book '{book.title}' lent to {member.name}.")

    def return_book(self, isbn, member_id):
        if isbn not in self.books:
            print('Book not found.')
            return
        if member_id not in self.members:
            print('Member not found.')
            return
        book = self.books[isbn]
        member = self.members[member_id]
        if book.title not in member.borrowed_books:
            print('This member did not borrow that book.')
            return
        book.available_copies += 1
        member.borrowed_books.remove(book.title)
        print(f"Book '{book.title}' returned by {member.name}.")


def main():
    library = Library()

    while True:
        print('\nLibrary Menu:')
        print('1. Add a Book')
        print('2. Add a Member')
        print('3. Lend a Book')
        print('4. Return a Book')
        print('5. Display Books')
        print('6. Display Members')
        print('7. Exit')
        choice = input('Choose an option: ').strip()

        if choice == '1':
            title = input('Book title: ').strip()
            author = input('Author: ').strip()
            isbn = input('ISBN: ').strip()
            copies = int(input('Number of copies: ').strip())
            library.add_book(Book(title, author, isbn, copies))
        elif choice == '2':
            name = input('Member name: ').strip()
            member_id = input('Member ID: ').strip()
            library.add_member(Member(name, member_id))
        elif choice == '3':
            isbn = input('ISBN to lend: ').strip()
            member_id = input('Member ID: ').strip()
            library.lend_book(isbn, member_id)
        elif choice == '4':
            isbn = input('ISBN to return: ').strip()
            member_id = input('Member ID: ').strip()
            library.return_book(isbn, member_id)
        elif choice == '5':
            library.display_books()
        elif choice == '6':
            print('\nLibrary Members:')
            for member in library.members.values():
                member.display()
        elif choice == '7':
            print('Exiting library system.')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == '__main__':
    main()
