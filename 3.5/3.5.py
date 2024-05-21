#3.5 Test Yourself
#Parking Times

def initialise():
    hourone=1
    hourtwo=2.2
    hourthree=3.3
    hourfour=4.4
    hourtwelve=12
    hourplus=24
    intime=[None]*100
    outtime=[None]*100
    date=[None]*100
    registration=[None]*100
    stay=[None]*100
    prices=[None]*100
    return hourone,hourtwo,hourthree,hourfour,hourtwelve,hourplus,stay,outtime,intime,date,registration,prices

def load_print(outtime,intime,date,registration):
    file = open("Times.csv","r")
    line = file.readline().rstrip('\n')
    counter=0
    
    while line:
            items = line.split(",")
            registration[counter] = (items[0])
            date[counter] = (items[1])
            intime[counter] = (items[2])
            outtime[counter] = (items[3])
            line = file.readline().rstrip("\n")
            counter = counter+1
    file.close()
    
    return registration,date,intime,outtime 
   
def calculation(hourone,hourtwo,hourthree,hourfour,hourtwelve,hourplus,stay,outtime,intime,date,registrations,prices):
    counter = 0
    for counter in range (0,100):
        stay[counter] = float(outtime[counter]) - float(intime[counter])
        if stay[counter] <= 1 and stay[counter]>=0:
            prices[counter] = hourone
        elif stay[counter] <= 2 and stay[counter]>=1:     
            prices[counter] = hourtwo
        elif stay[counter] <= 3 and stay[counter]>=2:
            prices[counter] = hourthree
        elif stay[counter] <= 4 and stay[counter]>=3:
            prices[counter] = hourfour
        elif stay[counter] <=12 and stay[counter]>=4:
            prices[counter] = hourtwelve
        elif stay[counter]>=12:
            prices[counter] = hourplus
        else:
            print("error 1")
    
    return prices
        

def write_file(prices,intime,outtime,date,registration):
    with open("name.csv","w") as file:
        for counter in range(0,100):
            file.write(str(registration[counter])+","+str(date[counter])+","+str(prices[counter])+","+str(intime[counter])+","+str(outtime[counter]+"\n"))
        
            

hourone,hourtwo,hourthree,hourfour,hourtwelve,hourplus,stay,outtime,intime,date,registration,prices = initialise()

registration,date,intime,outtime = load_print(outtime,intime,date,registration)

prices = calculation(hourone,hourtwo,hourthree,hourfour,hourtwelve,hourplus,stay,outtime,intime,date,registration,prices)

write_file(prices,intime,outtime,date,registration)

