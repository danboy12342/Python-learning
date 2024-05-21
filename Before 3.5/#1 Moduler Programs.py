#Funtion for input
def Getinput():
    value1 = int(input("Please enter your first number : "))
    value2 = int(input("Please enter your second number : "))
    return value1,value2

def Calc_awnser(firstvalue,secondvalue):
    awnser = firstvalue + secondvalue
    return awnser

def Dsply_awnser(awnser):
    print(number1, "+" ,number2, "= " + str(awnser))

number1,number2 = Getinput()

awnser = Calc_awnser(number1,number2)

Dsply_awnser(awnser)

    
