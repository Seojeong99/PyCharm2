pan=[]
h, w = input().split() #세로, 가로
n = int(input())#막대 개수

for i in range(int(h)):
    pan.append([])
    for j in range(int(w)):
        pan[i].append(0)

i=0
for i in range(int(n)):
    l, d, x, y = input().split()#길이,방향,좌표
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)

    if int(d)==0:
        for z in range(l):
            pan[x - 1][y + z - 1]=1
            z = 0


    else:
        for z in range(l):
            pan[x + z - 1][y - 1] = 1
            z = 0
i=0
j=0

for i in range(int(h)):
    for j in range(int(w)):
        print(pan[i][j],end=' ')
    print()

