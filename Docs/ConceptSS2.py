# here is a function is not required the value is returned
# def say_hi(name):
# 	""""function to say hello with users"""
# 	print('Hello', name , "Nice try")
# print(say_hi.__doc__)

# here is a function is required the value had returned:
# def type_number(num):
# 	"""Print odd or even number"""
# 	if num % 2 == 0:
# 		return print(num, "is even number")
# 	else:
# 		return print(num, "is odd number")
# print(type_number.__doc__) #See the docstring of func type_number
# type_number(132)

# Example with function:
# Check the divisor of number 7 from 1 to 100
# def is_divisor(number):
# 	print("danh sach cac so chia het cho", number, "la: ")
# 	for i in range(1, 101):
# 		if i % number == 0:
# 			print(i, end=', ')
# is_divisor(7)
# def is_divisor(number):
# 	if number % 7 == 0:
# 		return True
# 	else:
# 		return False
# for i in range(1, 101):
# 	if is_divisor(i):
# 		print(i, end=", ")

# Solve the math with some exercise:
# Find the prime number
# def is_prime(number):
# 	if number == 2:
# 		return True
# 	elif number % 2 == 0:
# 		return False
# 	elif number < 2:
# 		return False
# 	else:
# 		for i in range(3, number, 2):
# 			if number % i == 0:
# 				return False
# 	return True
# indexes = 0
# for i in range(1, 101):
# 	if is_prime(i):
# 		indexes += 1
# 		print(i, end=" ") # print the divisor numbers
# print()
# print("Tong so indexes:", indexes)

# Default parameter example
# def hello(name, letter = "How are you feeling today?"):
# 	print(name, letter)
# hello("daniel")
# hello("daniel", "New")
# another example to use default parameter in function
# def hello(name, letter):
# 	print(name, letter)
# hello(name="Daniel", letter="How are you?")
# hello(letter="Hello world?", name="Qi")

# Tham so khong gioi han ( parameter )
# def user(*names):
# 	for name in names:
# 		print("Hello", name)
# user("Qie","Daniel","Bie","Em",) # > Tuple: so have to use loop to get a value to value

# De quy ( callback function )
# Tinh giai thua cua 1 so
# def giaithua_x(number):
# 	if number == 1:
# 		return 1
# 	else:
# 		return (number * giaithua_x(number - 1))
# 	# callback right here:
# 	# 1. 4 * giaithua_x(4 - 1)
# 	# 2. 4 * 3 * giaithua_x(3 - 1)
# 	# 3. 4 * 3 * 2 * 1 # The statment if x == 1: return 1
# num = 4
# print(giaithua_x(num))
# khu de quy ( use loop change callback func
# Callback function make wast the memory of computer and made not good perform to app or user interactive ( tuong tac )
# num = 4
# result = 1
# for i in range(1, num + 1):
# 	result = result * i
# print(result)

# Lambda func: a unknown func, its basic func( havent name_function and have only 1 expression in this. )
# double = lambda x: x * 2 # define a varible is equal with lambda func
# it same with:
# def double(x):
# 	return x * 2
# print(double(2))

# The real benefit of lambda func:
# useful when a parameter of function is a function such as map(), reduce(), filter()
# def my_func(x):
# 	return lambda a: a * x
# my_result = my_func(2)
# print(my_result(12))

# example: calculate area of rectangle
# def area_rectangle(l, w):
# 	return l * w
# print(f'Area of rectangle is {area_rectangle(2,3)}')
# example: calculate area of rectangle with lambda
# area_rectangle = lambda l, x: l * x
# print(f"Area of rectangle is {area_rectangle(2, 3)}")

# filter func: fil the data with argument get in
# filter have 2 arguments:
# 1. the FUNCTION expression
# 2. the object need to edit
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = list(filter((lambda x: (x % 2 == 0)), (my_list)))
# print(new_list)

# map func: to edit the parameter is got in
# have 2 parameter:
# example: map(function expression, the object need to edit)
# 1. the function expression
# 2. the object need to edit
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = list(map((lambda x: x * 2), my_list))
# print(new_list)

