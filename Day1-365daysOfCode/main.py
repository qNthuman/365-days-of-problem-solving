# Day1-365daysOfCode 
AUTHOR = "Rmj"

"""
Problem statement : Create a library with minimal functions
"""

class library:
    def __init__(self,name):
        """ library class for creating library """
        self.name = name
        self.books= {}

    def add(self,books,author):
        """Add function to add books"""
        for index,val in enumerate(books):
            print(f"[Added] Added {val} written by {author[index]} to the library. ")
            self.books.update({val:author[index]})


    def getBooks(self):
        """get books and authors from the user"""
        confirm = input("Welcome to the {self.name} \n Do you want to add books ? \n [y] To add \n [n] To cancel")
        while confirm == "y":
            book = input("Enter the book name")
            author = input(f"Enter the author name of {book}")
            self.add([book],[author])
            confirm = input("Welcome to the {self.name} \n Do you want to add books ? \n [y] To add \n [n] To cancel")





    def ls(self):
        """Function to list all the items in a library"""
        for i in self.books:
            print(i)

    def dl(self,books:str):
        """delete books from the dict
        input in the format of :

        book1/book2/book3/...bookN

        
        """
        books = books.split("/") if type(books) is str else books
 
        

        for i in books:
            if i in self.books:
                print(f"Removing ... {i}")
                self.books.pop(i)
            else:
                print(f"No {i} found in the library.")

    def delBooks(self):
        "delte files selceted by user"
        print("Selected delete files function")
        book = input("Enter the name of the book ")
        cnf = input("Delete ? [y/n]")
        if cnf.lower() == "y":
            self.dl(book)

       


if __name__ == "__main__":
    lib1= library("MyLib")
    lib1.getBooks()
    lib1.delBooks()
    print(lib1.ls())
    print(lib1.ls())

    
        
