# def greet():
#     print("Hello I am divi")
# #Calling function greet()
# greet()

#
# def marks(a:int,b:int,c:int,d:int,e:int):
#     total=a+b+c+d+e
#     percent=(total/500)*100
#     return percent,total
# print(marks(85,90,95,98,91))
# def concat(a:str,b:str):->str:

def marks(s1:int,s2:int,s3:int,s4:int,s5:int):
    total=((s1+s2+s3+s4+s5)/5)*100
    return total>= 33
result=marks(10,20,30,10,10)
print(result)

