import re
n=int(input())
ls=[]
m=[]
for i in range(n):
    x=input()
    match= re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',x)
    if(match):
        m.append(1)
    else:
        m.append(0)
    ls.append(x)
print(ls)
print(m)
