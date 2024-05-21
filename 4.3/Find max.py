def initialise():
    maxvalue=0
    minvalue=10000
    array1=[None]*50
    array2=[None]*50
    return array1,array2,maxvalue,minvalue

def load_print(array1,array2):
    file = open("scores.csv","r")
    line = file.readline().rstrip('\n')
    counter=0
    
    while line:
            items = line.split(",")
            array1[counter] = (items[0])
            array2[counter] = (items[1])
            line = file.readline().rstrip("\n")
            counter = counter+1
    file.close()
    return array2
    

def maxvalues(array1,maxvalue,minvalue):
  
    for counter in range(0,len(array1)):
        array1[counter]=int(array1[counter])
        if array1[counter] > maxvalue:
         maxvalue = array1[counter]
        if array1[counter] < minvalue:
         minvalue = array1[counter]
    return maxvalue,minvalue

array1,array2,maxvalue,minvalue = initialise()
array1 = load_print(array1,array2)
maxvalue,minvalue = maxvalues(array1,maxvalue,minvalue)

print(maxvalue,minvalue)
