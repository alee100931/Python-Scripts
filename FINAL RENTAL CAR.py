import sys
#rentalCode is a variable assigned to a value the user will input
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
#the if branch conditions change the prompt of the user 
#dependent on their answer of either B D or W
if rentalCode == 'B' or rentalCode == 'D':
  rentalPeriod = input("Number of Days Rented:\n")
else:
  rentalPeriod = input("Number of Weeks Rented:\n")

# the charges here are examples assigning a numerical 
# value to the three variable charges
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00	
#if branches here are to apply different conditions to the baseCharge dependent on
# the rentalCode type; B D or W
if rentalCode == 'B':
  baseCharge = int(rentalPeriod) * budgetCharge
elif rentalCode == 'D':
  baseCharge = int(rentalPeriod) * dailyCharge
else:
  baseCharge = int(rentalPeriod) * weeklyCharge

odoStart = input("Starting Odometer Reading:\n")
#odoStart is a variable assigned to a changing value based on the user input
odoEnd = input("Ending Odometer Reading:\n")
#totalMiles is an example of assigning a variable to a string of operators
totalMiles = int(odoEnd) - int(odoStart)
#the if branches below apply conditions to the charges dependent on the 
#miles traveled which change dependent on the input of B D W
if rentalCode == 'B':
  mileCharge = totalMiles * 0.25 #if the code was budget then it only calculates the total driven by .25
elif rentalCode == 'D': #if charge was Daily, it calculates the average daily miles. 
  averageDayMiles = int(totalMiles) / int(rentalPeriod) #if the average is lower than 100 a day there is no additional charge
  if averageDayMiles > 100: #otherwise it calculated how over 100 the daily miles is and times the extra by .25
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25
  else:
    mileCharge = 0.0
else:
  averageWeekMiles = totalMiles/ rentalPeriod #if the code was Weekly, we calculate the average week miles.
  if averageWeekMiles > 900: #if it is over 900 miles a week we calculate the extraMiles by subtrated the average from 900
    extraMiles = averageWeekMiles - 900
  else: 
    mileCharge =0.0#otherwise there is no charge
#amountDue variable is assigned to a data type operators    
amtDue = baseCharge + mileCharge
print("Rental Summary")
print("Rental Code:",rentalCode) 
print("Rental Period:", rentalPeriod)
print("Starting Odometer:", odoStart)
print("Ending Odometer:", odoEnd)
print("Miles Driven:", totalMiles)
print("Amount Due:","$""%0.2f" %amtDue)
