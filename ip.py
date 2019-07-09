n=int(input("Enter number"))
m=0
for i in range(1,n,1):
    m+=1
    print()
    for j in range(n-1,m,-1):
        print(end=" ")
    for j in range(i):
        print('*',end=' ')
