import os
os.system('clear')



#*************** FIZZBUZZ ************************

num = 0
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
while (num <= 1000000):
	if (num % 3 == 0) and (num % 5 == 0):
		print (str(num) +". FIZZBUZZ!")
		fizzbuzz_count += 1

	elif (num % 3 ==0):
		print(str(num) + ". fizz!")
		fizz_count += 1

	elif (num % 5 ==0):
		print(str(num) + ". buzz!")
		buzz_count += 1

	else:
		print(str(num) + ".")
		
	
	num += 1

print("*************************************")

print("*************************************")

# This is used to first print Fizz then buzz and then fizzbuzz with taab space

print("Fizz\t\tBuzz\t\tFizzBuzz")  

# "\t" will give space btwn strings and first print fizz and then the other two

#"{:,}".format----> this function is used to put comma(,) in large number like (100,000)
print(str("{:,}".format(fizz_count)) + "\t\t" + str("{:,}".format(buzz_count)) + "\t\t" + str("{:,}".format(fizzbuzz_count)))


