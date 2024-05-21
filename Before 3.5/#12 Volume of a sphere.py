#Sphere Volume Calculator
radius = float(input("Enter the radius of the circle in M:"))
radiuscubed = float(radius*radius*radius)
three=float(4 / 3)
pi = float(3.141592653)
volume = float(three*pi*radiuscubed)
volume = round(volume)
volume = str(volume)
cm="m^3"
print(volume+cm)
