y=[]
answer=[]
sum=0
k, m = [int(x) for x in input().split()] 
#print(k)
#print(m)
for i in range(k):
    x = [int(x) for x in input().split()] 
    answer.append(max(x)*max(x))
    y.append(x)
for i in range(k):
    sum+=answer[i]
print(sum%m)