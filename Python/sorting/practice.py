# sort() → modifies the original list.
# sorted() → creates and returns a new sorted list.
# 55. Sort an array using built-in methods.
input_array = [12, 45, 7, 89, 23, 56, 34]
input_array.sort(reverse=True)
print(input_array)

#56. Sort an array without modifying the original array.
input_array = [12, 45, 7, 89, 23, 56, 34]
new = sorted(input_array)
print(new)

# 57. Sort an array in descending order.
input_array = [12, 45, 7, 89, 23, 56, 34]
new = sorted(input_array,reverse=True)
print(new)

# 58. Sort an array of strings alphabetically.
input_array1 = ["d", "a", "c", "f", "b", "e"]
input_array2 = ["banana", "apple", "orange", "grape", "mango", "kiwi"]
newarray1= sorted(input_array1)
newarray2= sorted(input_array2)
print(newarray1)
print(newarray2)
#Bubble Sort
def bubblesort(input_array1):
    for i in range(len(input_array1)):
        for j in range(len(input_array1) - 1 - i):
            if input_array1[j]>input_array1[j+1]:
                input_array1[j],input_array1[j+1] = input_array1[j+1],input_array1[j]
    return input_array1
print(bubblesort(input_array1))

def bubblesort(input_array2):
    for i in range(len(input_array2)):
        for j in range(len(input_array2) - 1 - i):
            if input_array2[j]>input_array2[j+1]:
                input_array2[j],input_array2[j+1] = input_array2[j+1],input_array2[j]
    return input_array2
print(bubblesort(input_array2))

# (imp)59. Sort an array based on string length.
input_array = ["apple", "hi", "banana", "cat", "a", "elephant"]
def sortarraywithlength(input_array):

    for i in range(len(input_array)):
        for j in range(len(input_array) - 1 - i):
            if len(input_array[j])>len(input_array[j+1]):
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]
    return input_array

print(sortarraywithlength(input_array))

# (imp)60. Sort an array of tuples based on the second element.
input_array = [
    ("apple", 5),
    ("banana", 2),
    ("orange", 8),
    ("grape", 3),
    ("mango", 6)
]
def sorttuple(input_array):
    for i in range(len(input_array)):
        for j in range(len(input_array) - 1 - i):
            if input_array[j][1] > input_array[j+1][1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]
    return input_array
print(sorttuple(input_array))

# 61. Sort an Array of Dictionaries by a Key
employees = [
    {"name": "Anjali", "age": 32},
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 29},
    {"name": "Somya", "age": 22}
]
def sortdictionarybykey(employees):
    key = "age"
    for i in range(len(employees)):
        for j in range(len(employees) - 1 - i):
            if employees[j][key] > employees[j+1][key]:
                employees[j],employees[j+1] = employees[j+1],employees[j]
    return employees       
print(sortdictionarybykey(employees))


#(imp) 64. Find the kth largest element.
#Question: Given an array of numbers and an integer k, find the kth largest element in the array.
input_array = [3, 2, 1, 5, 6, 4]
k = 3 # k starts from 1
def kthlargest(input_array,k):
    n = len(input_array)
    for i in range(n):
        for j in range(n - 1 - i):
            if input_array[j] > input_array[j+1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]
    return input_array[n-k]
print(kthlargest(input_array,k))   

input_array = [3, 2, 1, 5, 6, 4]
k = 3 # k starts from 0
def kthlargest(input_array,k):
    n = len(input_array)
    for i in range(n):
        for j in range(n - 1 - i):
            if input_array[j] > input_array[j+1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]
    return input_array[n-1-k]
print(kthlargest(input_array,k))   
#65. Find the kth smallest element
input_array = [3, 2, 1, 5, 6, 4]
k = 1 #starts with 0
def kthsmallest(input_array,k):
    n = len(input_array)
    for i in range(n):
        for j in range(n - 1 - i):
            if input_array[j] > input_array[j+1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]
    return input_array[k]
print(kthsmallest(input_array,k))  

input_array = [3, 2, 1, 5, 6, 4]
k = 2  #starts with 1
def kthsmallest(input_array,k):
    n = len(input_array)
    for i in range(n):
        for j in range(n - 1 - i):
            if input_array[j] > input_array[j+1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j]
    return input_array[k-1]
print(kthsmallest(input_array,k))  