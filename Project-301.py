from os import stat
import datetime
import time
from colorama import Fore, init
init()

class Bank:
    service = '';
    # savings_amount = 10000;
    def service_selector(self):    
            self.service = int(input(Fore.LIGHTYELLOW_EX + "Choose Your Transaction \n 1-Withdraw \n 2-Deposit \n 3-Balance-Enquiry \n".upper()))
            if self.service == 1:

                return 'Withdraw'
            elif self.service == 2:
                
                return 'deposit '
            
            elif self.service == 3:

                return 'balancecheck'
        
            else:
                print(Fore.RED+"You Choose Wrong Selection".upper())
     
    def withdraw(self,amount):
        if amount > 0:
            if self.savings_amount > amount :
                print(Fore.LIGHTBLUE_EX +"PROCESSING\n")
                time.sleep(1.0)
                self.savings_amount = self.savings_amount - round(amount,2)
                print(Fore.GREEN +"\nWithdrawel Successfully Completed".upper())
                return amount
            
            else:
                print(Fore.RED+"\nThere Is Not Much Money In Your Account".upper())
                return 0
                
        else:
            print(Fore.RED+"\nREQUESTED AMOUNT CANNOT BE WITHDRAW, PLEASE ENTER A PROPER AMOUNT")
            return 0
                      
    def deposit(self,amount):
        if(amount > 0):
            print(Fore.LIGHTBLUE_EX +"PROCESSING\n")
            time.sleep(1.0)
            self.savings_amount = self.savings_amount + round(amount,2)
            print(Fore.GREEN +"Successfully Deposited To Your Account".upper())      
            return amount
        else:
            print(Fore.RED+"Enter A Proper Amount For Deposit".upper()) 
            return 0
         
    @property
    def currentBalance(self):

        
                print(Fore.LIGHTBLUE_EX + "\nYour Current Balance:".upper(),round(self.savings_amount,2))     
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
          

print(Fore.MAGENTA +"\t\tWelcome to Our Bank".upper())
banking = True
while(banking != False):
    try:
        pin = int(input(Fore.BLUE +"\nEnter Your 4 Digit Pin Number: ".upper()))
        if len(str(pin)) != 4:
            raise TypeError
        if(pin == 1234):
            bank = Bank()
            service = bank.service_selector()
            service = service.upper()
            bank.ReadStatement()
            print(Fore.LIGHTWHITE_EX +"TRANSACTION TYPE: ".upper(),service)
            if service.lower() == 'withdraw':
                
                try:
                    amount = float(input(Fore.LIGHTMAGENTA_EX + "Enter The Amount For Withdrawel: ".upper()))
                    amount = bank.withdraw(round(amount,2))
                    savings = bank.currentBalance
                    if amount!=0:
                        bank.printTransaction(service,amount)
                except  ValueError:
                    print(Fore.RED + "Only Numbers Are Alloweded ".upper())   

                except Exception as e:
                    print(Fore.RED +"Exception caught".upper())
                    print(type(e))
                    
            if service.lower() == 'deposit ':
                amount = float(input(Fore.LIGHTMAGENTA_EX +"Enter The Amount:\n".upper()))
                amount = bank.deposit(round(amount,2))  
                if amount!= 0:   
                    bank.printTransaction(service,amount) 
                bank.currentBalance  
                    
            
            if service.lower() == 'balancecheck':
                bank.currentBalance

        else:
            print(Fore.RED +"\n Enter Your Password Correctly To Use Our Atm Services".upper())
            
        
    except TypeError:
        print(Fore.RED +"Please Enter 4 Digits Number Correctly".upper())
    except ValueError:
        print(Fore.RED +"Only Numbers Are Alloweded".upper())
    except AttributeError:
          print(Fore.RED +"Select The Option Carefully".upper())
    except Exception as e:
        print(Fore.RED +"Exception Was Caught Here".upper())
        print(type(e))
    try:
        banking = int(input(Fore.CYAN +'\nWould You Like To Use Our Atm Service Again?\n 1.Yes \n 2.No\n'.upper()))
    except ValueError:
         print(Fore.RED+"You Choosed Improper Option \nLogin Again To Use Our Services".upper())
         break
    if banking in [1 , 2]:

        if banking == 1:
            banking = True
            continue
        elif banking == 2:
            print(Fore.LIGHTGREEN_EX + "ThankYou for Using our Services".upper())
            banking = False
            break
    else:
        print(Fore.RED+"Don't use Improper Option \nLogin Again To Use Our Services".upper())
        break

       

