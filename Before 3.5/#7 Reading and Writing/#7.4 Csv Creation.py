
def load_write(text,enter):
    file = open(text,"w")
    file.write(enter)
    file.close

def load_read(text):
    file = open(text,"r")
    smt = file.readline()
    print(smt)

    
    
def file_select():    
    print("To Begin The Program Please")
    print("Enter A Full file name Inc .txt")
    text = str(input())
    text = text+str(".csv")
    enter = str(input("Enter what you want to input into the file"))
    return text,enter


text,enter = file_select()

load_write(text,enter)
load_read(text)
