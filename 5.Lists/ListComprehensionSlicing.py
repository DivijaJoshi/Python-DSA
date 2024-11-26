# Q1. Make your own list of numbers. Ask a start and end position from User. Print the list from start
#  position to end position using Slicing.
my_list=[1,10,13,4,57,5,6,4,68,5,863,8]
# start=int(input("Enter start: "))
# end=int(input("Enter end: "))
# print(my_list[start:end+1])



# Q2. Make your own list of numbers. Ask a start and end position from User. Make another different list
# which will contain number from start to end position. Use slicing logic.
# start=int(input("Enter start: "))
# end=int(input("Enter end: "))
# new_list=[my_list[start:end+1]]
# print(new_list)


# Q3. Make your own list. Write a Python program that takes an integer as an input, and make a new list
# containing the last n elements of the original list. Using slicing logic.
# n=int(input("Enter a number \"n\" to print last n elements of list: "))
# from typing import List
# def list_slicing(lst:list,n:int):
#     l=len(lst)
#     new_list=lst[l-n:]
#     return new_list
# ans=list_slicing(my_list,n)
# print(ans)


# Q4. Make your own list. Write a Python program that takes an integer as an input, and make a new list 
#containing the last n elements of the original list but in reverse order. Using slicing logic.
# from typing import List
# n=int(input("Enter a number \"n\" to print last n elements of list in reverse order: "))
# def list_slicing(lst:list,n:int):
#     l=len(lst)
#     new_list=lst[l-n:]
#     new_list.reverse()
#     print(new_list)
# list_slicing(my_list,n)

# or

# from typing import List
# n=int(input("Enter a number \"n\" to print last n elements of list in reverse order: "))
# def list_slicing(lst:list,n:int):
#     l=len(lst)
#     new_list=lst[:l-n-1:-1]
#     print(new_list)
# list_slicing(my_list,n)


# Q5. Write a python program to interchange first and last elements in a list.
# from typing import List
# def list_slicing(lst:list):
#     l=len(lst)
#     lst[0],lst[l-1]=lst[l-1],lst[0]
#     print(lst)
# list_slicing(my_list)

# or
# from typing import List
# def list_slicing(lst:list):
#     l=len(lst)
#     temp=lst[0]
#     lst[0]=lst[l-1]
#     lst[l-1]=temp
#     print(lst)
# list_slicing(my_list)


# Q6. Write a Python code to split a list into two halves using list slicing.(Keep the length of list even).
# l=len(my_list)
# def split_list(lst:list):
#     index=l//2
#     list1=lst[:index]
#     list2=lst[index:]
#     print(list1)
#     print(list2)
# split_list(my_list)


# Q7. Ask an integer n from the user. Write a Python program to generate a
# list of powers of 2 from 1 to n using List Comprehension
# Example input: n = 6
# Example output: [1, 4, 9, 16, 25, 36]
# n=int(input("Enter a number: "))
# new_list= [i*i for i in range(1,n+1)] 
# print(new_list)


# Q8. Count how many numbers are divisible by 3 and 6 between 1 to 1000 by using list comprehension.
# new_list=[i for i in range(1,1001) if i%3==0 and i %6==0]
# print(new_list)


# Q9. Ask an integer n from user. Create a list which contains all the prime
# numbers from 1 to n using list comprehension.
# Input: n = 20
# Output: [2, 3, 5, 7, 11, 13, 17, 19]

# n=int(input("Enter a number: "))
# def isPrime(n:int):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# new_list=[i for i in range(2,n+1) if isPrime(i)]
# print(new_list)


# Q10. Ask an integer n from user. Create a list which contains all the numbers divisible by 5.
# Input: n = 30
# Output: [5, 10, 15, 20, 25, 30]
# n=int(input("Enter a number: "))
# new_list=[i for i in range(1,n+1) if i%5==0]
# print(new_list)