# Global variable
# Position: it was put in out function or in global range
# The value of global variable can be use inside or outside function
# x = "Hello world" #This is a global variable
# def test():
# 	print(x, "Daniel") # value of x variable is here because global variable can access inside or
# # outside the function
# test()
# print(x, "Bie") # value of x variable is here because global variable can access inside or
# # outside the function

# Example for global variable:
# x = 10
#
#
# def foo():
# 	global x
# 	x = x * 2
# 	print(x)
#
#
# foo()
# print(x)

# Local variable: is a variable put inside a function, or declared in range of local variable
# can use it in outside the func of it
# def foo():
# 	x = "Hello world"
# 	print(x) # x only available inside the function here
# foo()
# print(x) # will error because x is not defined

# GLOBAL KEYWORD: default point to the global variable outside
# x = "Hello world!"
# a = "Hello world!"
# def foo():
# 	global x # point to the x global variable
# 	x = x * 2
# foo()
# print(x) # print x variable after code in the function
# print(a) # default print a variable ( in this case a is a global variable )

# Exercise about function
# Calculate average a list score subject
# print("Calculate average of all subject")
# m = 0  # math
# p = 0  # physical
# e = 0  # english
# l = 0  # literary
# t = 0  # technology
# def check_type(v):
# 	""""Function check type of number input: if type isn't int or float: as """
# 	while True:
# 		try:
# 			v = int(v)
# 			break
# 		except ValueError:
# 			try:
# 				v = float(v)
# 				break
# 			except ValueError:
# 				print("Just allow type NUMBER, please put value again")
# 				# print(f"Put {} score")
# 				v = input()
#
# def get_score():
# 	""""Get score of user and check the type of it, just allow the type NUMBER"""
# 	print("Put math score")
# 	m = input()
# 	check_type(m)
# 	print("Put physical score")
# 	p = input()
# 	check_type(p)
# 	print("Put english score")
# 	e = input()
# 	check_type(e)
# 	print("Put literary score")
# 	l = input()
# 	check_type(l)
# 	print("Put technology score")
# 	t = input()
# 	check_type(t)
#
# 	#define the varible to calculate average
# 	list_subject = [m, p, e, l, t]
# 	sum_score = m + p + e + l + t
# 	average = sum_score / len(list_subject)
# 	return average
# def check_result(score):
# 	print("Average your score is: ", score)
# 	if score < 5:
# 		print("HSTB")
# 	elif 5 <= score < 8:
# 		print("HSTT")
# 	elif 8 < score <= 10:
# 		print("HSG")
# average = get_score()
# check_result(average)

# Func check is this number prime:
# Step to solve
# 1 define a function check and have 1 parameter (n)
# - declare a variable is_prime and set value is True, use if statement to remove the value isnt prime number
# - use a for loop to point the number from 3 to (n) , step is 2:
# to point the odd number: and specify the odd number isn't divisor number of odd number else.
# 2 make a for loop in range from distance of math:
# - call the func check if put the variable of for loop in:
# Solve:
# def check_prime(n):
# 	""""a function to check number is prime number, or check the prime number of list number  """
# 	is_prime = True
# 	if n == 2:
# 		is_prime = True
# 	elif n < 2:
# 		is_prime = False
# 	elif n % 2 == 0:
# 		is_prime = False
# 	else:
# 		for i in range(3, n, 2):
# 			if n % i == 0:
# 				is_prime = False
# 	return is_prime
# sum_result = 0
# start = 0
# end = 100
# for i in range(start, end + 1):
# 	if check_prime(i):
# 		print(i)
# 		sum_result += i
# print("Sum of the list prime number from ", start, " to ", end," = ", sum_result)
# print(check_prime.__doc__)
#
#
# Exercise: find the largest number between 3 numbers
# Step to solve:
# 1 Define a function have 3 parameters ( such as 3 number ): define a varible is max and
# set it is a, then use if statement to
# def check_number(a, b, c):
# 	"""Func to check the value between numbers, return the largest number after comparison it"""
# 	max = a
# 	if a < b:
# 		max = b
# 	if b < c:
# 		max = c
# 	return max
# print("put number a")
# a = input()
# while True:
# 	try:
# 		a = int(a)
# 		break
# 	except ValueError:
# 		try:
# 			a = float(a)
# 			break
# 		except ValueError:
# 			print("Something was wrong, put number a again")
# 			a = input()
# print("put number b")
# b = input()
# while True:
# 	try:
# 		b = int(b)
# 		break
# 	except ValueError:
# 		try:
# 			b = float(b)
# 			break
# 		except ValueError:
# 			print("Something was wrong, put number b again")
# 			b = input()
# print("put number c")
# c = input()
# while True:
# 	try:
# 		c = int(c)
# 		break
# 	except ValueError:
# 		try:
# 			c = float(c)
# 			break
# 		except ValueError:
# 			print("Something was wrong, put number c again")
# 			c = input()
# print("the largest number between", a,", ", b, " and ", c, " is ", check_number(a, b, c))

