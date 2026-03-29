# Practical 10, Lab Assignment 1
# Read books.csv and perform requested DataFrame operations.

import os

try:
    import pandas as pd
except ImportError:
    print('Pandas is required for this script. Install it with pip install pandas.')
    raise


SAMPLE_BOOKS = [
    {'title': 'Python Basics', 'author': 'John Bale', 'edition': '1st', 'publication_year': 2020, 'publishing_house': 'Tech Press', 'price': 450},
    {'title': 'Data Science', 'author': 'Anna Ray', 'edition': '2nd', 'publication_year': 2021, 'publishing_house': 'Data House', 'price': 530},
    {'title': 'Machine Learning', 'author': 'John Bale', 'edition': '3rd', 'publication_year': 2019, 'publishing_house': 'ML World', 'price': 625},
    {'title': 'Deep Learning', 'author': 'Steve Kim', 'edition': '1st', 'publication_year': 2022, 'publishing_house': 'Tech Press', 'price': 780},
]


def load_books(file_path):
    if file_path and os.path.isfile(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame(SAMPLE_BOOKS)


def main():
    file_path = input('Enter the path to books.csv (leave blank to use sample data): ').strip()
    books = load_books(file_path)

    print('\nComplete report of books:')
    print(books.to_string(index=False))

    author = input('\nEnter author name to filter books: ').strip()
    if author:
        result = books[books['author'].str.contains(author, case=False, na=False)]
        print(f"\nBooks by '{author}':")
        print(result.to_string(index=False) if not result.empty else 'No books found for that author.')

    publisher = input('\nEnter publishing house to filter books: ').strip()
    if publisher:
        result = books[books['publishing_house'].str.contains(publisher, case=False, na=False)]
        print(f"\nBooks from '{publisher}':")
        print(result.to_string(index=False) if not result.empty else 'No books found for that publishing house.')

    if 'price' in books.columns:
        cheapest = books.loc[books['price'].idxmin()]
        costliest = books.loc[books['price'].idxmax()]
        print(f"\nCheapest book: {cheapest['title']} at price {cheapest['price']}")
        print(f"Costliest book: {costliest['title']} at price {costliest['price']}")

    if 'publication_year' in books.columns:
        sorted_books = books.sort_values(by='publication_year')
        print('\nBooks sorted by year of publication:')
        print(sorted_books.to_string(index=False))


if __name__ == '__main__':
    main()
