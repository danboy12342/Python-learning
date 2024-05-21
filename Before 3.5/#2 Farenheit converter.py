#farenheit converter

def Input_user():
    user = float(input("Please enter a celsius value :"))
    return  user

def calc(first):
    farenheit = (first*1.8)+32
    return farenheit

def print_answr(number,farenheit):
    print(str(number),"degrees centigrade is ",str(farenheit)," farenheit")

number = Input_user()
farenheit = calc(number)
print_answr(number,farenheit)

