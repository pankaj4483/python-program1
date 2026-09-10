class book:
    def __init__(self,tittle,author):
        self.tittle=tittle
        self.author=author
        self.is_available=True

    def show_info(self):
        status="available" if self.is_available else"borrowed"
        print(f"{self.tittle} by {self.author} - {status}")

class library:
    def __init__ (self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.tittle} added to library.")

    def show_all_books(self):
        print("\n---all books---")
        for book in self.books:
            book.show_info()

    def borrow_book(self,tittle):
        for book in self.books:
            if book.tittle==tittle:
                if book.is_available:
                    book.is_available=False
                    print(f"you borrowedd: {tittle}")
                    return
                else:
                    print(f"{tittle} is already borrowed.")
                    return
        print(f"{tittle} not found in library.")
#---main code---
lib=library()

book1=book("python basic","john doe")
book2=book("IOT for beginners", "jane smith")

lib.add_book(book1)
lib.add_book(book2)

lib.show_all_books()

print()
lib.borrow_book("python basic")
lib.borrow_book("python basic")#already borrowed test 
lib.borrow_book("unknown book")#not found test

print()
lib.show_all_books()
