
n=int(input("Enter a no.: "))
def pattern(n:int):
    for i in range(n//2+1,0,-1):
        for j in range(i,n//2+2):
            print(j,end=" ")
        print()
    for i in range(n//2,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
pattern(n)