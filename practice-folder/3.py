numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
oddNumbers = 0
evenNumbers = 0
for i in range(1, 10):
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
print("Number of even numbers:", evenNumbers)
print("Number of odd numbers:", oddNumbers)
