#4.4

names=[None]*50
forms=[None]*50
prelims=[None]*50
coursework=[None]*50
percent=[None]*50

def Load_Print():
    file = open("ComputingMarks.csv","r")
    line = file.readline().rstrip('\n')
    counter=0
    for counter in range(0,50):
            items = line.split(",")
            names[counter] = items[0]
            forms[counter] = items[1]
            prelims[counter] = items[2]
            coursework[counter] = items[3]
            line = file.readline().rstrip("\n")
            counter = counter+1       
    file.close()
    return prelims,coursework

def Calculation(marks,coursework):
    minmark = 160
    maxmark = 0
    
    for counter in range(len(marks)):
        
        marks[counter] = float(marks[counter])
        coursework[counter] = float(coursework[counter])

        percent[counter] = (marks[counter]+coursework[counter])/160
        
        
        
        if marks[counter] < minmark:
            minmark=marks[counter]
        if marks[counter] > maxmark:
            maxmark=marks[counter]
    return minmark,maxmark,percent



prelims,coursework = Load_Print()            
minmark,maxmark,percent = Calculation(prelims,coursework)
print("Min mark is :",minmark,"Max mark is :",maxmark)
for counter in range(0,len(percent)):
    percent[counter] = round(percent[counter] * 100)
    print(percent[counter],"%")
                     
 
