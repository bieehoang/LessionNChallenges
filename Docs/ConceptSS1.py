# import decimal #use decimal module
# from decimal import  Decimal as D #use decimal module
# import fractions #this module is support the way to working with so thap phan
# from fractions import Fraction as F #this module is support the way to working with so thap phan
# import math
# import random
# c = 5 + 3j
# print(type ( c + 3)) #use type to check the type of this element or the method,
# print(isinstance(c, complex)) # To check is type of this value same true or false
# print(0xFB + 0b10) #Hexadecimal and #Binary
# print(F(5,5))
# can use type of number to convert it
# print(float(3)) # convert 3 (type interger) to 3.0 (type is float)
# print(D(1.1 + 1.3)) #demacial: module to working with so thap phan, voi muc dich cho ra ket qua, hay voi bai toan yeu cau so lieu cu the, chinh xac hon
# About Fraction: lam viec voi so thap phan
# print(fractions.Fraction(1.5))

# a = [1,2,3,4,5,6,7] #List #type List
# print(random.randrange(1,7,2)) #sap sep lai element of list,

# *working with array
# thisList = ['banana','apple','pineapple'] #list
# thisList[1] = 'hello world'
# Lap qua tung phan tu: use for loop hoac while loop to truy cap tung phan tu cua mang
# for list in thisList:
# 	print ('Fruits:', list)

# kiem tra gia tri co o trong mang?
# if 'apple' in thisList:
# 	print('Apple co trong ham nay')

# them phan tu vao mang bang append method cua List
# thisList.append('lemon')
# Xoa phan tu ra khoi mang?
# thisList.remove('lemon') #remove method
# thisList.pop(3) #pop() method, if dont add indexes into, method will auto remove at last value
# del thisList[1]#del keyword,
# del # another del can delete all element
# thisList.clear()#clear method to clear all elements of this List
# print(thisList)

# this is Dictionary type, acctually it's same with Object in javascript, inside have two element is KEY and VALUE
# my_infor = {
# 	"user1": {
# 		"name": "Daniel",
# 		 "age": 20,
# 		 "sex": "male"},
# 	"user2": {
# 		"name": "Biee",
# 		"age": 19,
# 		"sex": "male"},
# 	"use3": {
# 		"name": "Quy",
# 		"age": 21,
# 		"sex": "male"},
# }
# print(my_infor["user1"]["name"])
# my_tuple = (4, 2, 3, [6, 5]) #type tuple: same with List, the different thing is cant change the element in tuple, just can change if inside tuple is a another list

# Thay đổi giá trị cho phần tử thứ nhất của phần tử thứ 4 trong my_tuple.
# my_tuple[3][0] = 9
# print(my_tuple)
# print(my_tuple.count(2) #method count to check how many time this element run in
# print(my_tuple.index(4)) #method index to return indexes of element which need to find

# Dictionary: same with object in Javascript
# a = my_infor["user2"].get("sex") #get() method which is get element from the key of this Dictionary
# print(a)
# print(my_infor["user1"]['name']) #get value bằng chỉ dấu ngoặc vuông và key
# the way add elemnt into Dictionary
# my_infor["user1"]["address"] = "Downtown"
# the way toi remove the element out of Dictionary
# my_infor["user1"].pop("name") #pop() method: return value of the key was puted in, delete element  have key is name and value of it
# my_infor["user1"].popitem() #popitem() method: return the (key, value) of the Dictionary, delete the element at last of element
# my_infor["user1"].clear()
# del my_infor
# print(my_infor["user1"])

# new_int = 123 #type this is interger ( lower than type float )
# new_float = 12.3 #this type is float ( higher type interger )
# new_complex = 1j + 3 #this type is complex
# new_str = "246"
# new_str = int(new_str) #typecasting: convert maintly of element to the type developer need, instance here: we need convert type of new_str to int, so we use the declare int and convert it
# new_str = complex(3+ 3j)
# print(isinstance(new_str, complex)) #type of new_str was converted from str to int
# new_value1 = new_int + new_float # This type was converted to the type rank higher ( in this case is float )
# new_value2 = new_float + new_complex # same with the operator in upper line
# print('Result of this operator:', new_value2) #135.5
# print(type(new_value2)) #result is float

