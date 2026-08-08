#Variable are dynamically typed in python, so we don't need to declare the type of variable before using it.

n = 10
print('n=', n)  # Output: 10

n = 'Hello'
print('n=', n)  # Output: Hello


#Multiple assignments
a, b, c = 1, 2, 3
print('a=', a, 'b=', b, 'c=', c)  # Output: a= 1 b= 2 c= 3

n,m = 5, 'World'
print('n=', n, 'm=', m)  # Output: n= 5 m= World

#Incrememnting a variable
n = 5
n += 1  # Incrementing n by 1
n = n+1  # Incrementing n by 1
print('n=', n)  # Output: n= 7

#None is a special constant in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value assigned to it.
x = 5
x = None  # Assigning None to x
print('x=', x)  # Output: x= None

#If statement
x = 10
if x > 5:
    print('x is greater than 5')  # Output: x is greater than 5 
elif x == 5:
    print('x is equal to 5')
else:
    print('x is less than 5')


#Parenthesis are optional in if statements, but they can be used for clarity or to group conditions together. For example, the following two if statements are equivalent:  
#and the second one uses parentheses to group the conditions together.
#and = && or = ||
x = 10
if x > 5 and x < 15:
    print('x is between 5 and 15')  # Output: x is between 5 and 15
if (x > 5) and (x < 15) or (x == 20):
    print('x is between 5 and 15 or x is equal to 20')  # Output: x is between 5 and 15 or x is equal to 20 

#LOOPS
#For loop
for i in range(5):  # Looping from 0 to 4
    print('i=', i)  # Output: i= 0, i= 1, i= 2, i= 3, i= 4

#Looping from i=2 to i=6
for i in range(2, 7):  # Looping from 2 to 6
    print('i=', i)  # Output: i= 2, i= 3, i= 4, i= 5, i= 6

#looping from i=6 to i=2
for i in range(6, 1, -1):  # Looping from 6 to 2
    print('i=', i)  # Output: i= 6, i= 5, i= 4, i= 3, i= 2

#looping from i=2 to i=6 with step of 2
for i in range(2, 7, 2):  # Looping from 2 to 6 with step of 2
    print('i=', i)  # Output: i= 2, i= 4, i= 6
    
 #Diviision is decimal by default in python, so we don't need to use float() function to convert the result of division to float.
x = 5
y = 2
z = x / y  # Division
print('z=', z)  # Output: z= 2.5

# Double SLash rounds down the result of division to the nearest whole number. It is also known as floor division.
x = 5
y = 2
z = x // y  # Floor Division
print('z=', z)  # Output: z= 2

#Defaults so negative no will round down to the next lowest whole number. For example, -5 // 2 will give -3 because -3 is the next lowest whole number after -2.5.
x = -5
y = 2
z = x // y  # Floor Division
print('z=', z)  # Output: z= -3
print(int(-5 / 2))  # Output: -2

#Modding operator returns the remainder of the division of two numbers. For example, 5 % 2 will give 1 because 5 divided by 2 is 2 with a remainder of 1.
x = 5
y = 2
z = x % y  # Modulus
print('z=', z)  # Output: z= 1  

a=-5
b=2
c=a%b
print('c=', c)  # Output: c= 1
#here, -5 divided by 2 is -3 with a remainder of 1. So, the result of -5 % 2 is 1.
#you can use math.fmod() function to get the same result as the modding operator. For example, math.fmod(-5, 2) will give -1 because -5 divided by 2 is -3 with a remainder of -1.
import math 
print('math.fmod(-5, 2)=', math.fmod(-5, 2))  # Output: math.fmod(-5, 2)= -1.0
print(math.floor(-5 / 2))  # Output: -3
print(math.floor(5 / 2))
print(math.ceil(5 / 2))  # Output: 3

#Maximum and Minimum
x = 5
y = 2
z = max(x, y)  # Maximum
print('z=', z)  # Output: z= 5
float_num = 3.14
int_num = 3
max_num = max(float_num, int_num)  # Maximum
print('max_num=', max_num)  # Output: max_num= 3.14

float('inf')  # Output: inf
float('-inf')  # Output: -inf

#python no are infinite so they never overflow. For example, 1e1000 will give inf because 1e1000 is greater than the maximum value that can be represented by a float in python.
x = 1e1000
print('x=', x)  # Output: x= inf

import math
print(math.pow(2, 1000))  # Output: 1.0715086071862673e+301


#Arrays in python are called lists. Lists are mutable, which means that you can change the elements of a list after it has been created. Lists can contain elements of different data types, including other lists. Lists are ordered, which means that the elements of a list have a specific order and can be accessed using their index.
#Lists are created using square brackets [] and elements are separated by commas. For example, the following code creates a list of integers:
my_list = [1, 2, 3, 4, 5]
print('my_list=', my_list)  # Output: my_list= [1, 2, 3, 4, 5]
#You can access the elements of a list using their index. The index of the first element is 0, the index of the second element is 1, and so on. For example, the following code accesses the first element of my_list:
print('my_list[0]=', my_list[0])  # Output: my_list[0]= 1
#You can change the elements of a list using their index. For example, the following code changes the first element of my_list to 10:
my_list[0] = 10
print('my_list=', my_list)  # Output: my_list= [10, 2, 3, 4, 5]
#You can add elements to a list using the append() method. For example, the following code adds the element 6 to my_list:
my_list.append(6)
print('my_list=', my_list)  # Output: my_list= [10, 2, 3, 4, 5, 6]
#You can remove elements from a list using the remove() method. For example, the following code removes the element 2 from my_list:
my_list.remove(2)
print('my_list=', my_list)  # Output: my_list= [10, 3, 4, 5, 6]
#You can get the length of a list using the len() function. For example, the following code gets the length of my_list:         
my_list.pop()  # Removes the last element from my_list
print('my_list=', my_list)  # Output: my_list= [10, 3, 4, 5]
print('len(my_list)=', len(my_list))  # Output: len(my_list)= 4 
