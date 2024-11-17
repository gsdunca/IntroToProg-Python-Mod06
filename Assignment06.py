# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_SDuncan
# Desc: This assignment demonstrates using Classes and Functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   SDuncan,11/16/24,Updated starter for assignment 06
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Variables and constants
students: list = []  # a list of student data
menu_choice = '' # user's menu choice initialized as null/none

# Processing Class ---(reads and writes Data to and from a file)-------------- #
class FileProcessor:
    """
    A collection of processing layer functions
    - Read files into memory
    - write to files with updated data from memory

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    SDuncan,11/16/24,Updated for Assignment06
    """
    pass
    # When the program starts it loads the .json file
    # Extract the data from the file

    @staticmethod # Reads data from file into memory
    def read_data_from_file(file_name: str, student_data: list):
        """
        reads the contents of a file into memory

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Updated for Assignment06
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("\n ERROR:" "\n File must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod # Writes updated user data to file

    def write_data_to_file(file_name: str, student_data: list):
        """
        writes the contents of memory into a file

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Updated for Assignment06
        """
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())


# Presentation Class ---(Contains various Input/Output functions for user interactions---
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    SDuncan,11/16/24,Updated for Assignment06
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Reused from Mod06-Lab03 for Assignment06

        :return: None, No Data is returned to program/Displayed only
        """
        pass
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Reused from Mod06-Lab03 for Assignment06

        :return: None, No Data is returned to program/Displayed only
        """
        pass
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function receives the menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Reused from Mod06-Lab03 for Assignment06
        :return: string with the users choice
        """
        pass
        choice = "0" # Defines the Variable as a string and Sets User Choice to be initialized as Zero/0/None/Null
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function receives the Students First Name, Last Name, and Course from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Updated starter file for Assignment06

        :return: None
        """
        pass
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

    @staticmethod
    def output_student_data(student_data: list):
        """ This function displays the contents of Enrollments.json

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        SDuncan,11/16/24,Updated starter file for Assignment06

        :return: None
        """
        pass

        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


# Beginning of the MAIN BODY of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
#students holds the List of data loaded from the file, referenced in constant FILE_NAME

# Present and Process the data
while (True):
    IO.output_menu(menu=MENU) #ties menu parameter in "output_menu" function to the constant MENU
    menu_choice = IO.input_menu_choice() #Stores the user's menu choice option/references the correct choice

    if menu_choice == "1":  # Allow the User to input new data
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":# Presents the current data to the user
        IO.output_student_data(student_data=students)
        continue

    elif menu_choice == "3":# writes the contents of memory to the data to a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4": # Stop the loop
        break  # out of the loop
print("Program Ended")
