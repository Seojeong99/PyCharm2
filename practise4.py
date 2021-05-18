a, m, d, n = input().split()
x = int(a)
y = int(m)
z = int(d)
k = int(n)
for i in range(x, k+x-1):
    x=i*y+z


print(x)
