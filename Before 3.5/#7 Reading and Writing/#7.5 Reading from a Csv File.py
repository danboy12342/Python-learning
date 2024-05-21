def inputs
    pupils = 
def load_read(text):
    file = open(text,"r")
    line = file.readline()
    print(line)

    
    
def file_select():    
    print("To Begin The Program Please")
    print("Enter A Full file name ")
    text = str(input())
    text = text+str(".csv")
    return text


text = file_select()
load_read(text)
