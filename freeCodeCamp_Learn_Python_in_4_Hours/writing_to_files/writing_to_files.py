# We will use the same employees.txt file to demonstrate this.
employee_file = open("/Users/alfred.shi/Desktop/VSCode/freeCodeCamp_Learn_Python_in_4_Hours/writing_to_files/employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()
# BE VERY CAREFUL ABOUT APPENDING, YOU CAN MESS UP A FILE EASILY. 
    # Running the program multiple times will continue to add the appended line.
    # Be wary also about line breaks. Use \n if necessary.

# Using "w" will overwrite everything in the existing file with what you put in the .write() brackets.
    # You can, however create a new file with "w".
employee_file = open("/Users/alfred.shi/Desktop/VSCode/freeCodeCamp_Learn_Python_in_4_Hours/writing_to_files/employees1.txt", "w")
employee_file.write("Kelly - Customer Service")
employee_file.close()

# You can convert/open between different file formats like html.
# Because we are in a different local workspace (folder), I used the absolute path to modify the
# employees/employees1.txt files.