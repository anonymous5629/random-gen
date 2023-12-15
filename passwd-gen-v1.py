import random 

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
#where the characters are sampled from; edit depending on what you characters want in the password(s)

for x in range(amount):
	password = "".join(random.sample(all, length))
	print (password)
#randomly samples characters from variable 'all'
	if print_to_file == True:
		with open(filename, "a") as f:
			f.write(password)
			f.write("\n")
input() 
# Keeps terminal open after; can be removed if running from command line i.e. python3 passwd-gen-v1.py