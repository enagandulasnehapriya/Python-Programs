#python program to print prime numbers within the given range
min=int(input("enter a number:"))
max=int(input("enter another number:"))
for i in range(min,max+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i,end=" ")
