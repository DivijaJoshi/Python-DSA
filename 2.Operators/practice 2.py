"""Write a program that takes two numbers as input and checks if the first
number is divisible by the second."""
# a=int(input("Enter number1: "))
# b=int(input("Enter number2: "))
# if a%b==0:
#     print("Number is divisible")
# else:
#     print("Not divisible")

"""Q2. A student will not be allowed to sit in exam if his/her attendance is less
than 75%.
Take following input from user
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.
# """
# classes= int(input("enter total no. of classes: "))
# attended= int(input("enter total no. of classes attended: "))
# percent= attended/classes*100
# print("Your attendance percentage is %s" %percent )
# if percent<75:
#     print("Not allowed to sit in exam")
# else:
#     print("Allowed")

#Write a program to check if number is divisible by 2 and 3 but not 8.
# a=int(input("Enter number: "))
# if a%2== 0 and a%3==0 and a%8!=0:
#     print("divisible by 2 and 3 and not 8")
# else:
#     print("Error doesnt meet criteria")

#Write a program to calculate bill. Ask the final amount from the user.
# """You have to give discount and print the final bill after discount."""
# bill=int(input("Enter final amount: "))
# if bill>=50000:
#     dis=bill-0.3*bill
#     print("Bill is %f" %dis)   
# elif bill>=40000 and bill<=49999:
#     dis=bill-0.25*bill
#     print("Bill is %f" %dis)
# elif bill>=30000 and bill<=39999:
#     dis=bill-0.2*bill
#     print("Bill is %f" %dis)
# elif bill>=10000 and bill<=29999:
#     dis=bill-0.1*bill
#     print("Bill is %f" %dis)
# else:
#     print("No discount, bill is %f" %bill)

"""Q6. Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest."""

# a=int(input("Enter number 1 : "))
# b=int(input("Enter number 2: "))
# c=int(input("Enter number 3: "))
# d=int(input("Enter number 4: "))
# if b==a:
#     b=int(input("Enter another no. 2 "))
#     print("b is ",b)
# if c==a or c==b:
#     c=int(input("Enter another no. 3 "))
#     print("c is",c)
# if d==a or d==b or d==c:
#     d=int(input("Enter another no. 4 "))
#     print("d is",d)
# if a<b and a<c and a<d:
#     print(a,"Is smallest")
# elif b<a and b<c and b<d:
#     print(b,"Is smallest")
# elif c<a and c<b and c<d:
#     print(c,"Is smallest")
# else:
#     print(d,"Is smallest")

# Input and validate 4 different numbers
# num1 = float(input("Enter the first number: "))

# while True:
#     num2 = float(input("Enter the second number: "))
#     if num2 != num1:
#         break
#     else:
#         print("This number has already been entered. Please enter a different number.")

# while True:
#     num3 = float(input("Enter the third number: "))
#     if num3 != num1 and num3 != num2:
#         break
#     else:
#         print("This number has already been entered. Please enter a different number.")

# while True:
#     num4 = float(input("Enter the fourth number: "))
#     if num4 != num1 and num4 != num2 and num4 != num3:
#         break
#     else:
#         print("This number has already been entered. Please enter a different number.")

# # Find the smallest number using only if-else statements
# smallest = num1

# if num2 < smallest:
#     smallest = num2

# if num3 < smallest:
#     smallest = num3

# if num4 < smallest:
#     smallest = num4

# # Print the result
# print(f"The smallest number is: {smallest}")

"""Ask a year input from user. And tell if the year entered by user is leap or
not.

"""
a= int(input("Enter an year: "))
if a%4==0 and a%400==0:
    print("Leap year")
elif a%4 == 0 and a%100 ==0:
    print("Not a leap year")
elif a%4==0:
    print("Leap year")
else:
    print("Not leap")