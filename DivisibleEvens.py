N=int(input("Enter the size of array:"))
k=int(input("enter number:"))
sum=0
for i in range(N):
    a=list(map(int,input("Enter values:").split()))

    for n in a:
        if(n%2==0 and n%k==0):
            sum+=n
print(sum)
