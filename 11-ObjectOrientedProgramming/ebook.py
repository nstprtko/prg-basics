class Ebook:
    def __init__(self, title,author,number_pages):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        self.current_page = 0
        self.is_open = False

    def open_book(self):
        if not self.is_open:
            self.is_open = True
            self.current_page = 1
            print(f'The book {self.title} by {self.author} is open on page {self.current_page}')

        else:
            print(f'{self.title} is already open')

    def close_book(self):
        if self.is_open:
            self.is_open = False
            self.current_page = 0
            print(f'The book {self.title} is now closed')

        else:
            print('The book is already closed ')

    def next_page(self):
        if self.is_open:
            if self.current_page < self.number_pages:
                self.current_page +=1
                print(f'Current page is {self.current_page}')
            else :
                print(f'youve reached the final page {self.number_pages}')
        else:
            print('the book is closed')

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -=1
                print(f'Turned to page {self.current_page}')
            else:
                print("there's nowhere to turn back")
        else:
            print('book is closed')
            
    def show_status(self):
        if self.is_open:
            status = 'open'
        else:
            status = 'closed'
             
        current_page_info = f'Currently on page {self.current_page}' if self.is_open else "Not reading"
        print(f'Book status : \n'
                f'Title : {self.title}\n'
                f'Author : {self.author}\n'
                f'Total Pages : {self.number_pages}\n'
                f'Status : {status}\n'
                f'{current_page_info}')