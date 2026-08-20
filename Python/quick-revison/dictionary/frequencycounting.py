#The core pattern -
# items[ch] = items.get(ch, 0) + 1
# or:
# items.setdefault(ch, 0)
# items[ch] += 1

# NOTE - Frequency required → dictionary
# Only existence required → set

# #21. Count itemsuency of characters
# s = "bananananadsasfgd"
# items = {}
# for ch in s:
#     items[ch] = items.get(ch,0)+1
#             # or 
# for ch in s:
#     items.setdefault(ch, 0)
#     items[ch] += 1
# print(items)

# #22. Count frequency of words
# text = "PytHon is easy and python is powerful"
# # words = text.split() #{'PytHon': 1, 'is': 2, 'easy': 1, 'and': 1, 'python': 1, 'powerful': 1}
# words = text.lower().split() #incase of sensitive- {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
# print(words)
# items = {}
# for word in words:
#     items[word] = items.get(word,0)+1
# print(items)

# #23. Find most frequent character
# s = "bananaasdabbgsfdfafnnnaaa"
# items = {}
# for ch in s:
#     items[ch] = items.get(ch,0)+1
# print(items)
# mostfrequent = max(items, key=items.get) #max(..., key=freq.get) finds the key having the largest value.
# print(mostfrequent)

# #24. Find least frequent character
# s = "bananaasdabbgsfsfafnnnaaa"
# items = {}
# for ch in s:
#     items[ch] = items.get(ch,0)+1
# print(items)
# leastfrequent = min(items, key=items.get) #max(..., key=freq.get) finds the key having the largest value.
# print(leastfrequent)

# #25. Find first repeating character
# s = "badqwertasdabbgsfdfafnnnaaa"
# # s = "abcdca"
# seen = set()
# for ch in s:
#     if ch in seen:
#         print("duplicate found",ch)
#         break
#     seen.add(ch)

# #26. Find first non-repeating character
# items = {}
# s = "badqwertasdabbgsfdfafnnnaaa"
# for ch in s:
#     items[ch]=items.get(ch,0)+1
# print(items)
# for key in items:
#     if items[key] == 1:
#         print(key)
#         break

# #27. Find all duplicate characters
# s = "badqwertasdabbgsfdfafnnnaaa"
# items={}
# duplicates = []
# for ch in s:
#     items[ch]=items.get(ch,0)+1
# print(items)
# for key,value in items.items():
#     if value>1:
#         duplicates.append(key)
# print(duplicates)

##28. Find all unique characters -> Unique means frequency exactly 1
# s = "badqwertasdabbgsfdfafnnnaaa"
# items={}
# duplicates = []
# for ch in s:
#     items[ch]=items.get(ch,0)+1
# print(items)
# for key,value in items.items():
#     if value == 1:
#         duplicates.append(key)
# print(duplicates)

# ##29. Find most frequent word
# text = "python java go python 1 2 12 1 1 1 1 1 go go go go java python"
# words = text.split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word,0)+1
# mostfrequent = max(frequency, key=frequency.get)
# print(mostfrequent)

##(imp)30. Find duplicate words
# text = "python java python go java python"
# words = text.split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word,0)+1
# duplicates = [
#     word
#     for word, count in frequency.items()
#     if count > 1
# ]
# print(duplicates)

##31. Count frequency of numbers
# text = "python java python go java python"
# words = text.split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word,0)+1
# print(frequency)

# # 35. Find elements occurring exactly K times
# nums = [1, 1, 2, 2, 2, 3, 4, 4]
# k = 2
# freq={}
# for i in nums:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# result = []
# for key,value in freq.items():
#     if value == k:
#         result.append(key)
# print(result)


#36. Find top K frequent elements
nums = [1, 1, 2, 2, 2, 3, 4, 4]
k = 2
freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1
print(freq)
result = []

sorted_items = sorted(freq.items(), key=lambda x:x[1], reverse=True)
print(sorted_items)
for key,count in sorted_items:
    result.append(key)
    if len(result) == k:
        break
print(result)

# #37.⁠ ⁠Sort elements according to frequency(imp)
# nums = [1, 1, 2, 2, 2, 3, 4, 4]
# k = 2
# freq={}
# for i in nums:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# result = []

# sorted_items = sorted(nums, key=lambda x:freq[x], reverse=True)
# for key,count in sorted_items[:k]:
#     result.append(key)
# print(result)