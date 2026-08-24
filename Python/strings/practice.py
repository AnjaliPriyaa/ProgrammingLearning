#15. Find the first occurrence of a character in a string.
s = "ProgrammingLearning" 
target ='a'
def getoccurence(s,target):
    for i in range(len(s)):
        if target == s[i]:
            return i
    return -1
print(getoccurence(s,target))


#16. Find all occurrences of a character in a string.
s = "strongandlong"
target ='n'
def alloccurence(s,target):
    a=[]
    for i in range(len(s)):
        if target == s[i]:
            a.append(i)
    return a

print(alloccurence(s,target))

#17. Find the first occurrence of a substring.
s='abcacbabbabac'
target='aba'
def firstoccurencesubstring(s,target):
    for i in range(len(s)):
        # print(s[i:i+len(target)])
        if s[i:i+len(target)] == target:
            return i
    return -1

print(firstoccurencesubstring(s,target))


#18. Count occurrences of a character.
s='abcacbabbabac'
target ='c'
def countoccurenceofchar(s,target):
    count = 0
    for i in range(len(s)):
        if s[i]==target:
            count+=1
            continue
    return count

print(countoccurenceofchar(s,target))

#19. Count occurrences of every character.
input_string='abcacbabbabac'

def countoccurenceofeverychar(s):
    counter={}
    for char in input_string:
        if char not in counter:
            counter[char]=0
        counter[char]+=1
    return counter

print(countoccurenceofeverychar(input_string))

#20. Find the first non-repeating character.
input_string='abcacbfadbbabace'
newdict={}
def nonrepeatingcharacter(input_string):
    for char in input_string:
        if char not in newdict:
            newdict[char]=0
        newdict[char]+=1
    print(newdict)
    for key in newdict:
        if newdict[key]==1:
            return key
    return -1

print(nonrepeatingcharacter(input_string))

#21. Find the first repeating character.
input_string='abcefhbfadbbabace'

def firstrepeatingchar(input_string):
    counter=set()
    for i in input_string:
        if i not in counter:
            counter.add(i)
        else:
            return i
    return -1

print(firstrepeatingchar(input_string))

#22. Find all non-repeating characters.
input_string='abcefhbfadbbabace'

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
input_string='abcefhbfadbbabace'

def allrepeatingchar(input_string):
    counter = {}
    a = []
    for char in input_string:
        if char not in counter:
            counter[char]=0
        counter[char]+=1
    for key in counter:
       if counter[key]!=1:
           a.append(key)
    return a
    counter =set()
    a=set()
    for char in input_string:
        if char not in counter:
            counter.add(char)
        else:
            a.add(char)
    return a
print(allrepeatingchar(input_string))

#24. Remove duplicate characters from a string.
input_string='abcefhbfadbbabace'
stringoutput=set()
def removeduplicates(input_string):
    for i in input_string:
        if i not in stringoutput:
            stringoutput.add(i)
    result = ''.join(sorted(stringoutput))
    return result

print(removeduplicates(input_string))

output = ''.join(sorted(set(input_string)))
print (output)

#25. Check whether a string contains only digits.(imp)
input_string ="12dsa3098"
int(input_string)
def isDigitString(input_string):
    try:
        int(input_string)
        return True
    except ValueError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
print(isDigitString(input_string))

#26. Check whether a string contains only alphabets.
print("12dsa3098".isalpha())

input_string = '12dsa3098'
#29. Reverse a string.
input_string = '12dsa3098'
def reversestring(input_string):
    result=""
    # for i in range(len(input_string)-1, -1,-1): #imp
    #     result+=input_string[i]
    # return result
    # n=len(input_string)
    for i in range(len(input_string)):
        result += input_string[len(input_string)-i-1]
    return result
print(reversestring(input_string))

#30. Check whether a string is a palindrome.
input_string='eabcbae'
# print(input_string == input_string[::-1])

def palindrome(input_string):
    reversed= reversestring(input_string)
    if reversed == input_string:
        return True
    return False
print(palindrome(input_string))

#31. Count vowels and consonants in a string
vowelslist = "aeiouAEIOU"
consonantslist = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
input_string = 'somyasuhansmahapatra'

def countvowelsconsonants(input_string):
    vowel=0
    consonant=0
    for char in input_string:
        if char in vowelslist:
            vowel+=1
        elif char in consonantslist:
            consonant+=1
    return vowel,consonant

print(countvowelsconsonants(input_string))


#32. Count spaces in a string.
input_string = "b a c dd e f gh l"

def countspaces(input_string):
    counter=0
    for char in input_string:
        if char == ' ':
            counter+=1
    return counter

print(countspaces(input_string))

#33. Remove spaces from a string.
input_string = "b a c dd e f gh l"

def countspaces(input_string):
    counter = []
    for char in input_string:
        if char != ' ':
            counter.append(char)
    return counter

print(countspaces(input_string))

#(imp)34. Replace every occurrence of a character with another character.(You are given a string and two characters: A character to find A character to replace it with You need to replace every occurrence of the first character with the second character.)
input_string = list("banana")
input_string = "banana"
old_char = "a"
new_char = "o"

def replacechartonewchar(input_string, old_char, new_char):
    new_string = ""
    for char in input_string:
        if char != old_char:
            new_string+=char
        else:
            new_string+=new_char
    return new_string
print(replacechartonewchar(input_string, old_char, new_char))

def replacechartonewchar(input_string, old_char, new_char):
    newstring = []
    for char in input_string:
        if char != old_char:
            newstring.append(char)
        else:
            newstring.append(new_char)
    return newstring
print(replacechartonewchar(input_string, old_char, new_char))

