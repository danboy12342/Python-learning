
def user_input():
    num = int(input("Enter a prime number"))
    return num


def calc(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for counter in range(2, int(num ** 0.5) + 1):
        if (num % counter) == 0:
            return False  # Not a prime number
    return True  # Is a prime number

            
                   
def output(opperator,num):
        if opperator == True:
            print(num, "is not a prime number")
        else:   
            print(num, "is a prime number")

            
user = user_input()
boolean = calc(user)
output(boolean,user)
