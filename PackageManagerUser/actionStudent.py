from PackageQLSV import data as d
def addUser():
    # Function add infor user to dict data from file data.
    # Structure of a user
    infor = {
        "id": '',
        "name": ''
    }
    idUser = input("What's ID User?")
    while True:
        checkSame = findUser(idUser)
        # Use function findUser() check same
        if checkSame != False:
            print(f"ID {idUser} was stored, please type again")
            idUser = input()
        else:
            break
    infor["id"] = idUser #Push id user into dict infor
    nameUser = input("What's NAME User?")
    infor["name"] = nameUser # Push name user into dict infor
    d.data.append(infor) # Push all infor user to Array data
    if len(d.data) != 0:
        print("T1 PASSED")
    else:
        print("T1 ERR")
def findUser(id):
    length = len(d.data)
    for i in range(0, length):
        if d.data[i]["id"] == id:
            return [i, d.data[i]]
    return False
def showUser():
    data = d.data
    print("Here is all user")
    for i in range(len(data)):
        print("[",data[i]["id"], "-", data[i]["name"], "]")
def editUser():
    print("EDIT USER FUNCTION\n"
          "What's ID USER who need to edit?")
    idUser = input()
    while True:
        checkSame = findUser(idUser)
        if checkSame != False:
            print("What's is ID? If not TYPE 0")
            idUser = input()
            if idUser == "0" or checkSame != False:
                break
            else:
                checkSame[1]["id"] = idUser
                print("What's NAME USER? If not TYPE 0")
                nameUser = input()
                if nameUser == '0':
                    break
                else:
                    checkSame[1]["name"] = nameUser
                    break
        else:
            print(f"ID {idUser} have not stored")
            break

def deleteUser():
    data = d.data
    print("DELETE FUNCTION\n"
          "What's ID User who need to delete?")
    idUser = input()
    while True:
        checkSame = findUser(idUser)
        if checkSame != False:
            print(f"Are you sure Y/N to delete user", [checkSame[1]["name"]],"?")
            confirm = input().upper()
            while True:
                if confirm == 'Y':
                    data.remove(checkSame[1])
                    break
                elif confirm == 'N':
                    break
                else:
                    print("Somethings wrong?")
                    confirm = input("Type Y/N or type /? to see docs help").upper()
            break
        else:
            print(f"ID {idUser} was not stored, please try again")
            idUser = input()




