class Bank:
    def __init__(self):
        self.balance=0

    def create(self,initial_deposit):
        if initial_deposit>=10000:
            self.balance+=initial_deposit
            print("Bank account opened successfully")
        else:
            print("Enter the value equal to above 10000")
     
    def deposit(self,amount):
        if amount%50==0:
            self.balance+=amount
            print("Amount deposited successfully")
        else:
            print("Enter 50 0r 100 or 200 or 500 or 1000")        
        
    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount%100==0:
            if (self.balance-amount)>=5000:
                self.balance-=amount
                print("Amount withdrawn successfully")
            else:
                print("It exceeds your minimum balance")
        else:
            print("Enter 100 or 200 or 500 or 1000")

user=Bank()
ch=1
while(ch==1):   
    print("1.Create new bank account")
    print("2.Deposit to existing account")
    print("3.Withdraw amount")
    print("4.Check balance")
    print("5.exit")
    choice=int(input("Choose 1 or 2 or 3 or 4 or 5"))
    if choice==1:
        initial=int(input("Enter the initial deposit"))
        user.create(initial)
    if choice==2:
        amount=int(input("Enter the amount to be deposited"))
        user.deposit(amount)
    if choice==3:
        amount=int(input("Enter the amount to be withdrawn"))
        user.withdraw(amount)
    if choice==4:
        print(user.get_balance())
    if choice==5:
        exit()





