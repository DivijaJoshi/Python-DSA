start=int(input("Enter start: "))
end=int(input("Enter end: "))
sum=0
for i in range(start,end+1):
    if i%7==0:
        sum+=i
        print(i)
print(sum)
# for i in range(0,10,2):
#     print(i)
# for i in range(31,-31,-5):
#     print(i)