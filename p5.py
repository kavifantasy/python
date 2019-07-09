import random
n=random.randint(1,100)
str=input("Hello!Enter your name:")
print("Well {}, I am thinking of a number between 1 and 10".format(str))
for i in range(5):
    m=int(input("Take a guess"))
    if(m>n):
        print("Your guess in too high")
    elif(m<n):
        print("Your guess is too low")
    else:
        print("Hey..Correct")
        break;
print("You failed :-) I won.. I thought of {}".format(n))
