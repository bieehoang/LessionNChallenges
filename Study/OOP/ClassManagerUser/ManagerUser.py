class User:
	__data = []

	def addUser(self):
		infor = {
			"id": "",
			"name": ""
		}
		print("ADD USER FEATURE")
		idUser = input("What's ID user?")
		while True:
			checkSame = self.findUser(idUser)
			if checkSame != False:
				print(f"ID {idUser} was stored")
				idUser = input("Type ID User again")
			else:
				break
		infor["id"] = idUser
		print("What's NAME User?")
		nameUser = input()
		infor["name"] = nameUser
		self.__data.append(infor)

	def findUser(self, id):
		data = self.__data
		for i in range(0, len(data)):
			if data[i]["id"] == id:
				return [i, data[i]]
		return False

	def showUser(self):
		"""
		Use for loop access for each value in data variable
		print index : i
		print value name: data[i]["name"]
		"""
		data = self.__data
		for i in range(0, len(self.__data)):
			print("[", data[i]["id"], data[i]["name"], "]")

	def editUser(self):
		"""
		call function findUser() to check id's user who need to edit >
		if same > edit value at indexes which function findUser returned
		"""
		data = self.__data
		idUser = input("What's ID of user who need to edit?")
		checkSame = self.findUser(idUser)
		if checkSame != False:
			print("What's ID?")
			checkSame[1]["id"] = input() #The second agruments in findUser returned
			print("What's NAME?")
			checkSame[1]["name"] = input()
			data[checkSame[0]] = checkSame[1] # the varible data is the list, checkSame[0] is the index value
		else:
			print(f"ID {idUser} is incorrect")
	
	def deleteUser(self):
		"""use for loop check the value input from user, if same with varible id from dict form > delete"""
		data = self.__data
		print("What's ID User who need to delete?")
		idUser = input()
		while True:
			checkSame = self.findUser(idUser)
			confirm = 0
			if checkSame != False:
				print(f"You will delete User {checkSame[1]['name']} has ID {idUser}?")
				print("Type 1: YES")
				print("Type 0: NO")
				confirm = int(input())
				if confirm == 1:
					# print(data[checkSame[0]])  The infor of user who need delete
					data.remove(data[checkSame[0]])
					print(f"User has ID {idUser} had removed")
					break
				# data.remove(checkSame[0])
				elif confirm == 0:
					break
			else:
				print(f"ID {idUser} have not stored, please try again")
				break
		