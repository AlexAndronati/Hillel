
S = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4
temp = len(S)//w
temp2 = len(S)%w
for i in range(temp+1):
    print(S[w*i:w*(i+1)])
