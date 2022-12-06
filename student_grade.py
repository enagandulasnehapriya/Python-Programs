m1=int(input("Enter sub1 marks"))
m2=int(input("Enter sub2 marks"))
m3=int(input("Enter sub3 marks"))
total=0
avg=0.0
if(m1>=35 and m2>=35 and m3>=35):
    total=m1+m2+m3
    avg=total/3.0
    if avg>=70:
        print("DISTINCTION")
    elif avg>=60 and avg<=70:
        print("FIRST CLASS")
    else:
        print("PROMOTED")
else:
    print("ohh Sorry You are FAILED....Better Luck Next Time")
