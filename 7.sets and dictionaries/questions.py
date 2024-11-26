# Q1. Ask number of subjects from the user. Ask the subject name and marks from 
# the user and store that into the dictionary and print it.
# d={}
# def dict_add(d:dict):
#     n=int(input("Enter no. of subjects: "))
#     for i in range(n):
#         k=str(input("Enter subject name: "))
#         v=str(input(f"Enter marks for subject {k}:  "))
#         d.update({k:v})
#         # d[k]=v
#     return d
# ans=dict_add(d)
# print(ans)


# Q2. Given a list of integers, create a dictionary that stores each unique
# integer as a key and its frequency as the value. Find the integer with the
# maximum frequency.
# Example Input: [4, 5, 6, 5, 4, 4, 7]
# Expected Output: 4 (Frequency: 3)
# n=int(input("Enter no. of elements:"))
# a=str(input())
# my_list=list(map(int,a.split()[:n]))
# print(my_list)
# d={}
# def create_dict(d:dict):
#     for k in my_list:
#         if k in d:
#             d[k]+=1
#         else:
#             d[k]=1
#     return d
# ans=create_dict(d)
# print(ans)
            


# Q3. Create two list. One would be subject name and other would be marks.
# Join both the list to make it as a dictionary. (The length of two lists should
# be the same).

# name=["sst","cse","maths","sci"]
# marks=[80,90,95,95]
# d={}
# def join_dict(d:dict,name:list,marks:list):
#     for i in range(len(name)):
#         d[name[i]]=marks[i]
#     return d
# ans=join_dict(d,name,marks)
# print(ans)
            


# Q4. Write a function that takes a dictionary and a key, and returns True if
# the key is found in the dictionary, otherwise False.
# d = {"anirudh": 45, 56: 78, "gender": "Male", 11: 22}
# k="anirudh"
# def find_key(d:dict,k):
#     return k in d
# ans=find_key(d,k)
# print(ans)


# Q5. Given two dictionaries, write a function to merge them into a new dictionary. 
# If there is any overlap of keys, the value from the second dictionary should overwrite 
# the one from the first dictionary.
# Dictionary 1:
# {'apple': 3, 'banana': 5, 'cherry': 7}
# Dictionary 2:
# {'banana': 8, 'orange': 10, 'apple': 9}
# Expected Output:
# {'apple': 9, 'banana': 8, 'cherry': 7, 'orange': 10}

# d1 = {"a": 54, "b": 11, "c": 90}
# d2 = {"a": 100, "b": 200, "d": 56}
# def mergedict(d1:dict,d2:dict):
#     for key,values in d2.items():
#         # d1[key]=values
#         # or
#         d1.update({key:values})
#     return d1
# ans=mergedict(d1,d2)
# print(ans)


# Q6. Write a function that updates the values of a dictionary by multiplying
# them by a given factor only if the value is an integer.
# d = {"a": 56, "b": "hello", "c": 55.67, "d": True, "e": 100}
# factor=int(input("Enter a factor: "))
# def update_dict(d:dict,factor:int):
#     for keys,values in d.items():
#         if isinstance(values,int):
#             d[keys]=values*factor
#     return d
# ans=update_dict(d,factor)
# print(ans)          


# Q7. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are squares of the keys.
# dict={}
# for i in range(1,16):
#     dict[i]=i**2
# print(dict)


# Q8. Given a dictionary, write a function that returns a new dictionary
# containing only the keys that have values of type str.
# my_dict = {"a": "b", "z": 12, "adult": True, 10: "Male"}
# def str_dict(my_dict:dict):
#     d1={}
#     for keys,values in my_dict.items():
#         if isinstance(keys,str):
#             d1[keys]=values
#     return d1
# ans=str_dict(my_dict)
# print(ans)          



# Q9. Ask a string from user. Store the frequency of each character in the
# dictionary. Then print the character with the maximum frequency.
# s=str(input("Enter a string: "))
# def max_freq(s:str):
#     d={}
#     maxfreq=0
#     ele=0
#     for k in s:
#         # d[i]=d.get(i,0)+1
#         # or
#         d[k]=s.count(k)
#     for k,v in d.items():
#         if v>maxfreq:
#             maxfreq=v
#             ele=k
#     print(f"Character with maximumvalue is {ele}, occuring {maxfreq} times  ")
#     return d
# ans=max_freq(s)
# print(ans)   



# Q10. Write a Python program to combine two dictionary by adding values
# for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
# def combine_dict(d1:dict,d2:dict):
#     for k,v in d2.items():
#         if k in d1:
#             d1[k]+=d2[k]
#         else:
#             d1[k]=v
#     return d1
# ans=combine_dict(d1,d2)
# print(ans)




# Q11. Given a dictionary with key-value pairs, remove all the keys with
# values greater than K, including mixed values.
# Input : test_dict = {‘Gfg’ : 3,
# ‘is’ : 7,
# ‘best’ : 10,
# ‘for’ : 6,
# ‘xyzx’ : ‘CS’}, K = 7
# Output : {‘Gfg’ : 3,
# ‘for’ : 6,
# ‘xyzx’ : ‘CS’}
# Explanation : All values greater than K are removed. Mixed value is
# retained.
# Input : test_dict = {‘Gfg’ : 3,
# ‘is’ : 7,
# ‘best’ : 10,
# ‘for’ : 6,
# ‘qqqq’ : ‘CS’}, K = 1
# Output : {‘qqqq’ : ‘CS’}
# Explanation : Only Mixed value is retained.

d = {"Gfg" : 3,"is" : 7,"best" : 10,"for" : 6,"xyzx" : "CS"}
key=3
def combine_dict(d:dict,key:int):
    d1={}
    for k,v in d.items():
        if isinstance(v,int):
            if v>key:
                d1[k]=v
        else:
            d1[k]=v
    return d1
ans=combine_dict(d,key)
print(ans)