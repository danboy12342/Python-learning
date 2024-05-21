#Reading and writing to a file
def load_print(text):

    names = [""]*20
    house = [""]*20
    counter = 0

    
    file = open(text,"r")
    
    line = file.readline().rstrip('\n')
    while line:
            items = line.split(",")
            names[counter] = (items[0])
            house[counter] = (items[1])
            line = file.readline().rstrip("\n")
            counter = counter+1
    file.close()
    return names , house
   

    
print("To Begin The Program Please")
print("Enter A Full file name Inc .txt")
text = str(input())

text = text+str(".txt")


array1,array2 = load_print(text)
for counter in range(0,10):
    print(array1[counter],array2[counter])


