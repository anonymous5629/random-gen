import random

digits = "1234567890"

length = int(input("Amount of Digits: "))
amount = int(input("Amount of Numbers: "))
state = input("Positive, Negative or Random: ")
print_to_file = input("Print to File? ")

if print_to_file in ["yes", "Yes", "True", "true"]:
	filename = input("File Name: ")
	print_to_file = True
if length > 10:
	digits = "1234567890" * length

if state in ["Positve", "positive"]:
	type = False
elif state in ["Negative", "negative"]:
	type = True

for x in range(amount):
	number = "".join(random.sample(digits,length))
	if type == False:
		print (" ", number)
	if type == True:
		print ("-", number)
	if type not in [True, False]:
		print (random.choice(["-", " "]), number)
# Prints Number with negative or no negative
	if print_to_file == True:
		with open(filename, "a") as f:
			if type == True:
				f.write("-", number)
				f.write("\n")
			if type == False:
				f.write(number)
				f.write("\n")
