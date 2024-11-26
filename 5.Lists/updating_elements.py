my_list=[1,34,56,68,12,26,15,16,33,17]
# updating list- add 1 if element is even and subtract one if element is odd
n=len(my_list)
for i in range(n):
    if my_list[i]%2==0:
        my_list[i]+=1
    else:
        my_list[i]-=1
print(my_list)

