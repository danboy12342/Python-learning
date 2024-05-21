def load_write(text,enter):
    file = open(text,"w")
    file.write(enter)
    file.close

def file_select():    
    print("To Begin The Program Please")
    print("Enter file name")
    text = str(input())
    text = text+str(".txt")
    enter = str(input("Enter what you want to input into the file"))
    return text,enter


text,enter = file_select()

load_write(text,enter)

