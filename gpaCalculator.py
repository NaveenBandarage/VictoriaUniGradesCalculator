file4 = open("courseListWGrades.txt", "r")
newLine = file4.readline()

while newLine:
    # Remove the new line characters and extra spacing
    newLine = newLine.strip()
    # For each part in the new line look for grade
    for part in newLine.split():
            print(part)
            # Take the whole line and then replace the 'Grade:' with a blank character so we are only left with the letter
            newLine = part[2] #if wanted the grades 
           # print it out
            print(newLine)
            # put it into the grades text file. 
    # Move to the next line regardless 
    newLine = file4.readline()