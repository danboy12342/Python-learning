#Peter 20/06/23 50%

#Module to get Inputs
def getnames():
    counter = 0
    usernames = [""]*10
    usergrade = [None]*10
    for counter in range(0,10):
        usernames[counter] = input("Enter name")
        usergrade[counter] = int(input("Enter Grade"))
    return usernames,usergrade


#Module to output pass or fail
def output(usernames,usergrade):
    counter = 0
    for counter in range(0,10):
        if usergrade[counter] < 51:
            print(usernames[counter] , "Failed")
        else:
            print(usernames[counter] , "Passed")

#Main Body of Code


name,grade = getnames()
output(name,grade)
            


            


