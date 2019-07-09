def leap(year):
    if year%400==0:
       return True;
    elif year%100==0:
        return False;
    elif year%4==0:
        return True;
    else:
        return False;

year=int(input("Enter year"))
if leap(year): print("Leap year")
else: print("Not a leap year")
