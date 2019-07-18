def sum_sq(num):
    sum=0
    for i in num:
        sum+=i*i
    return(sum)

num=[int(num) for num in input("Enter 1 or 2 numbers:").split()]
print(sum_sq(num))