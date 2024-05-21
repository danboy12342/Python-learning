def initialise():
    plant=[None]*200
    num=[None]*200
    return plant,num
    
def load_read(text,plant,num):
    file = open(text,"r")
    line = file.readline().rstrip('\n')
    counter=0
    while line:
            items = line.split(",")
            plant[counter] = (items[0])
            num[counter] = (items[1])
            line = file.readline().rstrip("\n")
            counter = counter+1
    file.close()
    return plant , num
    

def searchfile(names):
    searchitems = input("Please enter the items to be searched for: ")

    for x in range(len(names)):
        if names[x] == searchitems:
            print("items found in aisle : " + str(x+1))
            
plant,num = initialise()
items,prices = load_read("PlantStockfile.csv",plant,num)
searchfile(items)
            
