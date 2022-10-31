import QLSV.data as d
err = "SOMETHING WAS WRONG"

def addStudents():
	"""Function to add infor of user to student ( dict ), then add to data ( list )"""
	infor = {
		"id": '',
		"name": ''
	}
	while True:
		print("What is id's student?")
		idStudent = input()
		student = findStudent(idStudent)
		if student != False:
			print("Students was stored")
			idStudent = input("What's ID student?")
		else:
			break
	infor["id"] = idStudent
	print("What is infor student?")
	infor["name"] = input()
	d.data.append(infor)
	# if d.data != []:
	# 	print("FEATURE 1 PASSED")
	# else:
	# 	print(err)
def findStudent(id):
	data = d.data
	length = len(data)
	for i in range(0, length):
		if data[i]["id"] == id:
			return [i, data[i]]
	return False

def showStudent():
	data = d.data
	length = len(data)
	for i in range(0, length):
		print(f"[",data[i]["id"], data[i]["name"],"]")


def editStudent():
	print("What is id's user you want to edit")
	id = input()
	student = findStudent(id)
	if student == False:
		print(f"id {id} haven't stored")
	else:
		print("What would you want to change")
		print("Id?")
		student[1]["id"] = input()
		print("Name?")
		student[1]["name"] = input()
		d.data[student[0]] = student[1]
		
def deleteUser():
	print("DELETE INFOR'S USER FEATURE")
	idUser = input("What's ID user who need to delete?")
	while True:
		checkSame = findStudent(idUser)
		if checkSame == False:
			print(f"Something was wrong, please try again")
			idUser = input()
		else:
			break
	d.data.remove(checkSame[1])
	print(f"USER HAVE ID {idUser} was deleted")
		