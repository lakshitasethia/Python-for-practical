str='Hello'
print(str[::-1])

start=int(input('Enter start index: '))
end=int(input('Enter end index: '))
print(str[start:end])

str2='Data Science'
q=str2.split()
count=0
for split in q:
    print(split)
    count+=1
print('Number of words:',count)
delimiter=input('Enter a delimiter: ')
print(delimiter.join(q))