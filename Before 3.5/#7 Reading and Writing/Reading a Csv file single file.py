#Reading a file (Single line)
#3.4
#17/08/2023

def readfile(filename):
    namesarray = [None] * 100
    datesarray = [None] * 100
    ticketsarray = [None] * 100
    pricearray = [None] * 100
    counter = 0

    with open(filename) as readfile:
        line = readfile.readline().rstrip('\n')
        items = line.split(",")
        for purchasecounter in range(0,len(items),4):
            namesarray[counter] = items[purchasecounter]
            datesarray[counter] = items[purchasecounter+1]
            ticketsarray[counter] = items[purchasecounter+2]
            pricearray[counter] = items[purchasecounter+3]
            counter += 1
    return namesarray,datesarray,ticketsarray,pricearray

def display(namesarray,datesarray,ticketsarray,pricearray):
    for counter in range(0,100):
        print("{0:<25}".format(namesarray[counter]),"{0:<15}".format(datesarray[counter]),"{0:<6}".format(ticketsarray[counter]),"{0:<10}".format(pricearray[counter]))
  

x,y,z,a = readfile("sales.csv")
display(x,y,z,a)
    
