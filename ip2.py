lst1=[10,['user1','user2'],10.25,('test1','test2'),True,None]
lst1[3]=list(lst1[3])
f= []
for sl in lst1:
    if type(sl)==list or type(sl)==tuple:
        for item in sl:
            f.append(item)
    else:
        f.append(sl)
print(f)
