# # 1. Create a dictionary and access values
# person = {
#     "name": "Anjali",
#     "age": 25,
#     "city": "Bangalore"
# }
# print(person["age"])
# print(person["name"])
# print(person["city"])
# # print(person["likes"]) # raised keyerror if key doesn't exist

# #2. Add / update / delete a key-value pair

# data={"name":"Somya"}
# print(data)
# #Add
# data["age"]= 25
# print(data)
# #Update
# data["age"]= 26
# print(data)
# #Delete
# del data["age"] 
# print(data)
# data.pop("name")
# print(data)

# #3. Check if a key exists
# data = {"name": "Anjali", "age": 25}
# if "name" in data:
#     print("name exists, and its value is -", data["name"])

# #4. Iterate over keys
# data = {"name": "Anjali", "age": 25}
# for key in data:
#     print(key)
#                  #OR
# for key in data.keys():
#     print(key)

# #4. Iterate over values
# data = {"name": "Anjali", "age": 25}
# for key in data.values():
#     print(key)

# #6. Iterate over key-value pairs(imp)
# data = {"name": "Anjali", "age": 25}
# for key,value in data.items():
#     print(key,value)

# #7Use get()
# data = {"name": "Anjali"}
# print(data.get("name"))
# print(data.get("age"))
# print(data.get("age", 0))
# # data["age"]       # KeyError
# data.get("age")   # None

# data["age"] — use this when you know the key must exist
# data.get("age") — use this when the key might not exist.
# You can also provide a default:
# salary = data.get("salary", 0)
# print(salary)

# #8. Use setdefault()
# # If "errors" exists, give me its value.
# # Otherwise create "errors" with an empty list.
# data = {}

# # Long way:
# if "errors" not in data:
#     data["errors"] = []
# data["errors"].append("500")
# print(data)  # {"errors": ["500"]}

# # Short way with setdefault():
# data = {}
# data.setdefault("errors", [])
# data["errors"].append("500")
# print(data)  # {"errors": ["500"]}

# # get() vs setdefault() vs []
# data = {}

# # [] — expects the key to exist:
# # data["age"]        # KeyError if missing

# # get() — returns value or default, does NOT modify the dictionary:
# print(data.get("age"))      # None
# print(data.get("age", 0))   # 0
# print(data)                 # {} — unchanged

# # setdefault() — returns value, or INSERTS key with default:
# age = data.setdefault("age", 0)
# print(age)     # 0
# print(data)    # {"age": 0}

# # 9. Merge two dictionaries
# a = {"name": "Anjali", "age": 25}
# b = {"city": "Bangalore"}
# result = a | b #creates a new dictionary.
#                   #OR
# a.update(b) #modifies a.
# print(result)
# print(a)

# #10 Copy a dictionary
# data = {"name": "Anjali", "age": 25}
# copy_data = data.copy()
# print(copy_data)
# a = {
#     "numbers": [1, 2, 3]
# }
# print(a)
# b = a.copy()
# print(b)
# b["numbers"].append(4)
# print(a)

#11. Dictionary comprehension
# Create a dictionary from numbers:
# squares = {
#     x: x * x
#     for x in range(1, 6)
# }
# print(squares)
# Create a dictionary from numbers: With condition:
# even = {
#     x: x * x
#     for x in range(1, 6)
#     if x % 2 ==0
# }
# print(even)

#12. Sort dictionary by key
# data = {
#     "banana": 3,
#     "apple": 5,
#     "orange": 2
# }
# result = dict(sorted(data.items()))
# print(result)

#13. Sort dictionary by value
# data = {
#     "apple":5,"watermelon":1,"banana":7,"orange":2
# }
# result = dict(sorted(data.items(), key=lambda item:item[1]))
# print(result)

## IN Descending order
# data = {
#     "apple":5,"watermelon":1,"banana":7,"orange":2
# }
# result = dict(sorted(data.items(), key=lambda item:item[1],reverse = True))
# print(result)

#14. Find key with maximum value
# data = {
#     "A": 10,
#     "B": 50,
#     "C": 20
# }
# key = max(data, key=data.get)
# print(key)
#15. Find key with maximum value
# key_min = min(data, key=data.get)
# print(key_min)

#16. Reverse keys and values
# data = {
#     "A": 1,
#     "B": 2,
#     "C": 3
# }
# result = { 
#     value:key 
#     for key,value in data.items()
#     }
# print(result)
# data1 = {"A": 1, "B": 1}
# result1 = {
#     value:key
#     for key,value in data1.items()
#     }
# print(result1)  # {1: "B"} — "A" got replaced, keys must be unique

# # If duplicate values need to be preserved, use setdefault():
# data2 = {
#     "A": 1,
#     "B": 1,
#     "C": 2
# }
# result2 = {}
# for key, value in data2.items():
#     result2.setdefault(value, []).append(key)
# print(result2)  # {1: ["A", "B"], 2: ["C"]}

# #17. Remove duplicate values, and keep the first occurence
# data = {
#     "A": 10,
#     "B": 20,
#     "C": 10,
#     "D": 30
# }
# result = {}
# for key, value in data.items():
#     if value not in result.values():
#         result[key] = value
# print(result)

# seen = set()
# result = {}

# for key, value in data.items():
#     if value not in seen:
#         result[key] = value
#         seen.add(value)
# print(seen)
# print(result)

# #18. Convert two lists into a dictionary -If lengths differ, zip() stops at the shorter list.
# keys = ["name", "age", "city"]
# values = ["Anjali", 25, "Bangalore","Patna"]
# result = dict(zip(keys,values))
# print(result)

# # If lengths differ, zip() stops at the shorter list:
# keys1 = ["name", "age", "city"]
# values1 = ["Anjali", 25]
# result1 = dict(zip(keys1, values1))
# print(result1)  # {"name": "Anjali", "age": 25} — "city" silently ignored

# # Option 1 — Make unequal lengths an error:
# if len(keys1) != len(values1):
#     raise ValueError("Lists must have the same length")

# # Option 2 — Fill missing values with zip_longest():
# from itertools import zip_longest
# result2 = dict(zip_longest(keys1, values1, fillvalue=None))
# print(result2)  # {"name": "Anjali", "age": 25, "city": None}

# #19. Convert list of tuples into dictionary
# data = [
#     ("name", "Anjali"),
#     ("age", 25),
#     ("city", "Bangalore")
# ]
# result = dict(data)
# print(result)

# #20. Convert dictionary into a list
# data = {
#     "A": 10,
#     "B": 20
# }
# keys = list(data.keys())
# values = list(data.values())
# items = list(data.items())
# print(keys)
# print(values)
# print(items)