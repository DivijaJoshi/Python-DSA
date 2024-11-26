# Print reverse of words of the string eg hello cat to cat hello
my_str="Hello I am Divi"
# a=my_str.split()
# # print(a[::-1])

# # or
# a.reverse()
# b=" ".join(i for i in a )
# print(b)

# reverse words eg hello cat to olleho tac
# my_str="Hello I am Divi"
# a=my_str.split()
# print(a)
# for i in a:
#     b=i[::-1]
#     print(b,end=" ")

# reverse words eg hello cat to tac olleho 
my_str="Hello I am Divi"
a=my_str.split()
print(a)
a.reverse()
# b=" ".join(i[::-1] for i in a)
# or
b=" ".join(i[::-1] for i in a[::-1])
print(b)