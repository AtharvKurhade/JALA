#1. Write a program to print  “Bright IT Career”  ten times using for loop
a = "Bright IT Career"
for i in range(0, 10):
    print(a)

'''
2. Write a java program to print 1 to 20 numbers using the while loop
'''
a = 1
while (a <= 20):
    print(a)
    a += 1

#3. Program to equal operator and not equal operators
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if(a == b):
    print("Both numbers are equal")
if(a != b):
    print("Both number are not equal")  

#4. Write a program to print the odd and even numbers
a = int(input("enter first number:"))
if(a%2 ==  0): 
    print("%d is even number" % a)
else:
    print("%d is odd number" % a) 

#5. Write a program to print largest number among three numbers.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if(a>=b) and (a>=c):
    print(a)
elif(b>=a) and (b>=c):
    print(b)
else:
    print(c)

#6. Write a  program to print even number between 10 and 20 using while
a = 9
while(a <= 20):
    a += 1
    if(a%2 == 0):
        print(a)

#7. Write a program to print 1 to 10 using the do-while loop statement
a = 1
while (a <= 10):
    print(a)
    a += 1

#8. Write a program to find Armstrong number or not
a = int(input("Enter first number:"))
b = 0
c = a
while c > 0:
   d = c % 10
   b += d ** 3
   c //= 10
if a == b:
   print(a,"is an Armstrong number")
else:
   print(a,"is not an Armstrong number")

#9. Write a program to find the prime or not
a = int(input("Enter a number:"))
for i in range(2,a):
    if (a % i) == 0:
        print(a,"is not a prime number")
else:
    print(a,"is a prime number")

#10. Write a program to palindrome or not
a = input("enter number ot text to check if its palidrome or not:")
 
b = ""
for i in a:
    b = i + b
 
if (a == b):
    print("Yes")
else:
    print("No")

#11. Program to check whether a number is EVEN or ODD using switch
a = int(input("enter first number:"))
if(a%2 ==  0): 
    print("%d is even number" % a)
else:
    print("%d is odd number" % a) 
