#sum of the digits of the given number
n=int(input("enter a number:"))
sum=0
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
print("sum of digits of",n,"is:",sum)
