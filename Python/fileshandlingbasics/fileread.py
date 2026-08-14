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