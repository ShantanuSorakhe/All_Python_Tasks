class bank_account:
    def __init__(self,account_type,name,balance):
        self.account_type = account_type
        self.name = name
        self.balance = balance

    def details(self):
        print("account_type:",self.account_type)
        print("name:",self.name)
        print("balance:",round(self.balance,2))


class add_amount(bank_account):
    def __init__(self,account_type,name,balance):
        super().__init__(account_type,name,balance)
    
    def deposit(self,amount):
        if amount <= 0:
            print("invalid deposit amount")
        else:
            self.balance += amount
            print(f"{amount} chillar deposited successfully")


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


class bank_interest(withdraw_amount):
    def __init__(self,account_type,name,balance):
        super().__init__(account_type,name,balance)
    
    def add_quarterly_interest(self,rate,years):
        if rate <= 0 or years <= 0:
            print("galat dala rate ya time")
        else:
            Balance = self.balance
            Rate = rate
            Time = years

            Final_balance = Balance * ((1 + (Rate/(4*100))) ** (4*Time))
            interest = Final_balance - Balance

            self.balance = Final_balance

            print(f"chavanni interest added: {round(interest,2)}")
            print(f"rate: {rate}% for {years} year(s) (quarterly)")


obj = bank_interest("savings","shantanu",10000)

obj.details()
obj.deposit(500)
obj.details()
obj.withdraw(300)
obj.details()
obj.add_quarterly_interest(2,1)   
obj.details()