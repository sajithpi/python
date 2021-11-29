from os import stat
import datetime
import time
from colorama import Fore, init
init()


class Bank:
    service = '';
    # savings_amount = 10000;
    def service_switch(self):    
            self.service = int(input(Fore.LIGHTYELLOW_EX + "Choose Your bank option \n 1-Withdraw \n 2-Deposit \n 3-Balance-Enquiry \n"))
            if self.service == 1:

                return 'Withdraw'
            elif self.service == 2:
                
                return 'deposit '
            
            elif self.service == 3:

                return 'balancecheck'
        
            else:
                print(Fore.RED+"You choose wrong selection")
     
      

    def withdraw(self,amount):
        if amount > 0:
            if self.savings_amount > amount :
                print(Fore.LIGHTBLUE_EX +"Processing\n")
                time.sleep(1.0)
                self.savings_amount = self.savings_amount - amount
                print(Fore.GREEN +"\nWithdrawel successfully completed")
                return amount
            
            else:
                print(Fore.RED+"\nThere is not much money in your account")
                
        else:
            print(Fore.RED+"\nEnter a Proper Amount to Withdraw")
          
            
    def deposit(self,amount):
        if(amount > 0):
            print(Fore.LIGHTBLUE_EX +"Processing\n")
            time.sleep(1.0)
            self.savings_amount = self.savings_amount + amount
            print(Fore.GREEN +"Successfully Deposited to your account")      
            return amount
        else:
            print(Fore.RED+"Enter a proper amount for deposit") 
         
    @property
    def currentBalance(self):

        
                print(Fore.LIGHTBLUE_EX + "\nYour Current Balance:",self.savings_amount)     
                return self.savings_amount
        
         
    def ReadStatement(self):
        with open("bankBalanceStatement.text","r") as file:
          statement = file.readlines()
          for balanceSheet in statement:
              if "Current" in balanceSheet:
                number = balanceSheet.split()
                self.savings_amount = float(number[-1])

              else:
                  self.savings_amount = 0.00
                  


    def printTransaction(self,serviceType,amount):
    
     
        current_time = datetime.datetime.now()
        with open('bankBalanceStatement.text','a') as file:
            file.write(f"\n{current_time.day}/{current_time.month}/{current_time.year}\t\t\t{current_time.hour}:{current_time.minute}:{current_time.second} ")       
            file.write(f"\t\t\t{serviceType}\t\t{amount}\t\t\tCurrent Balance: {self.savings_amount}\n")
          


print(Fore.MAGENTA +"\t\tWelcome to Our Bank")
banking = True
while(banking != False):
    try:
        pin = int(input(Fore.BLUE +"\nEnter Your 4 digit pin Number: "))
        if len(str(pin)) != 4:
            raise TypeError
        if(pin == 1234):
            bank = Bank()
            service = bank.service_switch()
            service = service.upper()
            bank.ReadStatement()
            print(Fore.WHITE +"Service option ",service)
            if service.lower() == 'withdraw':
                
                try:
                    amount = float(input(Fore.LIGHTMAGENTA_EX + "Enter the amount for the withdrawel: "))
                    amount = bank.withdraw(amount)
                    savings = bank.currentBalance
                    bank.printTransaction(service,amount)
                except  ValueError:
                    print(Fore.RED + "Only Numbers are alloweded ")   

                except Exception as e:
                    print(Fore.RED +"Exception caught")
                    print(type(e))
                    
            if service.lower() == 'deposit ':
                amount = float(input(Fore.LIGHTMAGENTA_EX +"Enter the amount:\n"))
                amount = bank.deposit(amount)     
                bank.printTransaction(service,amount) 
                bank.currentBalance  
                    
            
            if service.lower() == 'balancecheck':
                bank.currentBalance

        else:
            print(Fore.RED +"\n Enter Your Password Correctly To Use Our Atm Services")
            
        
    except TypeError:
        print(Fore.RED +"Please Enter 4 digits number correctly")
    except ValueError:
        print(Fore.RED +"Only numbers are alloweded")
    except AttributeError:
          print(Fore.RED +"Select the option carefully")
    except Exception as e:
        print(Fore.RED +"Exception was caught hetr")
        print(type(e))
    try:
        banking = int(input(Fore.CYAN +'\nWould you like to use our atm service again?\n 1.Yes \n 2.No\n'))
    except ValueError:
         print(Fore.RED+"You Choosed Improper Option \nLogin again to use our services")
         break
    if banking in [1 , 2]:

        if banking == 1:
            banking = True
            continue
        elif banking == 2:
            print(Fore.LIGHTGREEN_EX + "ThankYou for Using our Services using repo")
            banking = False
            break
    else:
        print(Fore.RED+"Don't use Improper Option \nLogin again to use our services")
        break

       