# * If else elif
# Use if else to make a feature to notice number of day:
# day = 9
# if day == 2:
# 	print('Hôm nay là thứ', day);
# elif day == 3:
# 	print('Hôm nay là thứ', day);
# elif day == 4:
# 	print('Hôm nay là thứ', day);
# elif day == 5:
# 	print('Hôm nay là thứ', day);
# elif day == 6:
# 	print('Hôm nay là thứ', day);
# elif day == 7:
# 	print('Hôm nay là thứ', day);
# else:
# 	print('Hôm nay là Chủ nhật')

# find the numbers has value biggest
# number1 = 100
# number2 = 400
# number3 = 500
# #purpose number 1 is biggest
# max = number1
#
# if max < number2:
# 	max = number2
# if max < number3:
# 	max = number3
#
# print('The number biggest is', max)

# *For loop
# use for loop to extract the symbol of the letter
# letter = 'HelloWorld'
# for symbol in letter:
# 	print('Tung ki tu cua chu la:', symbol)
# for i in range(0, 11, 2): #range have 3 value inside: start, end, step
# 	print(i, end=', ' )
# fruits = ['apple', 'pineapple', 'mango']
# print(range(len(fruits))) #return range(0,3)
# for fruit in range(len(fruits)):
# 	print('Fruit:', fruits[fruit])
# Exercise321: Viet 1 block code to trinh bay so nhap vao co la so le hay so chan
# for index in range(0, 11):
# 	if index % 2 == 0:
# 		print(index, 'la so chan')
# 	else: print(index, 'la so le')
# #another instance with for
# for indexx in range(5):
# 	print(indexx, end=', ')
# else: print('Tong so phan tu la', indexx + 1)
# numbers = [1,2,3,4,5,6,7,8,9]
# for i1 in range(len(numbers) +1 ):
# 	for i2 in range(2,10):
# 		print(i1, 'x', i2, '=', i1*i2 )

# #For loop in for loop to excute a caculator
# for n1 in range(2,10)
# 	for n2 in range(1,10):
# 		print(n1, 'x', n2, '=', n1 * n2)

# If else in loop: in this case, check the type of number is chan hay le
# for number in range(1,10 + 1):
# 	if number % 2 == 0:
# 		print(number, 'la so chan')
# 	else:
# 		print(number, 'la so le')

# While loop

# number = 1
# while(number < 10):
# 	print('Luot dem', number)
# 	number = number + 1 # Expression to prevent the loop dont go to ove-extremly
# print('End')

# use while loop to made a calulator bang cuu chuong
# i = 1
# j = 1while i <= 9:
# 	while j <= 9:
# 		print(i, 'x', j, '=', i * j)
# 		i = i + 1
# 		j = j + 1
# 	print('End')

# break and continue statement in Python

# for key in 'Hello':
# 	if key == 'e':
# 		break #dung vong lap ngay khi gia tri cua lan lap nay thoa man dieu kien, dung vong lap ngay
# 		continue # bo qua gia tri cua lan lap co gia tri tuong ung nay, Khong dung lai ma tiep tuc o nhung lan lap tiep theo
# 	print(key)

# *Exercise32

# #convert data input to int or float to check this is true or false
# user_age = input('Nhap tuoi cua ban ')
# print('\n')
# #kiem tra nguoi dung nhap vao la number hay khong, ep du lieu nhap vao sang int hay float,
# # su dung try and exception de thuc hien bai bai toan nay
# try:
# 	val = int(user_age)
# 	print('nam nay ban ', val, 'tuoi')
# except ValueError:
# 	try:
# 		val1 = float(user_age)
# 		print('nam nay ban ', int(val1), 'tuoi')
# 	except ValueError:
# 		print('Ban dang hoi nham lan ?')
# su dung ham isdigit de kiem tra la number hay la str
# if user_age.isdigit():
# 	print('Kieu gia tri nhap vao la Number')
# else: print('Kieu gia tri nhap vao khong phai la number')
# ham nay chi hoat dong voi so duong, Neu nhap vao la mot so thuv hoav mot so am thi no se tra vr la chuoi, vi vay
# giai phap tot nhat van la su dung ep kieu int hay float de kiem tra du lieu nguoi dung nhap vao co phai la Number hay khong

# Code a func to required input a number
# while True:
# 	user_age = input('Nhap tuoi cua ban')
# 	try:
# 		val1 = int(user_age)
# 		print('Hien tai ban', val1, 'tuoi')
# 		break;
# 	except ValueError:
# 		try:
# 			val2 = float(user_age)
# 			print('Hien tai ban', val2, 'tuoi')
# 			break;
# 		except ValueError:
# 			print('Ban dang gap su co?')

