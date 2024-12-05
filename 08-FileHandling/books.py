import csv

def read_books_from_csv(file_name):
    books=[]
    with open(file_name,mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

def write_books_to_file(books,file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for book in books:
            file.write(f'{book['Title']} by {book['Author']} \n')
    
def main():
    genre_to_file={
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'book_romance.txt',
        'Classic': 'books_classics.txt'
    }

    books=read_books_from_csv('books.csv')

    for genre, file_name in genre_to_file.items():
        filtered_books=[]

        for book in books:
            if book['Genre'].lower()==genre.lower():
                filtered_books.append(book)

        write_books_to_file(filtered_books, file_name)
        print(f"copied {len(filtered_books)} books of genre '{genre}' to '{file_name}'.")

if __name__ == "__main__":
    main()