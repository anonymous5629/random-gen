from random import uniform

upperb = int(input("Upper Bound: "))
lowerb = int(input("Lower Bound: "))
decimal = int(input("Amount of Decimals: "))
amount = int(input("Amount of Numbers: "))
print_to_file = input("Print to File? ")
#User input parameters for number generated

if print_to_file in ["yes", "Yes"]:
	filename = input("File Name: ")
	print_to_file = True

for x in range(amount):
	number = round(uniform(lowerb, upperb), decimal)
	if decimal == 0:
		print (int(number))
	else:
		print (number)
	if print_to_file == True:
		with open(filename, "a") as f:
			f.write( number, "\n")
input()
# Keeps terminal open after; can be removed if running from command line i.e. python3 rng-v1.py