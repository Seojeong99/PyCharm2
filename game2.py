d=[]
h,w = input().split()

for i in range(int(h)-1):
    d.append([])
    for j in range(int(w)-1):
        d[i].append(0)

n = int(input())

for i in range(n):
    l,d,x,y = input().split()
    print(int(l))
    print(int(d))
    print(int(x))
    print(int(y))

d[2][3]=1

for i in range(int(h)-1):
    for j in range(int(w)-1):
        print(d[i][j],end=' ')
    print()


