#displaying the numbers between m and n
m=int(input("enter a number:"))
n=int(input("enter another number:"))
print("the numbers between",m,"and",n,"are:")
i=m+1
while(i<n):
    print(i,end=" ")
    i+=1
