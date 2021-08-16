import os
os.system('clear')



#*************** FIZZBUZZ ************************

num = 0
while (num <= 100):
	if (num % 3 == 0) and (num % 5 == 0):
		print (str(num) +". FIZZBUZZ!")
	elif (num % 3 ==0):
		print(str(num) + ". fizz!")
	elif (num % 5 ==0):
		print(str(num) + ". buzz!")
	else:
		print(str(num) + ".")
		
	
	num += 1


