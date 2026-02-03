#importing sys library
import sys

#account balance 
account_balance = float(500.25)

#Custom function that returns the current balance including 2 decimal places
def printbalance():
    print("Your current balance : %.2f" % account_balance)

#the function for deposit is a custom function
def deposit():
    deposit_amount = float(input("How much would you like to deposit today? \n "))
    balance = account_balance + deposit_amount #calculates balance
    print("Deposit was $%.2f, current balance is $%.2f" % (deposit_amount, balance))#prints out balance

#function for withdraw is a custom function
def withdraw():
    withdraw_amount = float(input("How much would you like to withdraw today? \n")) #takes withdraw_amount
    if(withdraw_amount > account_balance): # checks if requested withdrawal amount is greater than balance
        print("$%.2f is greater than your account balance of $%.2f" %(withdraw_amount,account_balance)) #if it is it states the comparison
    else:
        balance = account_balance - withdraw_amount
        print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdraw_amount, balance))
#User Input parameters
userchoice = input("What would you like to do?\n")
#User input is determines the function 
if (userchoice == 'D'):#deposit function is called
  deposit() 
elif userchoice == 'W':#withdraw function is called
  withdraw() 
elif userchoice == 'B':#balance function is called
  printbalance() 
else:
  print("Thank You for banking with us.\n")
