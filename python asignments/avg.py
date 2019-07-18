def avg(num):
    sum=0
    for i in num:
        sum+=i
    return(sum/len(num))

num=[int(num) for num in input("Enter the numbers").split()]
print(avg(num))