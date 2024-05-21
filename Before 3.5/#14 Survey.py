#Survey

def load_read(text,write):
    file = open(text,"w")
    file.write(write)
    file.close
    file = open(text,"r")
    line = file.readline()
    print(line)
    file.close
    

    
    
def file_select():    
    print("To Begin The Program Please")
    print("Enter A Full file name ")
    text = str(input())
    text = text+str(".txt")
    write = input("Enter the table")
    return text,write


text,write = file_select()
load_read(text,write)
