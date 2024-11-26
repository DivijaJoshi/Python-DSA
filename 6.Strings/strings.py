# my_string=""
# while True:
#     a=str(input("Enter a string: "))
#     if a=="q" or a=="Q":
#         break
#     else:
#         my_string+=a
# print(my_string)

# Q1. Write a function that takes a string and returns it reversed.

# def rev_string(s:str):
#     revstring=" "
#     return s[::-1]
# ans=rev_string("dsbfdsf")
# print(ans)

# or

# def rev_string(s:str):
#     new=" "
#     for i in s:
#         new=i+new
#     return new
# ans=rev_string("ddssddksk")
# print(ans)

# Q2. Write a function that takes a string and returns it in uppercase.
# n=str(input("Enter a string: "))
# def up_case(s:str):
#     return s.upper()
# ans=up_case(n)
# print(ans)

# or

# n=str(input("Enter a string: "))
# def up_case(s:str):
#     new=" "
#     for i in s:
#         a=ord(i)
#         if a>=97 and a<=120:
#             a-=32
#             new+=chr(a)
#         elif a>=65 and a<=90:
#             new+=i
#         else:
#             new+=i
#     return new
# ans=up_case(n)
# print(ans)


# Q2. Write a function that takes a string and returns it in uppercase.
# n=str(input("Enter a string: "))
# def up_case(s:str):
#     return s.upper()
# ans=up_case(n)
# print(ans)

# or

# n=str(input("Enter a string: "))
# def up_case(s:str):
#     new=" "
#     for i in s:
#         a=ord(i)
#         if a>=97 and a<=120:
#             a-=32
#             new+=chr(a)
#         elif a>=65 and a<=90:
#             new+=i
#         else:
#             new+=i
#     return new
# ans=up_case(n)
# print(ans)

# Q3. Write a function that removes all vowels (a, e, i, o, u) from a given string.
# n=str(input("Enter a string: "))
# def remove_vow(s:str):
#     vowels="aeiou"
#     new=" "
#     for i in s:
#         if i not in vowels:
#             new+=i
#     return new
# ans=remove_vow(n)
# print(ans)


# Q4. Write a function that counts the number of words in a given string.
# (String may only contain alphabets and spaces
# n=str(input("Enter a string: "))
# def count_words(s:str):
#     count=1
#     for i in s:
#         if ord(i)==32:
#             count+=1
#     return count
# ans=count_words(n)
# print(ans)

# or

# n=str(input("Enter a string: "))
# def count_words(s:str):
#     if not s:
#         return 0
#     count=1
#     for i in s:
#         if i==" ":
#             count+=1
#     return count
# ans=count_words(n)
# print(ans)


# Q5. Write a function that finds and returns the longest word in a given string.
# n=str(input("Enter a string: "))
# def long_word(s:str):
#     if not s:
#         return 0
#     longest=" "
#     current=" "
#     for i in s+" ":
#         if i!=" ":
#             current+=i
#         else:
#             if len(current)>len(longest):
#                 longest=current
#             current=" "
#     return longest
# ans=long_word(n)
# print(ans)

# OR

# def longest_word(s: str) -> str:
#     longest = ""
#     current = ""
#     for char in s:
#         if char == " ":
#             if len(current) > len(longest):
#                 longest = current
#             current = ""
#         else:
#             current += char
#     if len(current) > len(longest):
#         longest = current
#     return longest
# my_string = "ab cde cde dsfhkjfdshfs dshkjfhkdsjfhkdsjdjhkf"
# print(longest_word(my_string))

# OR
# n=str(input("Enter a string: "))
# def long_word(s:str):
#     longest=" "
#     for i in s.split():
#         if len(i)>len(longest):
#             longest=i
#     return longest
# ans=long_word(n)
# print(ans)


# Q6. Write a function that capitalizes the first letter of each word in a given string.
# n=str(input("Enter a string: "))
# def capitalize(s:str):
#     n=len(s)
#     a=" "
#     for i in s:
#         a=s.title()
#         return a
# ans=capitalize(n)
# print(ans)
        
# or
# n=str(input("Enter a string: "))
# def capitalize(s:str):
#     flag=True
#     a=" "
#     for i in s:
#         if i==" ":
#             a+=i
#             flag=True
#         elif flag:
#             a+=i.upper()
#             flag=False
#         else:
#             a+=i
#     return a
# ans=capitalize(n)
# print(ans)

# Q7. Write a function that replaces all consonants in a given string with asterisks (*).
# n=str(input("Enter a string: "))
# def rep(s:str):
#     vowels="aeiou"
#     a=""
#     for i in s:
#         if i.isalpha and i not in vowels:
#             a+="*"
#         else:
#             a+=i
#     return a
# ans=rep(n)
# print(ans)


# or
# n=str(input("Enter a string: "))
# def rep(s:str):
#     vowels="aeiou"
#     a=""
#     for i in s:
#         if ("a"<=i<="z"or "A"<=i<="Z")and i not in vowels:
#             a+="*"
#         else:
#             a+=i
#     return a
# ans=rep(n)
# print(ans)


# or     
# n=str(input("Enter a string: "))
# def rep(s:str):
#     vowels="aeiou"
#     for i in s:
#         if i.lower() not in vowels and i.isalpha():
#             s=s.replace(i,"*")
#     return s
# ans=rep(n)
# print(ans)

# Q8. Write a function that removes all non-alphabetic characters from a given string.
# n=str(input("Enter a string: "))
# def rep(s:str):
#     a=""
#     for i in s:
#         if not i.isalpha():
#             a+=i
#     return a
# ans=rep(n)
# print(ans)


# or
# n=str(input("Enter a string: "))
# def rep(s:str):
#     a=""
#     for i in s:
#         if not ("a"<=i<="z" or "A"<=i<="Z"):
#             a+=i
#     return a
# ans=rep(n)
# print(ans)

# Q9. Write a function that counts the number of digits in a given string.
# n=str(input("Enter a string: "))
# def rep(s:str):
#     count=0
#     for i in s:
#         if "0"<=i<="9":
#             count+=1
#     return count
# ans=rep(n)
# print(ans)


# Q10. Write a function that removes duplicate characters from a givenstring.
# n=str(input("Enter a string: "))
# def rep(s:str):
#     a=""
#     for i in s:
#         if i not in a:
#             a+=i
#     return a
# ans=rep(n)
# print(ans)


# Q11. Write a function that checks if a given string contains only alphanumeric characters.


# n=str(input("Enter a string: "))
# def rep(s:str):
#     a=""
#     for i in s:
#         if not("a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9" or i==" "):
#             return False
#     return True
# ans=rep(n)
# print(ans)


# Q12. Write a function that replaces all spaces in a given string with hyphens (-).
# n=str(input("Enter a string: "))
# def rep(s:str):    
#     for i in s:
#         if i==" ":
#             s=s.replace(" ","-")
#     return s
# ans=rep(n)
# print(ans)

#or
n=str(input("Enter a string: "))
def rep(s:str):
    a=""
    for i in s:
        if i==" ":
            a+="-"
        else:
            a+=i
    return a
ans=rep(n)
print(ans)
