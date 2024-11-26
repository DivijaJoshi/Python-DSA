# m=int(input("enter marks: "))
# if m>=91:
#     print("A")
# elif m>=81 and m<=90:
#     print("B")
# elif m>=71 and m<=80:
#     print("C")
# elif m>=61 and m<=70:    
#     print("D")
# else:    
#     print("Fail") 

#2nd 
a=int(input("enter an integer:"))
if a%3==0 and a%5==0:
    print("FOOBAR")
elif a%3==0:
    print("FOO")
elif a%5==0:
    print("BAR")
else:
    print("Invalid")