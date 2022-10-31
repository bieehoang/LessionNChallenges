# First, lets me explain some key symbols
# //: End of an unit concept
# * Concept important in unit
# ** Concept very important, often use when go to work
# /?: Continuing update
# -- LET'S STARTED --

iterator = ["Iterator"]
# * Learn about Iterator method: can use it method replace to for, while loop
# An iterator is an object which implement iterator protocol, it's consist iter() method and next() method
# need remember differentiate between iterator and iterable object:
# - Iterator is an object which implement iterator protocol
# - Iterable object is type object which can access value from, like: string, list, tuple, set.
# + use method iter() to made it to iterator, then use next() method to access for each value
# setObj = {1, 3, 4, "biee", 0, -1}
# listObj = [1, 3, 4, "biee", 0, -1]
# strObj = 'this is doc text'
# tupleObj = (1, 3, 4, "biee", 0, -1)
# Use for loop to access for each value of var word;
# for i in range(0, len(listObj)):
# 	print(tupleObj[i])
# made iterable object to iterator:
# iword = iter(setObj)
# for i in range(0, len(setObj)):
# 	print(next(iword))
# create iterator myself: need declare __iter__() method, and __next__() method, in this:
# - __iter__(): return at main object of this class
# - __next__(): return at next value of this object in list, ex:
# ** StopIterator: regular expression to prevent indexes go out indexes of variable
# class myNumber:
#     def __init__(self, number):
#         self.number = number
#
#     def __iter__(self):
#         self.a = 2
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 2
#         while True:
#             if x < self.number:
#                 return x
#             else:
#                 StopIteration
#
#
# start = myNumber(11)
# iNumb = iter(start)
# print(iNumb)
# for i in range(0, start.number):
#     print(next(iNumb))
# This is about share-exp about Iterator in Python, wish you study better!
# //

generator = ["generator"]
# * Learn about GENERATOR: It is way to create paradigm Iterator, by using keyword "yield"
# Generator can consist one or more than one key word yield
# Method __iter__() and __next__() is created auto, so can use next() method without use next() method before
# Value of each variable is stored between for each time call it.
# When func finish, StopIteration will execute > show iterator allow the last value.
# def myNumber(n):
#     n = 1
#     print(n)
#     yield n
#     n += 1
#     print(n)
#     yield n
#     n += 1
#     print(n)
#     yield n
# test = myNumber(1)
# print(test) # show what type of this object
# next(test) # return value at first yield
# next(test) # return value at second yield
# next(test) # return value at third yield
# >> Value n was stored after for each time return it ( yield )
# Exercise:
# Create a list
# my_list = [1, 3, 6, 10]
# Required: return the squared root of for each value in this list
# for i in my_list:
#     print(i**2)
# Another way, use Generator to solve this exercise
# def sqrtList(list):
#     for item in list:
#         yield item
# start = sqrtList(my_list)
# for i in start:
#     print(i**2)
# class Luythua:
# 	def __init__(self, number, time_count):
# 		self.number = number  # Ham luy thua can tinh, vd: Luythua2, luythua3....
# 		self.time_count = time_count  # so lan tinh cua ham, vd 3: tinh 3 lan tinh cua luythua so 2
# 		self.n = 0  # Thuoc tinh luu so cua luy thua hien tai
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self.n >= self.time_count:
# 			return StopIteration
# 		else:
# 			result = self.number ** self.n
# 			self.n += 1
# 			return result
# start = Luythua(2,5)
# for i in range(0, start.time_count):
# 	print(next(start))
# Use form Generator to create a func to calculator quintillion, the value same with the function upper.
# def quintillion(number, countNumber):
# 	count = 0
# 	while StopIteration:
# 		if count < countNumber:
# 			value = number ** count
# 			yield value
# 			count += 1
# 		else:
# 			return StopIteration
#
# start = quintillion(2,12)
# for i in start:
# 	print(i)
# print(next(start))

# This is example to use concept Iterator to calculate quintillion
# for i in range(0, len(start))
# ** Example about Recursive - Algorithm
# def giaithua(n):
#     """Đây là hàm tính giai thừa của một số nguyên by Quantrimang.com"""
#     if n == 1:
#         return 1
#     else:
#         return (n * giaithua(n-1))
# * Calculate LuyThua cua 1 so.
# num = num1 = int(input("Nhập số cần tính giai thừa: "))
# print("Giai thừa của", num, "là", giaithua(num))
# print(giaithua(4))
# """Lần gọi 1: n = 4: return 4 * giaithua (3)
#     Lần gọi 2: n = 3: return 3 * giaithua(2)
#     lần gọi 3: n = 2: return 2 * giaithua(1)
#     lần gọi 4: n = 1: return 1
#     Trả về của lần gọi 4: 1 > return 1
#     Trả về của lần gọi 3: 2 * 1 # 1 từ hàm giaithua(1) > return 2
#     Trả về của lần gọi 2: 3 * 2 # Kết quả từ lần gọi 3: 2 * 1 > return 6
#     Trả về của lần gọi 1: 4 * 6 # Kết quả từ lần gọi 2: 3 * 2 > return 24
#     """

# import calendar
# year = 2022
# month = 1
# print(calendar.month(year, month))

