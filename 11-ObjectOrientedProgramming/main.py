from ebook import Ebook 

def main():
    my_book = Ebook('The Winners Crime', 'Marie Rutkoski', 402)
    my_book.show_status()
    my_book.open_book()
    my_book.next_page()
    my_book.next_page()
    my_book.show_status()
    my_book.previous_page()
    my_book.show_status()
    my_book.close_book()
    my_book.next_page()

if __name__ =='__main__':
    main()