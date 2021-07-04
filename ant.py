global i
pan=[]
ipan=[]
pan=[list(map(int, input().split())) for _ in range(10)]

def check(i,j):
    while (ipan[i][j] == 0):
        pan[i][j] = 9
        j = j + 1
    print(i, j)
    return i,j

for i in range(9):
    ipan.append([])
    for j in range(9):
        ipan[i].append(0)

print(pan)
for i in range(9):
    for j in range(9):
       ipan[i][j]=int(pan[i][j])

for i in range(9):
    for j in range(9):
        print(ipan[i][j],end=' ')
    print()

#배열에 넣기

x,y=check(1,1)
a,b=check(x+1,y-1)
c,d=check(a+1,b-1)
e,f=check(c+1,d-1)
g,h=check(e+1,f-1)
i,j=check(g+1,h-1)
k,l=check(i+1,j-1)





for i in range(10):
    for j in range(10):
        print(pan[i][j],end=' ')
    print()
#출력하기


