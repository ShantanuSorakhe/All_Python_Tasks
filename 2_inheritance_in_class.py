class bank_account:
    def __init__(self,account_type,name,balance):
        self.account_type = account_type
        self.name = name
        self.balance = balance

    def details(self):
        print("account_type:",self.account_type)
        print("name:",self.name)
        print("balance:",self.balance)

class add_amount(bank_account):
    def __init__(self,account_type,name,balance):
        super().__init__(account_type,name,balance)
    
    def deposit(self,amount):
        if amount <= 0:
            print("invalid deposit amount")
        else:
            self.balance += amount
            print(f"{amount} deposited successfully")

class withdraw_amount(add_amount):
    def __init__(self,account_type,name,balance):
        super().__init__(account_type,name,balance)
    
    def withdraw(self,amount):
        if amount <=0:
            print(" invalid withdraw amount")
        elif amount > self.balance:
            print("insufficient balance- aukad se bahar")
        else:
            self.balance -= amount
            print(f"{amount} succesfully withdrawn")

obj = withdraw_amount("savings","shantanu",10000)

obj.details()
obj.deposit(500)
obj.details()
obj.withdraw(300)
obj.details()

    
        
        
