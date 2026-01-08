# #Q1
# list_1=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in list_1:
#     if i%2==0:
#         sum+=i
        
# print(sum)

# #Q2
# tuple_1=(10,20,30,40,50)

# print(tuple_1[2:])

# #Q3
# set_1={1,2,3,4,5}
# set_2={4,5,6,7}

# print(set_1 & set_2)

# #Q4
# dict_1={'a':1,'b':2,'c':3}
# dict_1['b']=10

# print(dict_1)

# #Q5
# sqr=[x**2 for x in range(1,6)]    #list comprehension

# print(sqr)

# #Q6
# tuple_1=('cat','dog','bird')
# if 'dog' in tuple_1:
#     print("Success")
# else:
#     print('Oops!')

# #Q7
# list_1=[1,1,2,3,5,8,13]
# set_1=set(list_1)

# print(set_1)

# #Q8
# dict_1={'A':[1,2],'B':[3,4]}
# dict_2={'C':[5,6],'D':[7,8]}
# dict_3=dict_1 | dict_2

# print(dict_3)

# #Q9
# list_1=[3,5,7,3,5,9,3]

# for i in list_1:

    
    
# #Q10
# tuple_1=(1,2,3,4,5)

# print(max(tuple_1))
# print(min(tuple_1))

# #Q11
# import statistics
# import math

# list=[12,15,18,20,22,25,30]

# print(round(statistics.variance(list),2))

# #Q12
# dict_1={'apple':150,'banana':60,'peaches':120}
# total=0
# for i in dict_1:
#     total+=dict_1.get(i, 0)
# print(total)

# #Q13
# list_1=[22,25,19,30,28,32,26]

# print(max(list_1))
# print(min(list_1))

# #Q14
# list_1 = [(90, 'Alice'), (85, 'Bob'), (88, 'Charlie')]

# max_marks, max_student = max(list_1)
# print(f"Max marks: {max_marks}, Student: {max_student}")

# #Q15
# list_1=[2,4,6,8,10]
# sum=0
# for i in list_1:
#     sum+=i

# print(sum)

# #Q16
# sqr=[x**2 for x in range(1,11)]    #list comprehension

# print(sqr)

# #Q17
# list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# for i in list_1:
#     if i%15==0:
#         print("FizzBuzz")
#         pass
#     elif i%3==0:
#         print('Fizz')
#         pass
#     elif i%5==0:
#         print('Buzz')

# #Q18
# list_1=list(range(1,101))
# list_2=[]

# for i in list_1:
#     if i%10==0:
#         list_2.append(i)

# print(list_2)

#Q19
# dict_1={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
# dict_2={}

# for i in dict_1:
#     dict_2[i]=set(dict_1[i])

# print(dict_2)


#Q23
list_1=[(1,2,3,4),(5,6,7,8)]

position=int(input("enter a number: "))

result=[]
for i in list_1:
    lexi=list(i)
    rotated_list=lexi[position:]+lexi[:position]
    result.append(tuple(rotated_list))
print(f"The rotated list is: {result}")    
    
        
    
        