# caculate sum of a list
# step to do
# 1. declare a varible to save the result of this caculate
# 2. made a for loop to get in value from 1 to n
# use the for loop
# sum = 0 #this is a varible to save the result
# n = 0
# print('Put your number which need to caculate here')
# n = int(input())
# for i in range(0, n + 1 ):
# 	sum += i
# print('Your result is', sum)
# use the while loop
# sum = 0 #tong gia tri cua phep tinh
# n = 0 #gia tri nhap vao input
# i = 0 #dieu kien lap (khai bao truoc doi voi while loop )
# print('put your number which need to caculate here')
# n = int(input())
# while i <= n:
# 	sum += i
# 	i += 1
# print('Your result is', sum)

# Code to check the value user put in, is Number > agree, opposite > disagree
# while True:
# 	print('Please type your password here')
# 	user_input = input()
# 	try:
# 		value = int(user_input)
# 		print("Your password you've type is", value)
# 		break
# 	except ValueError:
# 		try:
# 			value = float(user_input)
# 			print("Your password you've type is", value)
# 			break
# 		except ValueError:
# 			print('This block just allow the type password is Number')

# * Exercise3 to caculate of the math type: S(n) = n**2 + n**2 + ... n ** 2
# Step:
# 1. Declare a varible to stored the result
# 2. Use the loop: for range or while or st else
# 3. Use the algorithms **: a**b same with a^b
# sum = 0
# n = 0
# square_root_number = 2 # the number which is square root availbe with the exercise
# # i = 0 # for the while loop
# print('Put your number which you need to caculate here')
# while True:
# 	try:
# 		n = int(input())
# 		sum += n** square_root_number
# 		print('Result is', sum)
# 		break
# 	except ValueError:
# 		try:
# 			n = float(input())
# 			sum += n **  square_root_number
# 			print('Result is', sum)
# 			break
# 		except ValueError:
# 			print("Sure about the type you've put in?")

# * Exercise4: caculate of the math type: S(n) = 1 + 1/2 + ... 1/n
# Step:
# 1. Declare a varible to stored the result
# 2. Use the loop: for range or while or st else
# 3. Use the algorithms /: a/b
# result = 0
# n = 0
# print('The number which need to caculate')
# n = int(input())
# for i in range(1, n+1):
# 	result += 1/i
# print('Result is', result)

# * Exercise5: caculate of the math type: S(n) = 1/2 + 1/4 + ... 1/2n
# Step:
# 1. Declare a varible to stored the result
# 2. Use the loop: for range or while or st else
# 3. Use the algorithms / and *: a/(b*2) same with 1/(2*1), inside a is 1 and b is 2
# result = 0
# n = 0
# i = 1
# print('Put in the number which you need to caculate')
# n = int(input())
# while i <= n:
# 	result += 1/(2*i)
# 	i += 1
# print('result is', result)
# for i in range(1, n+1):
# 	result += 1 / (2*i)
# print('result is', result)

# * Exercise6: caculate of the math type: S(n) = 1/3 + 1/5 + ... 1/( 2n + 1)
# Step:
# 1. Declare a varible to stored the result
# 2. Use the loop: for range or while or st else
# 3. Use the algorithms +, /, * and (): a/(b*2 + 1) same with 1/(2*1 + 1), inside a is 1 and b is 2
# result = 0
# n = 0
# # i = 1 # index for while loop
# print('Put your number which you need to caculate here')
# n = int(input())
# for i in range(1, n+1):
# 	result += 1/(2*i + 1)
# print('Result is', result)

# * Exercise7: Find the divisor of a number
# Divisor: Call N is a number, which numbers is divided by N is divisor of N
# Example: N = {1,3,5,15} this is a list numbers which is divisor of number 15
# Step: 1. Use the loop: for range or while loop 2. Use if statement to check the  statement 3.Use the algorithm %: a%b = 0
# print('Put number which you need to caculate divisor here')
# user_input = int(input())
# print('list divisors of', user_input, 'is:')
# for i in range(1, user_input + 1):
# 	if (user_input % i == 0):
# 		result = i
# 		print(result, end=', ')

