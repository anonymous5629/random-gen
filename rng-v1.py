#!/usr/bin/python3

import random

digits = "1234567890"

length = int(input("Amount of Digits: "))
amount = int(input("Amount of Numbers: "))
type = input("Positive, Negative or Random: ")
print_to_file = input("Print to File? ")

if print_to_file in ["yes", "Yes", "True", "true"]:
	filename = input("File Name: ")
	print_to_file = True
if length > 10:
	digits = "1234567890" * length


if type in ["Positve", "positive"]:
	type = False
elif type in ["Negative", "negative"]:
	type = True
elif type in ["Random", "random"]:
	type = random.choice([True, False])

for x in range(amount):
	number = "".join(random.sample(digits,length))
	if type == False:
		print (number)
	if type == True:
		print ("-", number)
	if print_to_file == True:
		with open(filename, "a") as f:
			if type == True:
				f.write("-", number)
				f.write("\n")
			if type == False:
				f.write(number)
				f.write("\n")
