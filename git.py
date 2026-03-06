class BankAccount:
    def __init__(self, name, balance, secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def withdraw(self):
        print("=== Withdrawing Balance ===")
        secret = input("Inout your secret number:  ")

        if secret == self.__secret:
            amount = float(input("Input your amount:  "))
            remain = self.__balance - amount

            if remain < 0:
                print("your balance is not enough to withdraw")
            else:
                self.__balance = remain
                print("...Withdrawal Successfully...")
                print(f"Your remaining balance is: {self.__balance}")
        else:
            print("we dont't know you")

    def Check_Balance(self):
        print("=== Checking Balance ===")
        secret = input("Input your secret number: ")

        if secret == self.__secret:
            print(f"Hello User: {self.name}")
            print(f"Your remaining balance is {self.__balance}")
        else:
            print("We are sorry but we don't know you.")

    def deposit(self):
        print("User is depositing")

   
class SavingAccount(BankAccount):
    def Calculate_Interest(self):
        print(f"Your Balance now is {self._BankAccount__balance}")

   
class StudentBankAccount(BankAccount):
    def withdraw(self):
        print("==== Student Withdraw ====")
        secret = input("Input your secret number: ")

        if secret == self._BankAccount__secret:
            amount = float(input("Input your amount: "))

            if amount > 500:
                print("You cannot withdraw more than 500$")
            else:
                self._BankAccount__balance -= amount
                print(f"Your current balance is {self._BankAccount__balance}")
        else:
            print("We dont know you.")

   
class PremiumSaving(SavingAccount):
    def deposit(self):
        print("==== Premium Deposit ====")
        amount = float(input("Input deposit amount: "))

        bonus = amount * 0.02
        self._BankAccount__balance += amount + bonus

        print(f"Bonus: {bonus}")
        print(f"Your current balance is {self._BankAccount__balance}")

   
class BusinessAccount(BankAccount):
    def take_loan(self):
        loan = float(input("Input loan amount: "))
        self._BankAccount__balance += loan
        print(f"your current balance is {self._BankAccount__balance}")

    
rose = SavingAccount(name="rose", balance=30000, secret="1234")
rose.withdraw()
rose.Check_Balance()
rose.Calculate_Interest()

   
student = StudentBankAccount(name="rose", balance=90000, secret="1234")
student.withdraw()          
student.Check_Balance()

   
premium = PremiumSaving(name="rose", balance=249000, secret="1234")
premium.deposit()          
premium.Calculate_Interest()

    
business = BusinessAccount(name="rose", balance=143000, secret="1234")
business.take_loan()        
business.Check_Balance()