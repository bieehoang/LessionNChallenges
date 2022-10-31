from PackageManagerUser import actionStudent as s # Import module manager user with Package
action = 0
while action >= 0:
	if action == 1:
		s.addUser()
	elif action == 2:
		s.showUser()
	elif action == 3:
		s.editUser()
	elif action == 4:
		s.deleteUser()
	print("1: Add student")
	print("2: show student")
	print("3: edit student")
	print("4: delete student")
	print("0: Escape feature")
	action = int(input())
	if action == 0:
		break