my_list=[54,54,75,36,35,75,35,88,33,88,13,17,19]
# total=0
# n=len(my_list)
# for i in range(0,n):
#     total+=my_list[i]
# print(total)
# total2=0
# for i in my_list:
#     total2+=i
# print(total2)

# total=0
# n=len(my_list)
# for i in range(0,n):
#     if my_list[i] %2==0:
#         total+=my_list[i]
# print(total)

# total2=0
# for i in my_list:
#     if i %2==0:
#         total2+=i
# print(total2)


def isPrime(n:int):
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    if factors==2:
        return True
    else:
        return False

n=len(my_list)
for i in range(0,n):
    if isPrime(my_list[i])== True:
        print(my_list[i])
for i in range(0,101):
    if isPrime(i)==True:
        print(i)