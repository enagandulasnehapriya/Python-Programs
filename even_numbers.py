#printing even numbers from m to n
m=int(input("enter a number:"))
n=int(input("enter another number:"))
print("the even numbers from",m,"to",n,"are:")
i=m
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i=i+1
        
