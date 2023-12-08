#!/usr/bin/python3

import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
special_characters = "!£$%^&*()-_=+[{]};:'@#~,<.>/?\\|"
#characters used in password 

length = int(input("Password Length: "))
amount = int(input("Amount of Passwords: "))
print_to_file = input("Print to File? ")
if print_to_file == "yes" or print_to_file == "Yes" or print_to_file == "True" or print_to_file == "true":
	filename = input("File Name: ")
	print_to_file = True

upper,lower,nums,spec_chars = True,True,True,True
#edit booleans in order depending on what you characters want in the password(s)

all = ""
#where the characters are sampled from

if upper == True:
	all += uppercase_letters
if lower == True:
	all += lowercase_letters
if nums == True:
	all += digits
if spec_chars == True:
	all += special_characters

for x in range(int(amount)):
	password = "".join(random.sample(all,length))
	print (password)
#randomly samples characters from variable all the amount of times variable length specifies
#and does this the number of times variable specifies
	if print_to_file == True:
		with open(filename, "a") as f:
			f.write(password)
			f.write("\n")