listComprehension = ["list comprehension"]
# Learn about concept List comprehension,78
# Concept: it is way to create a new list data from a old list data, with a condition detail.
# * Form:
# newList = [ expression for item in iterable if condition == True ], in this:
# expression: data set have returned
# iterable: data set iterable, which is old list provide value to expression value
# condition: the condition to select value expression from iterable, if True > return expression
# Example:
# listData = [1, 3, 4, 5, 6, 6, 23, 423, 4, 234, 2, 3]
# newList = [x for x in listData if x % 2 == 0]
# Another way:
# newList = []
# for i in listData:
#     if i % 2 == 0:
#         newList.append(i)
# print(newList)
# * Exercise: Create list prime number from a list have declared
# Step: Declare a function to check number is Prime
# Use list comprehension to create newList
# data = [1, 2, 3, 5, 45, 46, 5, 6, 76, ]
#
# def isPrime(numb):
#     if numb <= 2:
#         return False
#     elif numb % 2 == 0:
#         return False
#     else:
#         for i in range(3, numb, 2):
#             if numb % i == 0:
#                 return False
#     return True
#
# newData = [nValue for nValue in data if isPrime(nValue)]
# print(newData)

closureFunc = ["closure function"]
# Understand 2 concept: nested function and non-global variable BEFORE study about closure Function
# 1. What is nested function and non-global variable?
# Nested function: is concept about 2 function nested
# Non-global variable: had declared at func bigger, so the nested func can use it, but can not change or edit
# def func(msg):
#     # this is bigger variable
#     numb = 2
#
#     def func2():
#         # here is nested function
#         print(msg)
#         # numb +=2 # non-global variable can not be change, Will return Error
#
#     return func2


# Inside func function have 1 nested function and was called it which name is func2
# start = func("bieehoang")
# start()  # bieehoangg
# start2 = func("daniel")
# start2()

# value of non-global variable was stored each time variable which call func2  > closure func
# profit: use closure func change with OOP ( object-oriented programming ), ex:
# ** Exercise: calculate result square root of a number:
# * Solve with Class:
# class sqrtNumb:
#     def __init__(self, number):
#         self.number = number
#     def cal(self, x):
#         return self.number**x
# cal= sqrtNumb(2)
# print(cal.cal(2)) # 2^2 = 4
# * Solve with Closure Function
# def sqrtNumb(numb):
#     # main number
#     def cal(x):
#         # the number upper.
#         return numb ** x
#     return cal
#
#
# start = sqrtNumb(2) # 2
# print(start(4)) # 2 exponent 4

higherOrderFunc = ['higher order function']
# **Characteristics of Higher Order Function:
# * Can assign for a variable
# def biggerFunc(func, mes):
#     print(func(mes))
# def func(mes):
#     return mes + "testing"
# # assign with a variable
# test = func
# biggerFunc(test, 'daniel')
# * Return a function
# ** Closure function
# * Decorator function
# apply both characteristics of higher order function to it:
# def decor(func): # have agrument is a function
#     def pattern():
#         print("**********************")
#         func()
#         print("**********************")
#     return pattern # return a function
# def myFunc():
#     print("test")
# test = decor(myFunc) # can asign with variable
# test()

decoratorFunction = ['decorator function']
# it is how to change behavior of an object callable without redesign it, decoratorFunc has mission cover
# about of other func, so we can decor the up line and end line inside of other func
# def decor(func):  # decorator func
#     # agrument is func which need to design
#     def patternt(n):
#         print("*****************")
#         func(n)
#         print('')
#         print("*****************")
#
#     return patternt
#     # nested function


# def warrning(func):
#     def wrapp(n):
#         print("//// warning ////")
#         func(n)
#         print('')
#         print("//// warning ////")
#
#     return wrapp


# @decor
# @warrning  # multi decorator function
# def getNumb(n):  # decor func if func has argument
#     for i in range(0, n):
#         print(i, end=' ')
#
#
# getNumb(10)


# of course can decorator function with class, MUST REQUIRED METHOD __call__, if not func will false
# class decoratorFunc:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, value):
#         print("// Warning //")
#         self.func(value)
#         print("")
#         print("// Warning //")
# @decoratorFunc
# def getNumb(n):  # decor func if func has argument
#     for i in range(0, n):
#         print(i, end=' ')
#
# getNumb(10)

solveFileAndDir = ['solve file and directory']
# File is where user can handle with it, open, write, save, copy .... , it is
# always stored at disk drive, unless disk drive was broken or file was deleted.
# ** with python, in workflow support 3 method to:
# Note: with python, 'a' character is not 92 in ASCII code, so need to define before
# > 'cp1252' with Windows, 'utf-8' with Linux

# 1. open(): use to open file
# * Form: var = open("name file", "mode", encoding='type')
# **f = open('file.txt', 'w', encoding='utf-8') # open file.txt, with mode 'w', create new if have not stored,
# else: override if have stored

# 2. close(): after open file and write file, always need to close file
# * use close() func after line open file # in case open file was error, close() func can not execute
# > use keyword 'with'
# ** with open('file.txt', mode= 'a', encoding = 'utf-8') as f # open file.txt, open file and write at end line before
# create new if file have not stored.
# open file.txt,  with mode 'mode', type encoding='type', and then auto close file although if have problem

# 3. write()
