def desc(lst):
    size=len(lst)
    for i in range(size-1):
        for j in range(i+1,size):
            if lst[j]>=lst[i]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
    return(lst)
lst=[5,1,10,24,53,12,53]
print(desc(lst))