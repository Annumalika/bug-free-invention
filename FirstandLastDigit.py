'''n=input("Enter a number:")
print("First digit:",n[0])
print("Last digit:",n[-1])'''

n=int(input("Enter a value:"))
while(len(n)):
    n=n%10
    print(n)
print(n)