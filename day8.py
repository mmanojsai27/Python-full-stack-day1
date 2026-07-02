#--------------------------------------Statements-------------------------
'''

1).Condition Statements
--------------------------------
if--->It uses to check a condition is True or Not 
eg:num = 9
if num % 3 == 0:
   print(f"{num} is a even number")
----------------------------------------------
if-else
------------------------------------------------
--->else
*
eg:num = 9
if num % 2 == 0:
   print(f"{num} is a even number")
else:
   print(f"{num} is odd number")
-----------------------------------------------------------------
nested if
--------------------------------------------------------------
--> if inside the another if is called as nested if
*
eg:manoj_SBI_details = {"ATM PIN":'2731'}
pin = input("Enter your ATM PIN: ")
if len(pin) == 4:
   if pin in manoj_SBI_details['ATM PIN']:
    print("Welcome to ATM MAnoj!")


   else:
       print("You have entered wrong pin")
else:
    print("Pls entered only digit pin")
------------------------------------------------------------
elif:
----> Eg :
marks = int(input("Enter yours marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks > 70:
    print("B")
else:
    print("Failed")
---------------------------------------------------------
2).control Statements
3).loop Statements

'''
'''
a = int(input())
b = int(input())
c = int(input())
if a>b:
    print(a,"is maximum value")
elif b>c:
    print(b," is maximum values")
elif c > a:
    print(c," is maximum value")
else:
    print("The value is Min Value")
'''


a = input("Enter a Char: ")
b  = "A,E,I,O,U,a,e,i,o,u"

if a in b:
    print(a,"Is Vowel")
else:
    print(a,"Is consonants")






































