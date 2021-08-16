import re
import os
os.system('clear')

userName = input("Hello! Welcome to FaceSnap! \n\nUsername: ") 
password = input("Password: ") 

x = True
y = True

count = 0 
count += 1 


while x and y: 
	if count == 3: 
		print("\nThree Username and Password Attempts used. Goodbye") 
		break

	elif userName == 'userName':
	    print("")
	    break 
	elif not re.search("[a-z]",password):
		print("Password must contain small letters")
		break
	elif not re.search("[0-9]",password):
		print("Password must contain numbers")
		break
	elif not re.search("[A-Z]",password):
		print("Password must contain capital letters")
		break
	    
	elif not re.search("[$#@]",password):
		print("Password must contain special characters")
		break
	    
	elif re.search("\s",password):

	    break
	else:
	    print("Valid Password")
	    x=False
	    break

if x and y:
	print("Not a Valid Password")

