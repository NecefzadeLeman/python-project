from email import feedparser
from termios import B0, B921600
from time import daylight
from xml.sax.handler import all_properties


a=int(input("Enter number1"))
b=int(input("Enter number2"))
if a>b:
    print(a, "is greater")
elif b>a:
    print(b, "is greater")
else:
    print("Numbers are equal")



n=int(input("Enter the number"))
if n>0:
    print("Number is positive")
elif n<0:
    print("Number is negative")
else:
    print("Number is zero")




n=int(input("Enter the number"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")
    




n=int(input("Enter the exam score"))
if n<0:
    print("invalid score")
elif n>100:
    print("invalid score")
elif n>=91:
    print("A")
elif n>=81:
    print("B")
elif n>=71:
    print("C")
elif n>=61:
    print("D")
elif n>=51:
    print("E")
else:
    print("F")




num1=int(input("Eded daxil edin"))
num2=int(input("Eded daxil edin"))
num3=int(input("Eded daxil edin"))
if num1>num2 and num1>num3:
    print(num1, "is greater")
elif num2>num1 and num2>num3:
    print(num2, "is greater")
else:
    print(num3, "is greater")




num1 = float(input("Enter the number: "))
num2 = float(input("Enter the number: "))
op = input("Enter an operation (+, -, *, /, %, **, //): ")

match op:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)

    case "/":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 / num2)

    case "%":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 % num2)

    case "**":
        if num1 == 0 and num2 < 0:
            print("Error: Zero cannot be raised to a negative power")
        elif num1 < 0 and num2 != int(num2):
            print("Error: Negative base with non-integer power")
        else:
            print(num1 ** num2)

    case "//":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 // num2)

    case _:
        print("Invalid operation")





age=int(input("Enter the age"))
if age<0:
    print("invalid age")
elif age<=12:
    print("Child")
elif age<=17:
    print("Teenager")               
elif age<=64
    print("Adult")
else:
    print("Senior")







price=float(input("AlIs veris meblegini daxil edin"))
if price<0:
    print("Invalid price")
elif price<100:
    print("Endirim yoxdur", "Yekun qiymet=", price)
elif price<300:
    a=price*0.10
    b=price-a
    print(price, "Endirim qiymeti=", a, "Yekun qiymet=", b)
elif price<500:
    a=price*0.15
    b=price-a
    print(price, "Endirim qiymeti=", a, "Yekun qiymet=", b)
else:
    a=price*0.20
    b=price-a
    print(price, "Endirim qiymeti=", a, "yekun qiymet=", b)






a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
if a<b and a<c:
    if b<c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b<a and b<c:
    if a<c: 
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a<b:
        print(c, a, b)
    else:
        print(c, b, a)






Balance=1000
mebleg=float(input("Enter the number"))
if mebleg<=0:
    print("invalid amount")
elif mebleg>1000:
    print("insufficient balance")
else:
    n=1000-mebleg
    print("remaining balance=", n)






energy=float(input("Enerji serfiyyatInI daxil edin"))
if energy<0:
    print("invalid energy")
else:
    if energy<=100:
        q=0.08
    elif energy<=300:
        q=0.12
    else:
        q=0.15
    M=q*energy
    print(energy, q, M)






    distance=float(input("Enter the distance (km)"))
    n=2 
    if distance<0:
        print("invalid distance")
    elif distance<=5:
        a=distance*0.70
    elif distance<15:
        a=distance*0.60
    else:
        a=distance*0.50
    c=a+n
    print("starting fee", n, "distance fee", a, "total fee", c)







    age=int(input("Enter the age"))
    salary=float(input("Enter the monthly salary"))
    amount=float(input())
    if age<0:
        print("Invalid input:Age cannot be negative")
    else:
        if salary<0:
           print("Invalid input:Salary cannot be negative")
        else:
            if amount<=0:
                print("Invalid input:Amount cannot be negative and zero")
            else:
                if age<18:
                    print("Rejected:Age below 18")
                else:
                    if salary<500:
                        print("Rejected:Salary below 500")
                    else:
                        if amount>salary*10:
                            print("Rejected:Requested exceeds 10 times the salary")
                        else:
                            print("Approved")
                        






a = float(input("Enter the side"))
b = float(input("Enter the side"))
c = float(input("Enter the side"))

if a <= 0:
    print("Triangle cannot be created")
elif b <= 0:
    print("Triangle cannot be created")
elif c <= 0:
    print("Triangle cannot be created")
else:
    if a + b > c:
        if a + c > b:
            if b + c > a:
                if a == b:
                    if b == c:
                        print("Equilateral")
                    else:
                        print("Isosceles")
                elif a == c:
                    print("Isosceles")
                elif b == c:
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Triangle cannot be created")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")







score=int(input("Enter the score"))
school=int(input("Enter the school note"))
age=int(input("Enter the age"))
if age<0:
    print("Rejected, Age cannot be negative")
elif score<0 and sore>700:
    print("Rejected, Score is between 0-700")
elif school<0 and school>100:
    print("Rejected, School is between 0-100")
elif age<16:
    print("Reected, Age is below 16")
else:
    if score>=600:
        print("scholarship, Score is between 600-700")
    elif score>=450:
        print("Accepted, Score is between 450-599")
    elif score>300:
        if school>=80:
            print("Accepted, Score is 300-449 and school is 80-100")
        else:
            print("Rejected, school is below 80")
    else:
        print("Rejeted, Score is below 300")






score=int(input("Enter the score"))
if score<0 or score>100:
    print("Rejected")
else:
    result = "Pass" if score >= 51 else "Fail"
    print(result)






total=float(input("Enter the order total"))
answer=input("Enter "yes" or "no")
if total<0 or (answer!="yes" and answer!="no"):
    print("Rejected")
else:
    delivery fee=0 if (total>=50 or answer="yes") else 5:
    a=total+delivery fee
    print("delivery fee=", delivery fee, "final total=", a)
    







day=int(input("Enter the day"))
match day
    case 1:
       print("monday, study day")
    case 2:
       print("tuesday, study day")
    case 3:
       print("wednesday, study day")
    case 4:
       print("thursday, study day")
    case 5:
       print("friday, study day")
    case 6:
       print("saturday, weekend")
    case 7:
       print("sunday, weekend")
    case_:
       print("invalid day")







drink=












student ID=input("Enter student ID")
if student ID="":
    print("rejected")
elif 























































































































