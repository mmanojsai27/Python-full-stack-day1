'''
=========================================
Operators
==========================================
-----------------------------
1) Arithmetic operators
--->
    +, -, *, /, //, **, %.
-------------------------
2) Assignment
--->
     =, +=, -=, *=, %=
-----------------------
3) camparison
---> ==, !=, <=, =>,
--------------------------
4) Logical
---> and, or, not.
----------------------------
5) Identity
---> is---> same object or not
---> is not---> not the same object
----------------------------------
6) Membership
---> in-->
---> not in-->
---------------------------
7) Bitwise
---> &, <<, >>,|, ^.
'''
'''
#Arithmetic operators
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

#Assignment
a=10
b=20
print(a=b)

#Identity
a= 20
b=20
print(a==b)
print(a is b)

#Membership
a = [1,2,3,4,5]
print(2 in a)
print(31 not in a)

#Bitwise
print(5 & 4)
print(5 | 3)
print(3 << 4)
print(3 >> 4)
print(5 ^ 4)
'''
#=================================================
#Example on Arithmetic
'''
a = 10
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
'''
#---------------------------------
#Example on Comaprison
'''
a = 10
b =4
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
'''
#Example on logical
'''
a = 10
b = 1
print(a and b)
print(a or b)
print(not (a>b))
'''
#Examole on Assignment
'''
x = 5
x += 3
print(x)
'''
#Example on Membership

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" not in fruits)

#Example on Identity
a = [1,2]
b = a
c = [1,2]

print(a is b)
print(a is c)
print(a == c)

