#4.5
names = [None]*50
genders = [None]*50
trips = [None]*50
counter = 0


def LoadOpen():
    file = open("schooltrips.csv","r")
    line = file.readline().rstrip('\n')
    for counter in range(0,len(names)):
            items = line.split(",")
            names[counter] = items[0]
            genders[counter] = items[1]
            trips[counter] = items[2]
            line = file.readline().rstrip("\n")
                  
    file.close()
    return names,genders,trips

def LoadCreate(names,genders,trips):
    londoncounter=0
    pariscounter=0
    gorgecounter=0
    mountaincounter=0
    for counter in range(0,len(trips)):
        if trips[counter] == "London":
            londoncounter=londoncounter+1
        elif trips[counter] == "Paris":
            pariscounter=pariscounter+1
        elif trips[counter] == "Mountain Biking":
            mountaincounter=mountaincounter+1  
        elif trips[counter] == "Gorge Walking":
            gorgecounter=gorgecounter+1
    london=[None]*londoncounter
    paris=[None]*pariscounter
    mountain=[None]*mountaincounter
    gorge=[None]*gorgecounter
    londoncounter=0
    pariscounter=0
    gorgecounter=0
    mountaincounter=0
    for counter in range(0,50):
        if trips[counter] == "London":
            london[londoncounter] = str(names[londoncounter])
            londoncounter=londoncounter+1
        elif trips[counter] == "Paris":
            paris[pariscounter] = str(names[pariscounter])
            pariscounter=pariscounter+1
        elif trips[counter] == "Mountain Biking":
            mountain[gorgecounter] = str(names[gorgecounter])
            gorgecounter=gorgecounter+1
        elif trips[counter] == "Gorge Walking":
            gorge[mountaincounter] = str(names[mountaincounter])
            mountaincounter=mountaincounter+1


            
    file = open("paris.csv","w")
    for counter in range(0,len(paris)):
        file.write(str(paris[counter]))
        file.write("\n")
    file.close
    
    file = open("london.csv","w")
    for counter in range(0,len(london)):
        file.write(str(london[counter]))
        file.write("\n")
    file.close
    file = open("gorge.csv","w")
    for counter in range(0,len(gorge)):
        file.write(str(gorge[counter]))
        file.write("\n")
    file.close
    file = open("mountain.csv","w")
    for counter in range(0,len(mountain)):
        file.write(str(mountain[counter]))
        file.write("\n")
    file.close
def LoadPrint(names,genders,trips):
    for counter in range(0,len(names)):
        print(names[counter],gender[counter],trips[counter])
    print()



names,gender,trips = LoadOpen()
LoadPrint(names,gender,trips)
LoadCreate(names,gender,trips)



