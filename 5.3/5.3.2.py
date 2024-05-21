class secondary():
    def __init__(self):
        self.name = ""
        self.score = ""
        self.school = ""
        self.type = "Secondary"

        
class primary ():
    def __init__(self):
        self.name = ""
        self.score = ""
        self.school = ""
        self.type = "Primary"

def ReadFile(): 
    primarypupils = [primary() for x in range(40)]
    secondarypupils = [secondary() for x in range(60)]
    primcounter=0
    seccounter=0
    
    with open("baking.csv","r")as readfile:
        line = readfile.readline().rstrip('\n')     
        while line:
             items = line.split(",")
             if items[3] == "Primary":                
                  primarypupils[primcounter].name = items[0]
                  primarypupils[primcounter].score = int(items[1])
                  primarypupils[primcounter].school = items[2]
                  primarypupils[primcounter].type = items[3]
                  primcounter+=1                     
             else: 
                 secondarypupils[seccounter].name = items[0]
                 secondarypupils[seccounter].score = int(items[1])
                 secondarypupils[seccounter].school = items[2]
                 secondarypupils[seccounter].type = items[3]
                 seccounter+=1
             line = readfile.readline().rstrip('\n')     
    input("File Read... Press any key to continue")
    return primarypupils,secondarypupils

def calculor(primarypupils,secondarypupils):
    counter=0
    primarymax=0
    primaryposition=0
    for counter in range(0,40):
        if int(primarypupils[counter].score) > int(primarymax):
            primarymax=primarypupils[counter].score
            primaryposition=counter

    secondarymax=0
    secondaryposition=0
    for counter in range(0, 60):
        if int(secondarypupils[counter].score) > int(secondarymax):
            secondarymax = secondarypupils[counter].score    
            secondaryposition=counter

    print("Best Primary Pupil :",primarypupils[primaryposition].name + " from " +  primarypupils[primaryposition].school)
    print("Best Secondary Pupil :",secondarypupils[secondaryposition].name + " from " + secondarypupils[secondaryposition].school)


primarypupils,secondarypupils = ReadFile()
calculor(primarypupils,secondarypupils)
