def minimum(num):
    min_value=num[0]
    for i in num:
        if i<=min_value:
            min_value=i
    return(min_value)
num=[int(num) for num in input("Enter the numbers").split()]
print(minimum(num))