# * Exercise8: Find sum of list divisor of a number
# Divisor: Call N is a number, which numbers is divided by N is divisor of N
# Example: N = {1,3,5,15} this is a list numbers which is divisor of number 15 so now i can caculate the sum of this list by use the loop, the if statement and % algorithm
# Step: 1. Use the loop: for range or while loop 2. Use if statement to check the statement 3.Use the algorithm %: a%b = 0
# print('Put number which you need to caculate divisor here')
# sum = 0
# n = int(input())
# for i in range(1, n + 1):
# 	if n % i == 0:
# 		sum += i
# print('Sum of the list divisor of', n, 'is', sum)

# * Exercise9: Find the largest odd number of a divisor
# Divisor: Call N is a number, which numbers is divided by N is divisor of N
# Example: N = {1,3,5,15} this is a list numbers which is divisor of number 15 so now i can find the largest odd number by use the loop, loop for N to 1 ( its better than 1 to N ),
# the if statement cover inside is % algorithm and %2 != 0 to remove the odd numbers and select the even number, NOTE: have to break as soon as when the code run
# Step: 1. Use the loop: for range or while loop 2. Use if statement to check the statement 3.Use the algorithm %: a%b = 0
# print('Put number which you need to caculate divisor here')
# result = 0
# n = int(input())
# for i in range(n + 1, 1, -1):
# 	if ( n % i == 0 and i % 2 != 0 ):
# 		result = i
# 		break
# print('The biggest odd number of', n, 'is', result)


# * Exercise10: Find the perfect number
# perfect number: is a number which have sum of list divisor ( from 1 to n -1 ) and the sum of it is equal with n ( the number which we put in to check is it a perfect number )
# Example: 6 is a number perfect because in range( 1, 6 -1 ) have a list = {1, 2, 3} and the sum of numbers in this list is equal with 6,
# some example another: with 8, in range ( 1, 8-1) have a list = {1,2,4} and the sum of numbers in this list is NOT EQUAL with 8 ( 7 != 8 ) so 8 isn't a perfect number
# The step solve: 1. declare a varible to stored the result
# 1. Use the loop: for range or while loop
# 2. Use if statement to check the statement: % algorithm == 0 to find the divisor of this number and += algorithm to caculate sum of divisior list
# 3.Use the == algorithm to check is this number is perfect number
# print('Put number which you need to check is it a PERFECT NUMBER here')
# result = 0
# n = int(input())
# for i in range(1, n):
# 	if n % i == 0:
# 		result += i
# if result == n:
# 	print(n, 'is perfect number')
# else:
# 	print(n, "isn't perfect number")

# * Exercise11: Find the perfect number
# square number: is a number which was build by a other number square root, another way square number is numbers when square return a interger
# Example:4 is a square number, square root 4 is equal 2 ( the second condition in the line up ) and square 2 is equal 4 ( the first condition in the line up )
# The step solve: 1. declare a varible is set default is False
# 1. Use the loop: for range or while loop
# 2. Use if statement to check the statement: i**2 = n to caculate when square is it equal with the n
# 3. Set the type of varible which we declared and set default is False to check the number is True
# 4. another will return n isn't square number
# 5. Bellow here is the func to check, have a type to check and just allow only type int and float
# print('Put the number which you need to check is it SQUARE NUMBER')
# while True:
# 	n = input()
# 	try:
# 		val = int(n) or float(n)
# 		type_number = False
# 		for i in range(2, val + 1):
# 			if i ** 2 == val:
# 				type_number = True
# 		if type_number == True:
# 			print(val, 'is SQUARE NUMBER')
# 			break
# 		else:
# 			print(val, "isn't SQUARE NUMBER")
# 			break
# 	except ValueError:
# 		print('Just allow NUMBER, for example: 123, 12.3.....')
# 		print('Put your number bellow here to check again')

# * Exercise11: check is number prime
# prime: is a number which only divisible to 1 and itself
# Example:3 is a prime, divisible to 1 and itself (3)
# The step solve: 1. declare a varible is set default is False
# 2. So acctually only 2 is even number prime. ( it just can divisible to 1 and it self, not else )
# The if statement is remove number 1 and even number, ( just allow number 2 )
# 3. Use the loop: for range or while loop to check is this number have any divisor else > if yes: remove else: get
# print('Put number bigger than N, you need to check is it PRIME')
# isPrime = True
# n = int(input())
# if n == 2:
# 	isPrime = True
# elif n % 2 == 0:
# 	isPrime = False
# elif n < 2:
# 	isPrime = False
# else:
# 	for i in range(3, n, 2): #check number which put in have any divisor else or not
# 		if n % i == 0:
# 			isPrime = False
# if isPrime == True:
# 	print(n, 'is PRIME')
# else:
# 	print(n, "isn't PRIME")


