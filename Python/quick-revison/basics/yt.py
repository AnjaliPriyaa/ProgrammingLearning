#Looping over a range of Numbers
#FOR - Loop Over Collections
for i in [0,1,2,3,4,5]:
    print (i**2)

for i in range(6):
    print (i**2)

#Looping over collections:
colors = ['red','green','blue','yellow']
"""
Don't do this
for i in range(len(colors)):
    print(colors[i])
"""
for color in colors:
    print(colors)

#Looping Backwards
for i in range(len(colors)-1,-1,-1):
    print(colors[i])

for color in reversed(colors):
    print(color)

#Looping over a collection an indices
"""for i in range(len(colors)):
    print(i, '--->', colors[i])"""

for i,color in enumerate(colors):
    print(i, '--->', colors[i])

#Looping over a two collection an indices at once
names = ['raymond','priya','anjali']
colors = ['red','green','blue','yellow']

"""n = min(len(names),len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])"""

for name,color in zip(names,colors):
    print(name, '--->', color)

"""for name,color in izip(names,colors):
    print(name, '--->', color) ----> used in python 2 to get an index as well in python3 we do this way"""

# When we also need the index
for i, (name, color) in enumerate(zip(names, colors)):
    print(i, name, color)

#SORTING
### 1. Normal sorting — alphabetical order
colors = ['red', 'green', 'blue', 'yellow']
print(sorted(colors))


### 2. `key=len` — recommended Python 3 approach
colors = ['red', 'green', 'blue', 'yellow']
print(sorted(colors, key=len))

