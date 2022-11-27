flag= '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽'
#print(flag.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))
for i in range(0, len(flag), 2):
    print(chr(flag[i] << 8))
    print(ord(flag[i + 1]))
    #print(i.decode('utf-8'))
#open('enc').read().decode('utf-8').split()
#for i in range(0, len(flag)):
#    ans = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]) 
#print(ans)
#for i in range(0,len(flag)):
#    num_ord += ord(flag[i])
#    chr_from_ord += chr(num_ord)
#    print(chr(ord(flag[i])>>8), end="")
#    print(chr(int(bin(ord(flag[i]))[9:], 2)),end="")
#print(chr_from_ord)
