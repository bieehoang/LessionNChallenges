# Import class ManageUser to use function manage user
import ManagerUser

start = ManagerUser.User()
action = 0
while action >= 0:
	if action == 1:
		start.addUser()
	elif action == 2:
		start.showUser()
	elif action == 3:
		start.editUser()
	elif action == 4:
		start.deleteUser()
	print("Type NUMBER same with funtion here")
	print("0: Escape program")
	print("1: Add User")
	print("2: Show list user")
	print("3: Edit infor user")
	print("4: Delete user")
	action = int(input())
	if action == 0:
		break
