# sort() → modifies the original list.
# sorted() → creates and returns a new sorted list.
#55. Sort an array using built-in methods.
# input_array = [12, 45, 7, 89, 23, 56, 34]
# input_array.sort(reverse=True)
# print(input_array)

# #56. Sort an array without modifying the original array.
# input_array = [12, 45, 7, 89, 23, 56, 34]
# new = sorted(input_array)
# print(new)

# 57. Sort an array in descending order.
# input_array = [12, 45, 7, 89, 23, 56, 34]
# new = sorted(input_array,reverse=True)
# print(new)

# 58. Sort an array of strings alphabetically.
input_array1 = ["d", "a", "c", "f", "b", "e"]
input_array2 = ["banana", "apple", "orange", "grape", "mango", "kiwi"]
for i in input_array1:
    newarray1= sorted(input_array1)
for i in input_array2:
    newarray2= sorted(input_array2)
print(newarray1)
print(newarray2)

# 59. Sort an array based on string length.
# 60. Sort an array of tuples based on the second element.
# 61. Sort an Array of Dictionaries by a Key
employees = [
    {"name": "Anjali", "age": 32},
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 29},
    {"name": "Amit", "age": 22}
]

# 64. Find the kth largest element.
# 65. Find the kth smallest element