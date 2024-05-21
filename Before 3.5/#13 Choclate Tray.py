#Choclate tray leftover

num_choc = int(input("Enter how many Choclate you want"))
counter = 0
while num_choc >24:
    counter = counter + 1
    num_choc = num_choc - 24

print("The number of trays is ",counter)
print("With a leftover of",num_choc)
