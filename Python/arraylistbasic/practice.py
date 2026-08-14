#35. Find the largest element in an array.
input_array = [12, 45, 7, 89, 23, 56, 34]

def largestelement(input_array):
    counter = -9999
    for i in input_array:
        if i > counter:
            counter = i
    return counter

def largestelement(input_array):
    counter = -9999
    for i in input_array:
        counter = max(counter,i)
    return counter
print(largestelement(input_array))

#36. Find the smallest element in an array.
input_array = [12, 45, 7, 89, 23, 56, 34]

def largestelement(input_array):
    counter = 9999999
    for i in input_array:
        if i < counter:
            counter = i
    return counter

def largestelement(input_array):
    counter = 9999999999
    for i in input_array:
        counter = min(i,counter)
    return counter
print(largestelement(input_array))

37.(imp) Find the second largest element.
input_array = [12, 45, 7, 89, 23, 56, 34]
    
def secondlargestelement(input_array):
    largest = -1
    secondlargest=-1
    for i in range(len(input_array)):
        if input_array[i] > largest:
            secondlargest=largest
            largest = input_array[i]
        elif input_array[i] < largest and input_array[i] > secondlargest:
            secondlargest = input_array[i]
    return secondlargest
print(secondlargestelement(input_array))

38. Find the second smallest element.

input_array = [12, 45, 7, 89, 23, 56, 34]

def secondsmallestelement(input_array):
    smallest = 999999
    secondsmallest = 999999
    for i in range(len(input_array)):
        if input_array[i] < smallest:
            secondsmallest = smallest
            smallest = input_array[i]
        elif input_array[i] < smallest and input_array[i] < secondsmallest:
            secondsmallest = input_array[i]
    return secondsmallest

print(secondsmallestelement(input_array))

39. Calculate the sum of all elements.
input_array = [12, 45, -7, 89, 23, 56, -34]
def sumofallelements(input_array):
    sum = 0
    for i in range(len(input_array)):
        sum+=input_array[i]
    return sum
print(sumofallelements(input_array))

#40. Calculate the average of all elements.
input_array = [12, 45, 7, 89, 23, 56, 34]
#input_array = [12, 45, 7, 89, 23, 56, 33]
n=len(input_array)
def averageofallelements(input_array):
    sum = 0
    average = 0
    for i in range(len(input_array)):
        sum+=input_array[i]
        average = sum/n
    return average
    # return round(average, 2)
print(averageofallelements(input_array))

#41. Count even and odd numbers.
input_array = [12, 45, 7, 89, 23, 56, 34]
def countevenodd(input_array):
    even = 0
    odd = 0
    for i in input_array:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return {"even": even, "odd": odd}

print(countevenodd(input_array))

#42. Find all even numbers.
input_array = [12, 45, 7, 89, 23, 56, 34]
def counteven(input_array):
    even = 0
    for i in input_array:
        if i%2 == 0:
            even+=1
    return {"even": even}

print(counteven(input_array))

#43. Find all odd numbers.

input_array = [12, 45, 7, 89, 23, 56, 34]
def countodd(input_array):
    odd = 0
    for i in input_array:
        if i%2 != 0:
             odd+=1
           
    return {"odd": odd}

print(countodd(input_array))

44. Reverse an array.
input_array = [12, 45, 7, 89, 23, 56, 34]
print(input_array[::-1])

def reversearray(input_array):
    new=[]
    for i in range(len(input_array)-1,-1,-1):
        new.append(input_array[i])
    return new

print(reversearray(input_array))

(imp)#45. Find the first occurrence(find the index/position of the first time that element appears) of an element
input_array = [10, 20, 30, 20, 40, 20, 50]
target = 500
def firstoccurence(input_array):
    for i in range(len(input_array)):
        if input_array[i] == target:
            return i
    return -1

print(firstoccurence(input_array))

#46. Find all occurrences of an element.Given an array and a target element, find every index where that element appears
input_array = [10, 20, 30, 20, 40, 20, 50]
target = 20

def alloccurence(input_array,target):
    counter =[]
    for i in range(len(input_array)):
        if input_array[i] == target:
            counter.append(i)     
    return counter

print(alloccurence(input_array))

#48. Remove an element from an array.
input_array = [10, 20, 30, 40, 50]
target = 20

def removeelement(input_array,target):
    
    for i in range(len(input_array)):
        if input_array[i] == target: 
            # input_array.remove(target)
            input_array.pop(i) #pop(i) removes the element at index i.
            break
    return input_array

print(removeelement(input_array,target))

#49.(imp) Remove all occurrences of an element.
input_array = [10, 20, 30, 20, 40, 20, 50]
target = 20
array = [x for x in input_array if x != target]
print(array)
def removealloccurence(input_array,target):
    for i in input_array:
        if i == target:
            input_array.remove(target)
    return input_array

print(removealloccurence(input_array,target))

input_array = [10, 20, 30, 20, 40, 20, 50]
target = 20
for i in range(len(input_array) - 1, -1, -1):
    if input_array[i] == target:
        input_array.pop(i)

print(input_array)


#50. Remove duplicate elements.
input_array = [10, 20, 30, 20, 40, 10, 50, 30]
input_array = list(set(input_array))
print(input_array)
def removeduplicate(input_array):
    res = []
    for x in input_array:
        if x not in res:
            res.append(x)
    return res
print(removeduplicate(input_array))

#51. Find Unique Elements in an Array
#Given an array, find the elements that appear exactly once. Unlike "remove duplicates," here you do not keep the first occurrence of a repeated element.
input_array = [10, 20, 30, 20, 40, 10, 50, 30, 60]

new_array =[]
def uniqueelements(input_array):
    for element in input_array:
        if input_array.count(element) ==1:
            new_array.append(element)
    return new_array

print(uniqueelements(input_array))

#52. Find duplicate elements in an array.
input_array = [10, 20, 30, 20, 40, 10, 50, 30, 60]

def duplicateelements(input_array):
    new=set()
    new_array =[]   
    for element in input_array:
        if element not in new:
            print(input_array)
            new.add(element)
        else:
            new_array.append(element)
            print(new_array)
    return new_array

print(duplicateelements(input_array))

#53. Find elements that occur exactly once.
input_array = [10, 20, 30, 20, 40, 10, 50, 30, 60]
def elementsoccuringonce(input_array):
    new=set()
    for i in input_array:
        if i not in new:
            new.add(i)
        else:
            new.remove(i)
    return new

print(elementsoccuringonce(input_array))

