def initialise():
    plant=[None]*200
    num=[None]*200
    return plant,num
    
def load_read(text,plant,num):
    file = open(text,"r")
    line = file.readline().rstrip('\n')
    counter = 0
    while line:
            items = line.split(",")
            plant[counter] = (items[0])
            num[counter] = (items[1])
            line = file.readline().rstrip("\n")
            counter = counter+1
    file.close()
    return plant , num
    

def searchfile(names):
    counter = 0
    found = False
    searchitem = input("Please enter the items to be searched for: ")
    #loop through the entire array
    while(counter <len(names) and found == False):
        if names[counter] == searchitem:
            found = True
            foundpostion = counter
        else:
            print("item has not been found")
            sleep()
        counter += 1
    print("item found in aisle : " ,foundpostion+1)
            
plant,num = initialise()
items,prices = load_read("PlantStockfile.csv",plant,num)
searchfile(items)
            
