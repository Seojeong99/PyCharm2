a, d, n = input().split()
x = int(a)
y = int(d)
z = int(n)
for i in range(x, z+x-1):
    x *= y

print(x)