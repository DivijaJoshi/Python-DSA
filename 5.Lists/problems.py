# Q1. Create a list of your own. Print the total count of all odd numbers.
my_list=[1,2,3,4,5,6,7,20,25,15]

# count=0
# for i in my_list:
#     print(i,end=" ")
#     print()
#     if i%2!=0:
#         count+=1
# print(f"Count of odd numbers is: {count}")


# Q2. Create a list of your own. Print the total count of all odd and even
# numbers.
# count_odd=0
# count_even=0
# for i in my_list:
#     print(i,end=" ")
#     print()
#     if i%2!=0:
#         count_odd+=1
#     else:
#         count_even+=1
# print(f"Count of odd numbers is: {count_odd}")
# print(f"Count of even numbers is: {count_even}")


# Q3. Create a list of your own. Print the prime numbers in that list.
# for i in my_list:
#     factors=0
#     for j in range(1,i+1):
#         if i%j==0:
#             factors+=1
#         else:
#             continue
#     if factors==2:
#         print(i,end=" ")


# Q4. Create a list of your own. Print the sum of all the prime numbers in that list.
# sum=0
# for i in my_list:
#     factors=0
#     for j in range(1,i+1):
#         if i%j==0:
#             factors+=1
#         else:
#             continue
#     if factors==2:
#         sum+=i
#         print(i,end=" ")
# print("sum of prime numbers in list is:", sum)


# Q5.  Create a list of your own. Print the sum and product of all the elements in that list.
# sum=0
# product=1
# for i in my_list:
#     sum+=i
#     product*=i
#     print(i,end=" ")
# print(sum)
# print(product)


# Q6. Create a list of your own. Print all the numbers divisible by 5 but in reverse order.

# a=[]
# for i in my_list:
#     if i%5==0:
#         a.append(i)
# print(a[::-1])

# or
# n=len(my_list)
# for i in range(n-1,-1,-1):
#     if my_list[i]%5==0:
#        print(my_list[i], end=" ")


""" Q7. Create a list of your own. Find the maximum number present in that list.
Do not use max function directly. List may contain both positive and negative integers. """

# n=len(my_list)
# max_no=my_list[0]
# for i in range(0,n):
#     if my_list[i]>max_no:
#         max_no=my_list[i]
# print(max_no)

#or 

# n=len(my_list)
# maxi=float("-INF")
# for i in range(n):
#     maxi=max(maxi,my_list[i])
# print(maxi)

"""Create a list of your own. Find the minimum number present in that
list. Do not use min function directly. List may contain both positive and
negative integers"""
# n=len(my_list)
# mini=float("INF")
# for i in range(n):
#     if my_list[i]<mini:
#         mini=my_list[i]
# print(mini)

# or

# n=len(my_list)
# mini=float("INF")
# for i in range(n):
#     mini=min(mini,my_list[i])
# print(mini)

"""Create a list of your own. Print the largest prime numbers in that list"""
# n=len(my_list)
# a=[]
# for i in my_list:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         a.append(i)
# print(a)
# maxi=0
# for i in a:
#     if i>maxi:
#         maxi=i
# print(maxi)

# or

# def isPrime(n:int):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# maxi=float("-Inf")        
# for i in my_list:
#     if isPrime(i):
#         if i>maxi:
#             maxi=i
# print(maxi)



