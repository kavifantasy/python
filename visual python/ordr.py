ls=[]
ls_tup=[]
tup=()
cost=[]
num=int(input("Enter the number of order"))
print("Enter details in the order of Order number, Book title, Quantity, Price per item:")
for i in range(num):
    x = [x for x in input().split()]
    x.append(int(x[2])*int(x[3]))
    ls.append(x)
cost=map(lambda ls[y][2],ls[y][3]:ls[y][2]*ls[y][3],ls)
print(ls)
print(cost)



