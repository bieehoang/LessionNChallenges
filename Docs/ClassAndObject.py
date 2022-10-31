# # Study about module, import, reload ( import reload from reloadlib ), dir(), print(help('modules'))
# # print(help('modules'))
#
# # from Game.Sound import music
# # n = input("Put something in here")
# # music.startMusic(n)
# # Study about package: know about package, function, define package in package and how to access inside
#
# # CLASS: OOP ( object oriented programming )
# # Have 2 main element: form adj and action, instance:
# # When class A is inherited value from class B, saying class A is child envelope and class B is father envelope
# # father envelope
# # class User:
# # 	name: ''
# # 	age: ''
# # 	def __init__(self,name,age):
# # 		self.name = name
# # 		self.age = age
# # 	def eat(self):
# # 		print("Eat")
# # 	def sleep(self):
# # 		print("Sleep")
# # 	def show(self):
# # 		print(self.name)
# # 		print(self.age)
# # class Student(User):
# # 	def study(self):
# # 		print("Study")
# # #inherted
# # us1 = Student("Daniel", 19)
# # us1.show()
# # us1.study()
#
# # Inherited between children element and father element, from children can access all adj and method from
# # father element. Except can not access if the level of this is private.
# # class Xe:
# # 	model : ''
# # 	def action(self, name):
# # 		self.name = name
# # 		print(self.name)
# # class Cycle(Xe):
# # 	def CAction(self, model):
# # 		self.model = model
# # 		self.action("Start")
# # 		print(self.model)
# # a = Cycle()
# # a.CAction(192)
#
# # class A:
# # 	def a1(self):
# # 		print("A1 public")
# # 	def _a1(self):
# # 		print("A1 protected")
# # 	def __a1(self):
# # 		print("A1 private")
# #
# # class B(A):
# # 	def b1(self):
# # 		print("B1 public")
# # 	def _b1(self):
# # 		print("B1 protected")
# # 	def __b1(self):
# # 		print("B1 private")
# #
# # class C(B):
# # 	def start(self):
# # 		self.b1()
# # start = C()
# # start.start()
# # startPrivate =B()
#
# # shutdown and restart by python code.
# # import os
# # put = input("Put here")
# # if put == 'shutdown':
# # 	os.system("shutdown /s /t 0")
# # elif put == 'restart':
# # 	os.system("restart /r /t 0")
#
# # getter and setter in python:
# # getter: its method to access the element of class
# # setter: is method to define the value of element of class
# # in fact can access and define value of class like this:
# # class User:
# # 	__name: ''
# # 	@property
# # 	def nameUser(self):
# # 		return self.__name
# # 	@nameUser.setter
# # 	def nameUser(self, name):
# # 		self.__name = name
# # class userOne(User):
# # 	global __age
# # 	User.__name = __age
# # 	def nameUser(self, age):
# # 		self.__age = age
# #
# # class userTwo(User)
# # check = userOne()
# # check.nameUser = "daniel"
#
# #OVERRIDE: This is acction to edit value of element or function of father class in children class
# # class Animal:
# # 	__name: ''
# # 	def __int__(self, name):
# # 		self.__name = name
# # 	def move(self):
# # 		pass
# # class dog(Animal):
# # 	def show(self):
# # 		Animal.move(self)
# # 		print()
# # class duck(Animal):
# # 	def move(self):
# # 		print("Duck move by two foots")
#
# # Interface
# # a = int(input())
# # b = int(input())
# # c = a + b
# # print("a + b = {0}".format(c))
# # Exercise: solve the information about student, to add, delete, show, and edit by type module

#
#
