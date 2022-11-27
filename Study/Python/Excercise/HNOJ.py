"""NOTE: To see all part of this unit, type shortcut Ctrl + A to select all characters,
    then type shortcut Ctrl + Shift + '-': to compact.
"""
from math import floor

"""Nhập liên tục vào một số nguyên,
đến khi số lượng số chẵn bằng số lượng số lẻ thì dừng lại và in ra số lượng của chúng.
# Input: Gồm nhiều dòng, mỗi dòng chứa một số nguyên
# Output: In ra số lượng số chẵn hoặc số lẻ"""

ex1 = 'Find odd all odd number form users input'
# Start:
# data = []
# oddNumb = []
# def start():
#     while True:
#         try:
#             numb = int(input())
#         except ValueError:
#             numb = int(input())
#         data.append(numb)
#         for i in data:
#             for j in range(i, len(data) + 1):
#                 if i % 2 == 0 and j != i:
#                     oddNumb.append(i)
#                     print(len(oddNumb))
#                     break
# start()

ex2 = 'Print status of the light bubble when on or off'
# Print type of button light bubble
# nLights = int(input("How many light bubble?"))
# nAction = int(input("How many time you change the switch?"))
#
#
# def displayBublight(a, b):
#     x = 0
#     result = []
#     if b % 2 == 0:
#         a = 0
#         result.append(a)
#     else:
#         a = 1
#         result.append(a)
#     for i in range(nLights-1):
#         if a == 0:
#             x = 1
#         result.append(x)
#     print(result)
#
# displayBublight(nLights,nAction)

ex3 = 'find indexes of the number which is add them is equal with target.'
# Cho 1 list, and a value is target. Find for each value in list the value if add both it is equal target. And
# return index of this value in list.

# def Solution(list, target):
# # CASE SOVLE 1
#     result = []
#     for i in list:
#         for j in list:
#          # print(i, j)
#             if i + j == 9:
#              # print(i,j)
#                 result.append(i)
#                 result.append(j)
#                 break
#         break
#     return [list.index(result[0]),list.index(result[1])]
# print(Solution([2,7,11,15],9))
#
# algothrm_lin_search = 'linear search'
# ** Linear search: find index of target value in

algothrm_bin_search = 'binary search'
# ** Binary Search: A list was sorted: i1 < i2 < i.n. Find the index of which value target
# list = [1,3,6,52,56,66,75,123]
# target = 75
# from math import floor as f
# def Solution(list, target):
#     l = 0
#     r = len(list)
#     while l < r:
#         mid = f((l+r)/2)
#         print(mid)
#         if list[mid] == target:
#             print("***",list[mid])
#             return list[mid]
#         elif list[mid] > target:
#             r = mid + 1
#         elif list[mid] < target:
#             l = mid - 1
#     else:
#         print(f"{target} had not stored")
# Solution(list,target)

algothrm_recursion = 'About RECURSION - lifo'
# # ** About RECURSION - lifo:
# def recursion(n):
#     if n > 0:
#         result = n + recursion(n - 1)
#         # print(result)
#     else:
#         result = 0
#     return result
#
#
# check = recursion(3)
# print(check)

algothrm_dfs = 'DFS - Depth First Search'
# ** DFS - Depth First Search
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#
#     print(start)
#
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
#
# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}
#
# dfs(graph, '0')
#
#
# print(None)

cal_time = "Calculate time after add minutes"
# ** Calculate time after add minutes
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# # Write your code here.
# hour += (mins + dura)// 60
# mins = (mins + dura) % 60
# if hour > 23:
#     hour =  hour%24
# print("result", hour, mins)
#

cal_tax = "Calculate tax from citizen's income."
# ** Calculate tax from citizen's income.
# income = float(input("Enter the annual income: "))
# cent = 1 / 32  # 1 thaler == 32 cent
# tax = ((income * 18) / 100) - 556 - (2 * cent)  # basic: lesser 85,528 thales
# if tax <= 0:
#     tax = 0
# elif income > 85528:  # if income larger 85,528
#     surplus = income - 85528  # surplus over 85,528 thalers
#     tax = ((surplus * 32) / 100) + 14839 + (2 * cent)
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# ** Stored and print the largest number from input's user:
# larg_numb = -9999999999999999999999999
# list_numb = []
# inp_user = input("Put number here\n Type \"S\" to end and get result\n")
# esc = "s"
# try:
#     while int(inp_user) != esc.upper():
#         if larg_numb < int(inp_user):
#             larg_numb = int(inp_user)
#             list_numb.append(larg_numb)
#         inp_user = input("Put number here\n Type \"S\" to end and get result\n")
# except ValueError:
#     print("The largest number:", larg_numb)
 
# ** Find the answer of magican:
# key = 777
# user_inp = int(input("Put number here"))
# while True:
#     if user_inp == key:
#         print("Successful")
#         break
#     else:
#         print("So close")
#         user_inp = int(input("Put number here"))
doc = """What happens when an IF statement has a false condition?
In an if...else statement, if the code in the parenthesis of the if statement is true, 
the code inside its brackets is executed. But if the statement inside the parenthesis is false, 
all the code within the else statement's brackets is executed instead"""
# count = -1
# print(count == False)
# if count:
#     print("value: true")
# else:
#     print("value: false")


