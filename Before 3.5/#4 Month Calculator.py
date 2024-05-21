#Month calcluator

def userInput():
    days = [31,"28 or 29",31,30,31,30,31,31,30,31,30,31]
    month = ["January","Feburary","March","April","May","June","July","August","September","November","December"]
    user_input = int(input("Enter the number of a month :"))
    while user_input <1 or user_input >12:
        print("Incorrect Number of the month.")
        user_input = int(input("Enter a valid number of a month :"))
    user_input = user_input-1
    return month ,days, user_input

def calc(array1,array2,user_input):
    selected1 = array1[user_input]
    selected2 = array2[user_input]
    return selected1,selected2

def printing(day,month):
    print("|The Month is :",month)
    print("|The day is :", day)


month,day,number = userInput()
array1,array2 = calc(day,month,number)
printing(array1,array2)
    

        
        
