file4 = open("courseListWGrades.txt", "r")
newLine = file4.readline()

while newLine:
    # Remove the new line characters and extra spacing
    newLine = newLine.strip()
    # For each part in the new line look for grade
    newLine = newLine.split(":")[-1]    
    print(newLine)
            
            # Take the whole line and then replace the 'Grade:' with a blank character so we are only left with the letter
             #if wanted the grades 
           # print it out
            # put it into the grades text file. 
    # Move to the next line regardless 
    newLine = file4.readline()