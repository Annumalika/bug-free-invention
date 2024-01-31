n = int(input("Enter a Number: "))
ref = n
r = 0
s = 0
if n > 9 and n < 100:
    while(n > 0):
        r = n % 10
        s = r ** 2 + s
        n = n // 10
    if ref == s:
        print("Armstrong")
    else:
        print("Not an Armstrong")
else:
    while(n > 0):
        r = n % 10
        s = r ** 3 + s
        n = n // 10
    if ref == s:
        print("Armstrong")
    else:
        print("Not an Armstrong")