# 125. Create a file and write some content.
def create_file():
    with open("./Misc/outputfile.txt", "w") as file:
        file.write( 
            "Hello, this is my first file.\n"
            "I am learning Python file handling.\n"
            "This content is written using Python."
            )

create_file()

#126. Read the contents of a file. Entire file → read()
def readcontentfromfile():
    with open("./Misc/sample_app.log", "r") as file:
        content=file.read()
        print(content)

readcontentfromfile()

#127. Print every line of a file. - The requirement is to process/print one line at a time. Line by line → for line in file
def readcontentfromfile():
    with open("./Misc/outputfile.txt", "r") as file:
        for line in file:
            print(line.strip()) #strip() → removes leading/trailing whitespace, including \n.

readcontentfromfile()

#128. Count the number of lines.
def countnooflinesinfile():
    count = 0
    with open("./Misc/outputfile.txt","r") as file:
        for line in file:
            count+=1
        return count
print(countnooflinesinfile())

#129. Count the number of words.
def countnoofwordsinfile():
    count = 0
    with open("./Misc/outputfile.txt","r") as file:
        for line in file:
            words = line.split()
            count += len(words)
        return ('count:', count)

print(countnoofwordsinfile())

#130. Count the number of characters in a file.
def countnoofcharsinfile():
    count = 0
    with open("./Misc/sample_app.log","r") as file:
        for line in file:
            count += len(line)
        return ('count:', count)

print(countnoofcharsinfile())

#131. Find the longest line.
def longestlineinfile():
    longest_line =""
    with open("./Misc/sample_app.log","r") as file:
        for line in file:
            if len(line)> len(longest_line):
                longest_line = line
        return ("longestline:",longest_line,len(longest_line))

print(longestlineinfile())

#132.(imp) Find the shortest line.
def shortestlineinfile():
    shortest_line = None
    # shortest_line = 99999999999999
    with open("./Misc/sample_app.log","r") as file:
        for line in file:
            if shortest_line is None or len(line)< len(shortest_line):
                shortest_line=line
        return ("shortestline:",shortest_line, len(shortest_line))

print(shortestlineinfile())

#133.(imp)Search for a particular word in a file. & 134. Count how many times a word occurs.
keyword = 'ERpo'
count = 0
with open("./Misc/sample_app.log","r") as file:
    for line in file:
        if  keyword in line:
            count+=1
    if count > 0:
        print("we found the word, it occured :", count ,"times" )
    else:
        print("no word matches the keyword")


