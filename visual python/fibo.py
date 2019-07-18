def fibo(n):
    a,b=0,1
    print(a,'\n',b)
    for i in range(n):
        c=a+b
        print(c)
        a=b
        b=c
n=int(input("Enter number of terms"))    
fibo(n)
