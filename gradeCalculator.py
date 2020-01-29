print("Hello! This is the Grades Calculator.\n")
# List of all the names
courses = []
file1 = open("executeInput.txt","w") #opening file in append mode;
file2 = open("courseList.txt","r") #This is the file from which will provide inputs


# Set new_name to something other than 'quit'.
holder = '' #this is for the final holding
course = ''
grade = ''
happy = ''


# Start a loop that will run until the user enters 'quit'.
#before the loop clear the old execute file. 
 
while course != 'quit' or grade != 'quit':
    # Ask the user for a name.
   print(course)
   course = input("Enter the courses you want to add, once finished type 'quit': ")
   if(course == 'quit'):
         print("You have terminated here at the course.")
         break

   grade = input("Enter the grade for that course: ")
   if (grade =='quit'):
         print("You have terminated here.")
         break

   print("Course: "+course + " Grade: " + grade)
   happy = input("Are you happy to enter in this info? (Y/N) ")
   courses.append(course)

   while happy != 'Y':
       course = input("Please make sure to try writing it better this time. To quit type 'quit': ")
       if(course == 'quit'):
         print("You have terminated here at the course.")
         break

       grade = input("Enter the grade for that course: ")
       if (grade =='quit'):
         print("You have terminated here.")
         break
            
       print("Course: "+course + " Grade: " + grade)
       happy = input("Are you happy to enter in this info? (Y/N): ")




# Show that the name has been added to the list.