# Define a func to calculate the math exam: S = 1 + 1/2 + ........ 1/n
# def calculate_x(n):
# 	""""Define a func to calculate the math exam: S = 1 + 1/2 + ........ 1/n"""
# 	result = 0
# 	while True:
# 		try:
# 			n = int(n)
# 			break
# 		except ValueError:
# 			try:
# 				n = float(n)
# 				break
# 			except ValueError:
# 				print("Was wrong, because you put the type value is", type(n))
# 				print("Put number again")
# 				n = input()
# 	for i in range(1, n+1):
# 		result += 1/i
# 	print("The result of this math is", result)
# calculate_x(2)

# Exercise: define a function to print information of student
# Request:
# 1 input name first
# 2 request the age, then print the name + age
# 3 request the sex, then print the name + sex
# 4 request the national, then print the name + national#
# Step to solve:
# def name_user(name):
# 	return lambda infor: name + " " + infor
# print("What is your name?")
# name = input()
# infor_user = name_user(name)
# print("How old are you?")
# age = input()
# print(infor_user(age))

# func calculate compound
# def request_number(n):
# 	while True:
# 		try:
# 			n = int(n)
# 			break
# 		except ValueError:
# 			try:
# 				n = float(n)
# 				break
# 			except ValueError:
# 				print("The input just allow type NUMBER")
# 				n = input()
## def calculate_margin():
# 	result = 0
# 	margin = 0
# 	compounding = 0
# 	print("How much money which you want to calculate?")
# 	fund = int(input())
# 	request_number(fund)
# 	print("The margin banking in your localtion?")
# 	percent = int(input())
# 	request_number(percent)
# 	print("How long you might to put your money in?")
# 	year = int(input())
# 	request_number(year)
# 	result = fund*(1+(percent/100)/1)**1*year
# 	print(f"With basic margin banking is {percent}%, {fund} VND after {year} years equal {result} VND ")
#
# calculate_margin()

# Exercise: calculate the math S = 1 + 2 + 3 + 4 + ...... n
# step to solve:
# 1 define a func have 1 parameter is the number which calculate,
# the func will start until the parameter is number 1, use if statement to solve this, and then
# return parameter + func(parameter - 1) # like 2 + (2-1) = 3 > with n = 2, S = 1 + 2
# list = ["user1","user2","user3","user4"]
# list.append("userH")
# print(f"Current value {list}")
# # value = input("Put the value you need to add\n")
# # index = int(input("Put the value you need to add\n"))
# # list.insert(index, value)
# print(isinstance(list[-1], str))
# print(f"Updated value: {list}")
# data = ["hello", 19]
# data = set(data)
# data2 = {19, 20, "hi"}
# print(set.__doc__)
# print(data ^ data2)
# data_tuple = (
# 	["biee", 19, "Vietnam"],
# 	["qie", 20, "Vietnam"],
# 	["bieehoang", 19, "Vietnam"],
# )
# data_tuple[0][0] = "quy"
#
# data_dict = {
# 	"user0": data_tuple[0],
# 	"user1": data_tuple[1],
# 	"user2": data_tuple[2],
# }
# data_dict["user1"][0] = "daniel"
# print(data_dict["user1"])
# squares = {1:1, 2:1, 3:1, 4:1, 5:1}
# index = 0
# for i in squares:
# 	squares[i] =  i ** 2
# 	index += 1
# print(squares)

