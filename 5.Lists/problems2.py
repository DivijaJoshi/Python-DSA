# Q1. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list 
# but in reverse order.
# my_list=[]
# for i in range(1,11):
#     a=int(input(f"Enter number {i} :"))
#     my_list.append(a)
# print(my_list)
# n=len(my_list)
# new_list=[]
# for i in range(n-1,-1,-1):
#     new_list.append(my_list[i])
# print(new_list)



# Q2. Make a list. Write a simple program for addition of the 2nd element from start and 2nd element from the end.
# my_list=[1,2,35,55,2,3,7,16]
# a=my_list[1]+my_list[-2]
# print(a)


# Q3. Ask 10 numbers from the user and put them into the list. Now remove all the even numbers from that list.
# my_list=[]
# for i in range(10):
#     a=int(input(f"Enter number {i+1} :"))
#     my_list.append(a)
# print("my_list",my_list)
# n=len(my_list)
# ls=[]
# for i in range(n):
#     if my_list[i]%2!=0:
#         ls.append(my_list[i])
# print(ls)


# Q4. Write a python program which prints all the values whose count is greater than 3.
# my_list=[3,4,3,3,3,4,4,4,5,1,9,6,5,5,5,6,6,6,7,7,7,8,10,15,14,13,13]
# ans=[]
# print("my_list",my_list)
# n=len(my_list)
# for i in range(n):
#     if my_list.count(my_list[i])>3:
#         if my_list[i] not in ans:
#             ans.append(my_list[i])
# print(ans)



# Q5. Write a program to remove the nth index element from a list using a function.
# n=int(input("Enter the nth index to remove: "))
# def remove_ele(l:list,index:int):
#     N=len(l)
#     if index>N:
#         print("List out of index")
#     else:
#         l.pop(index)
#     print(l)

# my_list=[1,2,3,15,14,1,618,1,9]
# print(my_list)
# remove_ele(my_list,n)



# Q6. Make two lists of same length and pass it to a function. Return a third
# list where each element is the sum of index.
# a=[1,2,3,5,8,9,4,5,6,1]
# b=[5,4,6,9,8,7,5,0,15,4]
# c=[]
# def add_list(m:list,n:list):
#     n1=len(m)
#     for i in range(n1):
#         total=m[i]+n[i]
#         c.append(total)
#     return(c)
# ans=add_list(a,b)
# print(ans)


# Q7. Write a Python Program to find sum and average of List in Python.
# my_list=[1,2,3,4,56,56,47,48,44,16]
# n=len(my_list)
# total=0
# for i in range(n):
#     total+=my_list[i]
# print("total is: ",total)
# aveg=total/n
# print("Average is: ",aveg)      


    
