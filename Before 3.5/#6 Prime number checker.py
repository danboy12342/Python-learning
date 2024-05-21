
def user_input():
    num = int(input("Enter a prime number"))
    return num


def calc(num):
    opperator = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for counter in range(2, num):
            if (num % counter) == 0:
                opperator = True
                return opperator
            
                   
def output(opperator,num):
        if opperator == True:
            print(num, "is not a prime number")
        else:   
            print(num, "is a prime number")

            
user = user_input()
boolean = calc(user)
output(boolean,user)
