#5.1
#ISBN Version 1

class Book():
    def __init__(self):
        self.titles = ""
        self.author = ""
        self.ISBN = ""
        self.price = 0.0
    

def Readbooks():
    Books = [Book() for x in range(20)]
    counter=0

    readfile = open("books.txt","r")
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        Books[counter].titles = items[0]
        Books[counter].authors = items[1]
        Books[counter].ISBN = items[2]
        Books[counter].prices = items[3]
        line = readfile.readline().rstrip('\n')
        counter += 1
    input("File Read... Press any key to continue")
    return Books

def Searchbooks(books):
    found = False
    choice = input("Please enter the ISBN to search for: ")
    for counter in range(0,len(books)):
        if books[counter].ISBN == choice:
            found = True
            position = counter
    if found == False:
        print("No book found in the list")
    else:
        print("Book found: ")
        print("Title: ",books[position].titles)
        print("Author: ",books[position].authors)
        print("Price: ",books[position].prices)

books=Readbooks()
Searchbooks(books)


        
