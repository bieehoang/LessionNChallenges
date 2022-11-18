flag= '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽'
#print(data.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))
#for i in data:
    #print(i)
    #print(i.decode('utf-8'))
    #print(chr(i))
#open('enc').read().decode('utf-8').split()
for i in range(0,len(flag)):
    print(chr(ord(flag[i])>>8), end="")
    print(chr(int(bin(ord(flag[i]))[9:], 2)),end="")
