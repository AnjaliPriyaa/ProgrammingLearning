#1. Take a number as input and print it.

number = int(input('Enter a Number: '))
print(number)
print(type(number))

#2. Take a string as input and print it.

string = input('Enter a string: ')
print(string)
print(type(string))

#3. Take multiple numbers from the user and store them in an array.

multiple_numbers = list(map(int, input("Enter numbers separated by space: ").split())) #"12 23 34 56 78" , ["12", "23", "34", "56", "78"] ,[12, 23, 34, 56, 78]
print(type(multiple_numbers))
print(multiple_numbers)
print(multiple_numbers[0])

# 4. Take n numbers from the user and print them.

n = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)
print(numbers)

# 5. Take multiple strings from the user and store them in an array.

s =  input("Enter multiple separated by space: ")
print(s)
print(type(s))
list_string = s.split()
print(list_string[3])

# 6. Concatenate two strings. (Combine Two Strings)
s1 = input('enter a string: ')
s2 = input('enter a string: ')
s3 = s1+ ' ' +s2
s4 = f"{s1} Loves {s2}"
print(f"{s1} Loves {s2}")
print(s3)
print(s4)
print(type(s3))

# 7. Merge two arrays.
array1 = list(map(int, input('Enter No for an array1: ').split()))
array2 = input("Enter String for an array2: ").split()
array3 = array1 + array2
print(array3)
array1+=array2
print(array1)

# 8. Find the length of a string without using len().
s = input('Enter a string: ')
print(s)
print(len(s))

# 9. Find the length of an array without using len().
array1 = list(map(int, input('Enter No for an array1: ').split()))
array2 = input("Enter String for an array2: ").split()
array1+=array2
count = 0
for i in array1:
    count +=1
print(count)


# 10. Print each element of an array on a separate line.
array = input("Enter String for an array: ").split()
print(array)
for i in range(len(array)):
    print(array[i])

# 11. Print an array in reverse order.(Use Append and Pop for list )
array = input("Enter String for an array: ").split()
print(array[::-1])
array2=[]
for i in range(len(array)):
    print(i)
    # array2+=[array[len(array)-i-1]]
    array2.append(array[len(array)-i-1])
print(array2)

# 12. Print a string in reverse order.
s = input("Enter String: ")
print(s[::-1])
s2=[]
for i in range(len(s)):
    print(i)
    s2+=[s[len(s)-i-1]]
print(s2)

# 13. Swap two numbers without using a third variable.
a=15
b=33
print(a)
print(b)
a,b=b,a
print(a)
print(b)

#14. Find the largest of three numbers.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number:", largest)