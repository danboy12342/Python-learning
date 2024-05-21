#Vat Calculator
def userInput():
    price = int(input("Enter a Price :"))
    return price
def calc(money):
    final = money *1.2
    final = round(final,2)
    return final
def printing(answer):
    print("The final price is : £",answer)

price = userInput()
answer = calc(price)
printing(answer)