# Normal:
# blocks = int(input("How's many block do you have?"))
# height = 0
# count = 0
# # start = ''
# while count < blocks: # while count's value lesser blocks value
#     blocks -= 1 # minus 1 each time execute: reduce value each time run
#     height += 1 # add 1 each time execute
#     count += height # count
#     # start += '*'*height+'\n'
# # print("The paramid:\n", start)
# print("The height of the paramid:\n", height)
# blocks = int(input("How's many block do you have?"))
# height = []
# stack = 0
# for i in range(1, blocks+1):
#     count = blocks
#     count -= i
#     stack += i
#     height.append(i)
#     if count <= stack:
#         break
# print("The height of the pyramid:", len(height))


# ** Lothar Collatz algorithm
# c2 = int(input("Put number here"))
# steps = 0
# while c2 != 1:
#     if c2 % 2 == 0:
#         c2 /= 2
#     else:
#         c2 = 3 * c2 +1
#     print(int(c2))
#     steps += 1
# print("Steps:", steps)

# """
# Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits, replace each 0 with x,
# and print the modified string to the screen. Use the skeleton below:
# """
# result = ''
# for i in "0165031806510":
#     if i == "0":
#         print('x', end='')
#     print(i, end='')


# # step 1
# beatles = []
# print("Step 1:", beatles)
#
# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)
#
# # step 3
# for i in beatles:
#     # usr = input("Did you append Stu Sutcliff and Pete Best?1")
#     usr_rq1 = 'Stu Sutcliffe'
#     usr_rq2 = "Pete Best"
#     # if usr == usr_rq1:
#     #     beatles.append(usr)
#     # elif usr == usr_rq2:
#     #     beatles.append(usr)
#     while True:
#         usr = input("Did you append Stu Sutcliff and Pete Best?2")
#         if usr == usr_rq1:
#             beatles.append(usr)
#         elif usr == usr_rq2:
#             beatles.append(usr)
#         print(beatles)
#         if usr_rq1 and usr_rq2 in beatles:
#             break
# print("Step 3:", beatles)
#
# # step 4
# del beatles[-1], beatles[-2]
# print("Step 4:", beatles)
#
# # step 5
# beatles.insert(0, "Ringo Start")
# print("Step 5:", beatles)
#
#
# # testing list legth
# print("The Fab", len(beatles))

# m = [1,2,3]
# print(m[1]) # 1
# print(m[1]) # 2
# print(m[2]) # 3
# for i in range(len(m)):
#     print(i)
#     # print(m[i])
#     m.insert(1, m[i])
# print(m)
#
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")
#
# a = 1
# b = 0
# c = a & b
# d =a | b
# e = a ^ b
# print(c + d + e)
#l = [1,3,4,5,6]
#print(l[-3:2])

# Example of Class, OOP and the way to override method of parent class in children class
#class Rectangle:
#   def __init__(self, length, width):
#      self.length = length
#      self.width = width
#    def area(self): 
#         return self.length * self.width
#class Square(Rectangle):
#    def __init__(self, length):
#        super().__init__(length, length)
#s = Square(2)
#print(s.area())

algothrm_insertionsort = ["Insertion-sort algorithm"]
#** Insection sort: This is the algothrm same with sort the wild card when playing
#def insertionSortAlgothrm(arr):
#    for i in range(0, len(arr)):
#            key = arr[i] #
#            j = i + 1
#            while j >= 0 and arr[j] < key:
#                arr[j] = arr[i]
#                j -= 1
#                # print(j)
#            arr[j -1] = key
#            print(key)
#            print(arr)
#arr = [12,4,23,1,5]
#insertionSortAlgothrm(arr)
#print(arr)
#

"""Initially, the zoo have a single chick. A chick gives birth to 2 chicks every day and
 the life expectancy of a chick is 6 days. Zoo officials want to buy food for chicks so 
 they want to know the number of chicks on an Nth day. 
"""

def findOpposite(n, nInput):
#    distantA = []
#    distantB = []
    lengthN = []
    for i in range(0, n+1):
        lengthN.append(i)
    print(lengthN)
    cut = int(n/2)
    distantA = list(lengthN[0:cut+1])
    distantB = lengthN[cut+1:]
    print(distantA,distantB)
    if nInput > n:
        print(f'{nInput} is not in list\nPlease try again')
        exit()
    if nInput in distantA:
        for i in distantA:
            if i == nInput:
                print('Opposite of', distantA[i],'is', distantB[i])
    elif nInput in distantB:
        for i in distantB:
            if i == nInput:
                print(i)
                print('Opposite of', distantB[distantB.index(i)],'is ', distantA[distantB.index(i)])
    else:
        print(f'{nInput} was wrong')

findOpposite(7,6)
