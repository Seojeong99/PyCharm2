n = int(input())
a = input().split()

for i in range(n):
     a[i] = int(a[i])

min = a[0]
for i in range(1,n-1):
        if a[i]<a[i+1]:
            if a[i]<min:
                min = a[i]
        else:
            if a[i+1]<min:
                min = a[i+1]


print(min)
#d=[]
#for i in range(24):
#    d.append(0)

#for i in range(n):
#    d[a[i]]+=1

#for i in range(1,24):
#    print(d[i],end=' ')
