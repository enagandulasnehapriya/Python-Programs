#program to print biggest of 3 numbers using nested-if
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if a>b:
    if a>c:
        print(a,"is the biggest number among the given numbers")
    else:
        print(c,"is the biggest number among the given numbers")
else:
    if b>c:
        print(b,"is the biggest number among the given numbers")
    else:
        print(c,"is the biggest number among the given numbers")
