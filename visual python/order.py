units=int(input("Enter the number of units consumed"))
if units>=0 and units<=100:
    cost=units
elif units>=101 and units<=200:
    cost=units*1.50
elif units>=201 and units<=500:
    cost=units*3
else:
    cost=units*5
cost+=cost*0.015
print(cost)
