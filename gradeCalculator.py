print("Hello! This is the Grades Calculator.")
print("These are all the courses you are taking this year.\n")

# List of all the names
courses = []
grades = []

file1 = open("courseListWGrades.txt","a") #opening file in append mode;
file2 = open("courseList.txt","r") #This is the file from which will provide inputs


# Set new_name to something other than 'quit'.
holder = '' #this is for the final holding
course = ''
grade = ''
happy = ''
courseLine =''

# Start a loop that will run until the user enters 'quit'.
#before the loop clear the old execute file. 
line = file2.readline()
count = 0
while line:
     courseLine = line.rstrip('\n')
     print(count,'- ' +courseLine)
     count+=1
     courses.append(courseLine)
     line = file2.readline()



print("\nNow lets add your grades!")

while grade != quit:
    grade = (input("\nEnter the number of the course you want to add to (0 - 7): "))
    if(grade == 'quit'):
        print("\nYou are exiting now! Bye bro.")
        break
    else:
        grade = int(grade)
    
    if(grade < 0 or grade > 7):
        print("The grade needs to be be between 0 and 7")
    else:
        print("\nThe course you selected is: ",courses[grade])
        gradeValue = input("What is the grade for this course?: ")
        grades.append(gradeValue)
        print("\nYou got an " + gradeValue + " for " + courses[grade] + ". Congrats!")
        print("If you got more courses then feel free to add else type quit")
        file1.write(courses[grade] + gradeValue + '\n')

file1.close
file3 = open("courseListWGrades.txt","r+")


line2 = file3.readline()
print(line2)
while line2:
    courseLine = line2.rstrip('\n')
    print(courseLine)
    line2 = file3.readline()


#    print(course)
#    course = input("Enter the courses you want to add, once finished type 'quit': ")
#    if(course == 'quit'):
#          print("You have terminated here at the course.")
#          break

#    grade = input("Enter the grade for that course: ")
#    if (grade =='quit'):
#          print("You have terminated here.")
#          break

#    print("Course: "+course + " Grade: " + grade)
#    happy = input("Are you happy to enter in this info? (Y/N) ")
#    courses.append(course)

#    while happy != 'Y':
#        course = input("Please make sure to try writing it better this time. To quit type 'quit': ")
#        if(course == 'quit'):
#          print("You have terminated here at the course.")
#          break

#        grade = input("Enter the grade for that course: ")
#        if (grade =='quit'):
#          print("You have terminated here.")
#          break
            
#        print("Course: "+course + " Grade: " + grade)
#        happy = input("Are you happy to enter in this info? (Y/N): ")




# Show that the name has been added to the list.
