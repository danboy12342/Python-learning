#Gas bill calculator

def Input_user():
    previos_gas_reading = float(input("Please enter a previos Gasmeter  value :"))
    current_gas_reading = float(input("Please enter a current Gasmeter  value :"))
   
    return current_gas_reading , previos_gas_reading 

def calc(first_reading,second_reading):
    unit = (first_reading - second_reading)
    corrected_unit = unit * 1.02264
    metric = corrected_unit * 2.83
    caloric = metric * 39.3
    kWh = caloric / 3.6
    price = kWh * 0.0374
    price = (price * 0.05) + price
    kWh = round(kWh,2)
    price = round(price,2)
    return first_reading,second_reading,unit,kWh,price

def print_answr(unit1,unit2,unit3,unit4,unit5):
    print("Previous reading :", unit1)
    print("Current reading :", unit2)
    print()
    print("You have used :", unit3)
    print("This is", unit4 ,"Kilowatt hours")
    print("Your bill is £",unit5)
        
    
firstreading,secondreading = Input_user()
firstreading,secondreading,unit,kWh,price = calc(firstreading,secondreading)
print_answr(firstreading,secondreading,unit,kWh,price)
