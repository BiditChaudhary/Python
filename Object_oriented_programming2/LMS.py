class Library:

    def __init__(self,booklist):
        self.booklist = booklist
    
    def display_books(self):
        print("booklist")

        for i in self.booklist:
            print(i)
        
    def add_books(self,booklist):
        self.booklist = booklist

booklist = ["Stig of the Dump","Charlie and the chocolate factory","Genesis","Munamadan"]
l1 = Library(booklist)
while True:
    print("1. Add books \n2. Display books \n3. Lend books \n 4. Return Books")

    ch = input("Enter your choice: ")
    if ch == "1":
        New_book = input("Enter the name of the new book: ")
        booklist.append(New_book)
        l1.add_books(booklist)
        print("Book added")

    elif ch == "2":
        l1.display_books()

    else:
        break



