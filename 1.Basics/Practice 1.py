# a=5
# b=10
# print( a > 5 and b >= 10)
# print(a >= 5 or not b > 10)
# print(not ( a > 5 and b > 5))
# print(not ( a < 10 or not b < 10))
# # print(not ( not a <= 5 or not b >= 10))

# """2) Python progsram to convert kilometers to miles. Ask kilometer from
# User """
# a=float(input("Enter distance in km: "))
# miles= a*0.62137
# print(a)
# print(f"Distance converted to miles for {a} km is {miles:.3f} miles")

#. 4) Ask 3 numbers from User and Calculate the Average
# a=int(input("Enter amount in rupees"))
# print (a)
# b=a*100
# print(f"{a} rupees is {b} paise")

#5)Q5. Calculate Area of Square by taking side from User.
# side = int(input("Enter side:"))
# area=side**2
# print(f"Area of square is {area}")

"""Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win= 4 points, 1 tie =2 points)
"""
# games=int(input("Enter number of games played"))
# won=int(input("Enter number of games won: "))
# loss=int(input("Enter number of games lost: "))
# tied=games-(won+loss)
# points=won*4+tied*2
# print("Total no. of ties are:",tied,"and total points= ",points)

#Q7. Check if the number entered by User is divisible by 3 or not.
# n=int(input("Enter a number: "))
# if n%3==0:
#     print(f"divisible by 3")
# else:
#     print(f"Not divisible")

#Ask a number from user. Print if the number is ODD or EVEN.
# a=int(input("enter a number: "))
# if a%2==0:
#     print("even")
# else: 
#     print("odd")    

"""Q9. Take values of length and breadth of a rectangle from user and check if
it is square or not."""
length=int(input("enter l of rect."))
breadth=int(input("enter b of rect."))
if length==breadth:
    print("SQUARE")
else:
    print("NOT SQUARE")
           
