pan=[]
ipan=[]
pan=[list(map(int, input().split())) for _ in range(10)]

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


for i in range(1,9):
    for j in range(1,9):
        if ipan[i][j]==0:
            pan[i][j]=9
            print("ㅇㅋ")
        else:
            i=i+1
            print("ㄴ")

i=0
j=0
for i in range(10):
    for j in range(10):
        print(pan[i][j],end=' ')
    print()
#출력하기
