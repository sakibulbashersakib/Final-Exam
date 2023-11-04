class User:
    def __init__(self,name,email,address,accountType,accNum) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.accountType=accountType
        self.accNum=accNum
        self.balance=0
        self.trasHistory_deposite=[]
        self.trasHistory_withdrawal=[]

class Admin:
    def __init__(self,name,password) -> None:
        self.name=name
        self.password=password

class Bank:
    account_list=[]
    account_admin=[]
    def __init__(self) -> None:
        self.totalBalance=0
        self.totalLoan=0
        self.loan_status=True
        self.bankrupt=False
        self.loan_times=2

    def admin(self,name,password):
        user=Admin(name,password)
        self.account_admin.append(user)

    def creat_account(self,name,email,address,accountType,accNum):
        user=User(name,email,address,accountType,accNum)
        Bank.account_list.append(user)
        return user
    
    def deleteAcc(self,accNum):
        for acc in Bank.account_list:
            if acc.accNum==accNum:
                Bank.account_list.remove(acc)
        print(f"\n{accNum} Account is delete\n")
    
    def showUser(self):
        for acc in Bank.account_list:
            print(f"\n-->Account Number: {acc.accNum} > Name: {acc.name} > Email: {acc.email} > Address: {acc.address} > Type: {acc.accountType}\n")
    
    def total_balance(self):
        print(f"\n-->Total Balance {self.totalBalance}")
    
    def total_loan(self):
        print(f"\nThe total loan is: {self.totalLoan}")
    
    def loan_feature(self,lo):
        if lo=="Off":
            self.loan_status=False
            print("\nLoan feature is off by admin\n")
        else:
            self.loan_status=True
    
    def bank_rupt(self,br):
        if br=="Yes":
            self.bankrupt=True
            print("\nThe bank is bankrupt\n")
        else:
            self.bankrupt=False

    # ..........user..........

    def deposite(self,user,amount):
        if amount>=0:
            user.balance+=amount
            self.totalBalance+=amount
            user.trasHistory_deposite.append(amount)
            print(f"\nDeposited {amount}. New balance: {user.balance}\n")
            return
        else:
            print("\nInvalid deposit amount\n")

    def withdraw(self,user, amount):
        if self.bankrupt==False:
            if amount >= 0 and amount <= user.balance:
                user.balance -= amount
                user.trasHistory_withdrawal.append(amount)
                print(f"\nWithdrew {amount}. New balance: {user.balance}\n")
                return
            else:
                print("\nWithdrawal amount exceeded\n")
                return
        else:
            print("\nThe bank is bankrupt\n")

    def balance(self,user):
        print(f"\nYour balance is {user.balance}\n")
    
    def tra_history(self,user):
        print("\nThe deposite History")
        for val in user.trasHistory_deposite:
            print(val)
        print("\nThe withdrawal History")
        for val in user.trasHistory_withdrawal:
            print(val)

    def take_loan(self,user,amount):
        if self.loan_status==True:
            if self.loan_times>0:
                user.balance+=amount
                self.totalLoan+=amount
                self.loan_times-=1
                print(f"\nTake loan: {amount}. Now balance is: {user.balance}\n")
                return
            else:
                print("\nSorry! You can not take loan more than two times\n")
        else:
            print("\nSorry! Admin off the loan feature\n")
    def transfer(self,user,accNum,amount):
        if self.bankrupt==False:
            if amount<=user.balance:
                for acc in Bank.account_list:
                    if acc.accNum==accNum:
                        user.balance-=amount
                        acc.balance+=amount
                        print(f"\nTransfer: {amount}. Now balance is: {user.balance}")
                        return
                    else:
                        print("\nAccount does not exist\n")
                        return
            else:
                print("\nSorry! Amount exceeded\n")
                return
        else:
            print("\nThe bank is bankrupt\n")


bkash=Bank()
admin=bkash.admin("Admin",123)

currentUser=None
while True:
    flag=0
    print("\n--------Welcome To Bank------------\n")
    person=input("\nWho are you? (Admin/User) :")
    if person=="Admin":
        password=int(input("Enter your password :"))
        if password==123:
            print("\n--------Welcome Admin-----------\n")
            while True:
                print("\n-->Option: \n")
                print("1. Creat Account ")
                print("2. Delete Account ")
                print("3. Show User")
                print("4. Show Total Balance")
                print("5. Show total loan")
                print("6.Loan Featur(On/Off)")
                print("7.Bankrupt(Yes/No)")
                print("8.logout")
                op=int(input("\nEnter your option: "))
                if op==1:
                    name=input("Enter name: ")
                    email=input("Enter email: ")
                    address=input("Enter address: ")
                    account_type=input("Enter account type(seaving/Current) ")
                    accNum=f"{name}-{len(Bank.account_list)+1}"
                    bkash.creat_account(name,email,address,account_type,accNum)
                elif op==2:
                    accNum=input("\nEnter Delete Account Number: ")
                    bkash.deleteAcc(accNum)
                elif op==3:
                    bkash.showUser()
                elif op==4:
                    bkash.total_balance()
                elif op==5:
                    bkash.total_loan()
                elif op==6:
                    loan=input("\nLoan featur (On/Off): ")
                    bkash.loan_feature(loan)
                elif op==7:
                    br=input("Bankrupt(Yes/No): ")
                    bkash.bank_rupt(br)
                elif op==8:
                    break
                
                else:
                    print("\nSorry! Enter valid option.\n")
                currentUser=None
        else:
            print("\nPlease enter correct password.\n")

    elif person=="User":
        print("\n---- No user logged in !----")
        ch=input("\n Register/Login (R/L) : ")
        if ch=="L":
            accNum=input("Account Number: ")
            for account in Bank.account_list:
                if account.accNum==accNum:
                    currentUser=account
                    flag=1
                    break

        elif ch=="R":
            name=input("Enter your name: ")
            email=input("Enter your email: ")
            address=input("Enter your address: ")
            account_type=input("Enter your account type(seaving/Current) ")
            accNum=f"{name}-{len(Bank.account_list)+1}"
            currentUser=bkash.creat_account(name,email,address,account_type,accNum)
            flag=1

        if flag==1:
            print(f"\n---------Welcome {currentUser.name}-----------\n")
            while True:
                print("-->Option ")
                print("1. Deposite")
                print("2. Withdraw")
                print("3. Check availaable balance")
                print("4. Check Transaction history")
                print("5. Take loan")
                print("6. Money transfer")
                print("7.Logout")
                op=int(input("\nEnter your option: "))
                if op==1:
                    amount=int(input("Enter the amount of deposite money: "))
                    bkash.deposite(currentUser,amount)
                elif op==2:
                    amount=int(input("Enter the amount of withdrawl money: "))
                    bkash.withdraw(currentUser,amount)
                elif op==3:
                    bkash.balance(currentUser)
                elif op==4:
                    bkash.tra_history(currentUser)
                elif op==5:
                    amount=int(input("Enter the amount of loan: "))
                    bkash.take_loan(currentUser,amount)
                elif op==6:
                    accNum=input("Enter account number: ")
                    amount=int(input("Enter transfer amount: "))
                    bkash.transfer(currentUser,accNum,amount)
                elif op==7:
                    break
                else:
                    print("Sorry! Enter valid option")
        elif flag==0:
            print("\nPlease Registation fast\n")
    else:
        print("\nPlease select correct person.\n")