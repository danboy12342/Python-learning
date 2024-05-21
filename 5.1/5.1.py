#5.1
#ISBN Version 1

def Readbooks():
    titles = [None]*20
    authors = [None]*20
    ISBN = [None]*20
    prices = [None]*20
    counter = 0

    readfile = open("books.txt","r")
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        titles[counter] = items[0]
        authors[counter] = items[1]
        ISBN[counter] = items[2]
        prices[counter] = items[3]
        line = readfile.readline().rstrip('\n')
        counter += 1
    input("File Read... Press any key to continue")
    return titles,authors,ISBN,prices

def Searchbooks(titles,authors,ISBN,prices):
    found = False
    choice = input("Please enter the ISBN to search for: ")
    for counter in range(0,len(ISBN)):
        if ISBN[counter] == choice:
            found = True
            position = counter
    if found == False:
        print("No book found in the list")
    else:
        print("Book found: ")
        print("Title: ",titles[position])
        print("Author: ",authors[position])
        print("Price: ",prices[position])

titles,authors,ISBN,prices=Readbooks()
Searchbooks(titles,authors,ISBN,prices)


        
