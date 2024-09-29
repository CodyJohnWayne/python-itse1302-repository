investment_amount = int(input("Enter Investment Amount: "))
while investment_amount < 0 or investment_amount > 50000:
    print('Error: Enter Amount Between 0 and 50000')
    investment_amount = int(input('Enter Investment Amount: '))
interest_rate = int(input('Enter Interest Rate: '))
while interest_rate <0 or interest_rate > 15:
    print('Error: Enter Rate Between 0 and 15')
    interest_rate = int(input('Enter Interest Rate: '))
duration = int(input('Enter Investment Duration in Years: '))
while duration < 0:
    print('Error: Enter Duration in Years More than 0')
    duration = int(input('Enter Investment Duration in Years: '))
monthly_rate = (interest_rate/12)/100
months = duration * 12
future_value = 0
for i in range (1, months +1):
    future_value += investment_amount
    interest = future_value * monthly_rate
    future_value += interest
    if i % 12 == 0:
        print('Year', i//12 , ':', round(future_value, 2))
print()
print('Investment Duration: ',duration, 'years')
print('Yearly Interest Rate: ',interest_rate,'.0%')
print('Monthly Investment Amount: $',investment_amount)
print('Total Amount of Investment After Compounding: $', round(future_value,2))
print()
print('Created by, Cody Hobbs')

      
