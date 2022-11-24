#python program to check whether a given number is palindrome or not
n=int(input("enter a number:"))
pal=n
rev=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
if pal==rev:
    print(pal,"is a palindrome number")
else:
    print(pal,"is not a palindrome number")
