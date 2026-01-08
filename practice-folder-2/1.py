print(len('Hello World'))
print(('Python Programming').upper())
str='Data'+' '+'Science'
print(str)
str2=' Data Analysis '
print(str2.strip())
str3='level'
for i in range(len(str3)+1):
    if str3[:i]==str3[:i][::-1]:
        print(str3,'is a palindrome')
        break
    else:
        print(str3,'is not a palindrome')
        break

str4='machine learning'
splitted=str4.split()
for split in splitted:
    if len(split)%2==0:
        print(split,'has even length')