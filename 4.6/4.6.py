#4.6
names = [None]*100
grade = [None]*100
bib_number = [None]*100
slow_times = [None]*100
fast_times = [None]*100
def LoadOpen():
    file = open("RunnerTimes.csv","r")
    line = file.readline().rstrip('\n')
    for counter in range(0,100):
            items = line.split(",")
            names[counter] = items[0]
            grade[counter] = items[1]
            bib_number[counter] = items[2]
            slow_times[counter] = items[3]
            fast_times[counter] = items[4]
            line = file.readline().rstrip("\n")        
    file.close()

    return names,grade,bib_number,slow_times,fast_times


def Sorting(names,grade,bib_number,slow_times,fast_times):
    searchitems = int(input("Please enter the items to be searched for: "))
    counter=0
   
    for counter in range(len(bib_number)):
        bib_number[counter]=int(bib_number[counter])
        if bib_number[counter] == searchitems:
            print(names[counter])
            print(grade[counter])
            print(bib_number[counter])
            print(slow_times[counter])
            print(fast_times[counter])
            if slow_times[counter]> mintime:
                mintime = slow_times[counter]
            if fast_times[counter]< maxtime:

                


names,grade,bib_number,slow_times,fast_times = LoadOpen()

Sorting(names,grade,bib_number,slow_times,fast_times)
