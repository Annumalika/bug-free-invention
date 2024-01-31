a = 0
b = 1
n = int(input("Enter range:"))

print(a, end=" ")
print(b, end=" ")
for i in range(3, n+1):
    c = a + b
    a = b
    b = c
    print(c, end=" ")