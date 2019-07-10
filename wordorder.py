num=int(input("Enter"))
ls=[]
times=[]
for i in range(num):
    ls.append(input())
    times.append(1)
for i in range(0,num-1,1):
    for j in range(i+1,num,1):
        if ls[i]==ls[j]:
            times[i]+=1
            del ls[j]
            del times[j]
            num-=1
ls=set(ls)
print(len(ls))
for i in range(0,len(times),1):
    print(times[i],end=" ")
