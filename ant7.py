global i
pan=[]
ipan=[]
pan=[list(map(int, input().split())) for _ in range(10)]

#핵심으로 이동하는 친구,,
def check(i,j):
    while (ipan[i][j] == 0):
        pan[i][j] = 9
        j = j + 1
        if(j==9):break
    #print(i,j)
    return i+1,j-1

#def check2(i,j):
#   if(pan[i-1][j]==9):
#       pan[i][j]=9
#   elif(pan[i][j-1]==9):
#       pan[i][j]=9

#배열 만들어주는 친구
for i in range(9):
    ipan.append([])
    for j in range(9):
        ipan[i].append(0)

#배열 int로 전환해주는 친구
for i in range(9):
    for j in range(9):
       ipan[i][j]=int(pan[i][j])


#배열에 넣기


x,y=check(1,1)
a,b=check(x,y)
c,d=check(a,b)
e,f=check(c,d)
g,h=check(e,f)
i,j=check(g,h)
k,l=check(i,j)


if(l+2<9):
    pan[k-2][l+2]=9
else:
    z, z2 = check(k, l)


for i in range(10):
    for j in range(10):
       # if(pan[i][j]==2):
       #     check2(i,j)
        print(pan[i][j],end=' ')
    print()



