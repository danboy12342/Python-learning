#Reading a .txt file and splitting a comma from it 
#Task 3.2
#Peter Acton


def load_print(text):
    names = [""]*20
    house = [""]*20
    counter = 0

    #Read the first line of the file
    file = open(text,"r")
    #While this line of code contains any chararcters (file isnt empty)
    line = file.readline().rstrip('\n')
    while line:
        #split the line on the comma (and store in an array)
        #Each parar of the array contains the parts between the commas
            items = line.split(",")
            names[counter] = (items[0])
            house[counter] = (items[1])
            line = file.readline().rstrip("/n")
            counter = counter+1
    file.close()
    return names , house



    
#File Selector    
def file_select():    
    print("To Begin The Program Please")
    print("Enter a CSV file name")
    text = str(input())
    text = text+str(".csv")
    return text


text = file_select()



array1,array2 = load_print(text)
print("{0:<10}".format("Names"),"{0:<10}".format("House"))
print()
for counter in range(0,20):
    print("{0:<10}".format(array1[counter]),"{0:<10}".format(array2[counter]))


