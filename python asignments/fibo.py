def fibonacci(n):
    series=[]
    a=-1
    b=1
    for i in range(n):
        c=a+b
        series.append(c)
        a=b
        b=c
    return series
n=int(input("Enter the number of fibonacci series"))
print(fibonacci(n))