# * Exercise12: translate a number from start to end to end to start: example: 123 > 321
# Step to solve this problem:
# 1. Use while loop to check the statment: if the number put in isn't equal 0 > can move into next step
# 2. print the the first number at the end of number was translated by algorithm %10:
# 3. use //: to solve - get the interger on last number ( like : 1/10 : 10.10.010.0010.00011e > 1//10: 1 )
# print(12%10)
# print('Put the number which you need to stranslate here')
# n = int(input())
# while n != 0: # 123: check is 123 != 0 > accept to into
	# print(n%10) # 123%10 = 3
	# n = n//10 # 123//10 = 12 then continue in while loop until the statement is not true
# Same with exercise but declare a varible to stored the result
# result = ''
# while n != 0:
# 	result += str(n%10)
# 	n = n//10
# print(result)

# * Exercise13: Print list of step number to step number
# Step to solve:
# 1. Declare a varible to stored the result
# 2. use the loop translate the number which need to print to replace the position of number
# 3. use the loop to convert and print the result which we need
# print('Put the NUMBER need extract')
# n = int(input())
# result = ''
# while n != 0:
# 	result += str(n%10)
# 	n = n//10
# result = int(result)
# while result != 0:
# 	print(result%10, end=' - ')
# 	result = result//10

# Excercise14: Caculate the result of the equation: aX + b
# Step to solve:
# 1. declare 2 varible to get input of a and b
# print("Caculate the result of equation aX + b")
# while True:
# 	print("Put number a here")
# 	a = input()
# 	while True:
# 		if a == 0:
# 			print('Put a not equal 0')
# 			a = input()
# 		else:
# 			break
# 	print("Put number b here")
# 	b = input()
# 	try:
# 		a = int(a)
# 		b = int(b)
# 		print("Result of equation aX + b is =", -(b/a))
# 	except ValueError:
# 		try:
# 			a = float(a)
# 			b = float(b)
# 			print("Result of equation aX + b is =", -(b / a))
# 		except ValueError:
# 			print('Just allow type INTERGER and FLOAT, try again')

# Excercise15: Caculate the result of the equation: a*x**2 + b*x + c
# Step to solve: caculate the delta = b**2 - 4 * a * c
# 1. Delta == 0 : equation is solution
# 2. Delta > 0: have two solution different x1 != x2 = -(b2 + square root delta) / 2a
# 3. Delta < 0: have two solution same: x1 == x2 = -(b/2a)
# Note: import math to use the square root: math.sqrt(delta)
# import math as M
# print('Result of the equation a*x**2 + b**x + c')
# result = 0
# print('put a')
# a = input()
# print('put b')
# b = input()
# print('put c')
# c = input()
# while True:
# 	try:
# 		a = int(a)
# 		b = int(b)
# 		break
# 	except ValueError:
# 		try:
# 			a = float(a)
# 			b = float(b)
# 			break
# 		except ValueError:
# 			print('Please put number in a and b')
# 			print('put a')
# 			a = input()
# 			print('put b')
# 			b = input()
# while True:
# 	if a == 0:
# 		print('Put a not equal 0')
# 		a = int(input())
# 	elif b == 0:
# 		print('Put b not equal 0')
# 		b = int(input())
# 	try:
# 		c = int(c)
# 		break
# 	except ValueError:
# 		try:
# 			c = float(c)
# 			break
# 		except ValueError:
# 			print('Please put number in')
# 			print('put c')
# 			c = input()
# 	else:
# 		break
# print('Caculating result of the equation', a, '*x**2 +', b, '**x +', c, )
# delta = b ** 2 - 4 *( a * c)
# if delta == 0:
# 	print('Equation is have not solution  ')
# elif delta < 0:
# 	result = -(b / 2 * a)
# 	print('Equation has 2 solution same: x1 == x2 =', int(result))
# else:
# 	x1 = int(-((b + M.sqrt(delta)) / 2 * a))
# 	x2 = int(-((b - M.sqrt(delta)) / 2 ** a))
# 	print('Equation has 2 solution different:', 'x1 =', x1, 'and x2 =', x2)
