no_of_units=int(input('Please enter number of units consumed: '))
if no_of_units<=100:
    bill_amount=0
    print('No charge')
elif no_of_units<=200:
    bill_amount=(no_of_units-100)*5
    print('Bill amount is:',bill_amount)
elif no_of_units>200:
    bill_amount=100*5+(no_of_units-200)*10
    print('Bill amount is:',bill_amount)