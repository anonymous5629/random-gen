from random import sample

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "1234567890"
spec_chars = "!£$%^&*()-_=+[{]};:\'@#~,<.>/?\\|"
#characters used in password 
length = int(input("Password Length: "))
amount = int(input("Amount of Passwords: "))
print_to_file = input("Print to File? ")
if print_to_file in ["Yes", "yes"]:
	filename = input("File Name: ")
	print_to_file = True

all = (uppercase + lowercase + digits + spec_chars)
if length > 99:
	all = all*int(length/10)
#where the characters are sampled from; edit depending on what you characters want in the password(s)
passlist = []

for x in range(amount):
	password = "".join(sample(all, length))
	passlist.append(password)
	
passlst = "\n".join(passlist)
print(passlst)
#randomly samples characters from variable 'all'
if print_to_file == True:
	with open(filename, "a") as f:
		f.write(passlst)
input() 
# Keeps terminal open after; can be removed if running from command line i.e. python3 passwd-gen-v1.py