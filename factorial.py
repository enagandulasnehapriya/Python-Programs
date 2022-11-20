#printing the factorial of a given number
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("the factorial of the given number is:",fact)
