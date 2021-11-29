from os import stat
import datetime


class Bank:
    service = '';
    # savings_amount = 10000;
    def service_switch(self):
        self.service = input("Choose Your bank option \n 1-Withdraw \n 2-Deposit \n 3-Balance-Enquiry \n")
        if self.service == '1':

            return 'Withdraw'
        elif self.service == '2':
            
            return 'deposit'
        
        elif self.service == '3':

            return 'b'
      
        else:
            print("You choose wrong selection")
            return 0    

    def withdraw(self,amount):
        if amount > 0:
            if self.savings_amount > amount :
                self.savings_amount = self.savings_amount - amount
                print("Withdrawel successfully completed")
            
            else:
                print("There is not much money in your account")
        else:
            print("Enter a proper amount to withdraw")
            
    def deposit(self,amount):
        self.savings_amount = self.savings_amount + amount
        print("Successfully Deposited to your account")       
         
    @property
    def currentBalance(self):
        with open('bankBalanceStatement.text','r') as file:
            print("Your Current Balance:",self.savings_amount)     
            return self.savings_amount
        
    
    def ReadStatement(self):
        with open("bankBalanceStatement.text","r") as file:
          statement = file.readlines()
          for balanceSheet in statement:
              if "Current" in balanceSheet:
                number = balanceSheet.split()
                self.savings_amount = float(number[-1])
                # print(number[-1])    
        # print("Current Balance: ",self.savings_amount)
            


    def printTransaction(self):
    
        balance = [self.savings_amount,]
        current_time = datetime.datetime.now()
        with open('bankBalanceStatement.text','w') as file:
            file.write("\t\t\tService Bank\t\t\n")
            file.write(f"{current_time.hour}:{current_time.minute}:{current_time.second}\t\t\t\t\t\t{current_time.day}/{current_time.month}/{current_time.year}\n\n")

            file.write(f"Current Balance: {self.savings_amount}")
            #   file.write(self.savings_amount)


print("Welcome to Our Bank")
banking = True
while(banking != False):
    try:
        pin = int(input("Enter Your 4 digit pin Number: "))
        if len(str(pin)) != 4:
            raise TypeError
        bank = Bank()
        service = bank.service_switch()
        bank.ReadStatement()
        print("Service option ",service)
        if service.lower() == 'withdraw':
            
            try:
                amount = float(input("Enter the amount for the withdrawel: "))
                bank.withdraw(amount)
                savings = bank.currentBalance
                bank.printTransaction()
                # bill = input("Would you like to print the reciept of the transaction \n 1.Yes \n 2.No \n ")
                # if bill in ['1', '2']:
                #     if bill == '1':
                #         bank.printTransaction()
                #     else:
                #         pass
                # else:
                #     print("Choose Proper Option")
                
            except Exception as e:
                print("Exception caught")
                print(type(e))
                
        if service.lower() == 'deposit':
            amount = float(input("Enter the amount:\n"))
            bank.deposit(amount)     
            bank.printTransaction() 
            bank.currentBalance  
                
        
        if service.lower() == 'b':
            print("Second")
            bank.currentBalance
            
        
    except TypeError:
        print("Please Enter 4 digits number correctly")
    except ValueError:
        print("Only 4 digit numbers are alloweded")
    except Exception as e:
        print("Exception was caught")
        print(type(e))
    
    banking = int(input('Would you like to continue bank transaction?\n 1.Yes \n 2.No\n'))
    if banking == 1:
        banking = True
        continue
    else:
        banking = False
        break

