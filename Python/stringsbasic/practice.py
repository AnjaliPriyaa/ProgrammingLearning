# #15. Find the first occurrence of a character in a string.
# s = "ProgrammingLearning" 
# target ='a'
# def getoccurence(s,target):
#     for i in range(len(s)):
#         if target == s[i]:
#             return i
#     return -1
# print(getoccurence(s,target))


# #16. Find all occurrences of a character in a string.
# s = "strongandlong"
# target ='n'
# def alloccurence(s,target):
#     a=[]
#     for i in range(len(s)):
#         if target == s[i]:
#             a.append(i)
#     return a

# print(alloccurence(s,target))

# #17. Find the first occurrence of a substring.
# s='abcacbabbabac'
# target='aba'
# def firstoccurencesubstring(s,target):
#     for i in range(len(s)):
#         # print(s[i:i+len(target)])
#         if s[i:i+len(target)] == target:
#             return i
#     return -1

# print(firstoccurencesubstring(s,target))


# #18. Count occurrences of a character.
# s='abcacbabbabac'
# target ='c'
# def countoccurenceofchar(s,target):
#     count = 0
#     for i in range(len(s)):
#         if s[i]==target:
#             count+=1
#             continue
#     return count

# print(countoccurenceofchar(s,target))

# #19. Count occurrences of every character.
# input_string='abcacbabbabac'

# def countoccurenceofeverychar(s):
#     counter={}
#     for char in input_string:
#         if char not in counter:
#             counter[char]=0
#         counter[char]+=1
#     return counter

# print(countoccurenceofeverychar(input_string))

#20. Find the first non-repeating character.
# input_string='abcacbfadbbabace'
# newdict={}
# def nonrepeatingcharacter(input_string):
#     for char in input_string:
#         if char not in newdict:
#             newdict[char]=0
#         newdict[char]+=1
#     print(newdict)
#     for key in newdict:
#         if newdict[key]==1:
#             return key
#     return -1

# print(nonrepeatingcharacter(input_string))

#21. Find the first repeating character.
# input_string='abcefhbfadbbabace'

# def firstrepeatingchar(input_string):
#     counter=set()
#     for i in input_string:
#         if i not in counter:
#             counter.add(i)
#         else:
#             return i
#     return -1

# print(firstrepeatingchar(input_string))

#22. Find all non-repeating characters.
# input_string='abcefhbfadbbabace'

def allnonrepeatingchar(input_string):
    counter = {}
    a = []
    for char in input_string:
        if char not in counter:
            counter[char]=0
        counter[char]+=1
    for key in counter:
       if counter[key]==1:
           a.append(key)
    return a
print(allnonrepeatingchar(input_string))

#23. Find all repeating characters.