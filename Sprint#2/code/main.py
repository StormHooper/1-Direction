from classes import student, course, criteria, admin, interface



#screen creation -- import
import turtle
#import tkinter as tk
from  tkinter import *


def test():
  namesson = student.Student(1, 'Name Nameer N. Namesson III Jr. Esquire')
  joe = student.Student(2, 'Joe')
  john = student.Student(3, 'John')
  jane = student.Student(4, 'Jane')
  jeffrey = student.Student(5, 'Jeffrey')
  imposter = student.Student(6, 'Imposter')

  games = criteria.Criteria('Games')
  games.add_student(imposter)
  games.add_student(joe)
  games.add_student(namesson)
  cecs = criteria.Criteria('CECS')
  cecs.add_student(joe)
  cecs.add_student(john)
  
  g0 = course.Course('Among Us Fundamentals, Sec01', 1, 'GAME-344', games)
  imposter.add_course(g0)
  c0 = course.Course('Intro to Software Engineering, Sec05', 32, 'CECS 343', cecs)
  
  c1 = course.Course('Among Us Fundamentals, Sec02', 1, 'GAME-344', games)
  
  joe.read_notify()
  john.read_notify()
  imposter.read_notify()


  print("Please press Y to waitlist all test students so that value error not occur")

  
  namesson.add_course(c1)
  joe.add_course(c1)
  john.add_course(c1)
  jane.add_course(c1)

  # The below is equivalent to admin.add_student(s5, c1) and disregards capacity.
  c1.add_student(jeffrey)
  jeffrey.courses.append(c1)
  # end of admin.add_student
  
  print(f'Init:\n{c1}\n')
  jane.remove_course(c1)
  print(f'Remove Jane:\n{c1}\n')
  jane.add_course(c1)
  print(f'Add Jane:\n{c1}\n')
  joe.remove_course(c1)
  print(f'Remove Joe:\n{c1}\n')
  namesson.remove_course(c1)
  print(f'Remove Name:\n{c1}\n')
  jeffrey.remove_course(c1)
  print(f'Remove Jeffrey:\n{c1}\n')


  print('\n'*3 + 'Admin Test:')
  
  # Simulating admin actions
  boss = admin.Admin(1234, "Admin", 
                     student_edit = True, 
                     student_addcourse = True, 
                     student_removecourse = True,
                     create_course = True)  # Assuming admin has all permissions
  oldname = namesson.name
  print(f"\nStudent: {namesson}")
  boss.edit_student_info(namesson)
  print(f"\nStudent {oldname} is now {namesson}")

  # Add a course to a student
  print(f"\nStudent: {namesson}'s Current Courses")
  print([course.name for course in namesson.courses])
  boss.add_course_to_student(namesson, c0)
  print(f"\nStudent: {namesson}'s Current Courses after Adding")
  print([course.name for course in namesson.courses], '\n')

  # Remove a course from a student
  boss.remove_course_from_student(namesson, c0)
  print(f"Student: {namesson}'s Courses after Removal")
  print([course.name for course in namesson.courses], '\n')

  # Create a new course
  new_course = boss.create_course(games)
  print(new_course)
  namesson.read_notify()
  namesson.add_course(new_course)
  print(f"Student: {namesson}'s Courses after Creating")
  print([course.name for course in namesson.courses], '\n')
  print(new_course)
  #print(new_course.name)


'''Prototype of student-admin login system'''
# import turtle
# from tkinter import *
# from classes import student, course, criteria, admin

# # Function to display a message on the screen using Turtle
# def display_message(message, y_offset=0):
#     pen.goto(0, y_offset)
#     pen.write(message, align="center", font=("Arial", 16, "normal"))

# # Function to clear the screen using Turtle
# def clear_screen():
#     pen.clear()

# # Function to display student actions using Turtle
# def display_student_actions():
#     clear_screen()
#     display_message("Student Actions", 150)
#     display_message("1. View Courses", 125)
#     display_message("2. Enroll in Course", 100)
#     display_message("3. Drop Course", 75)

# # Function to display admin actions using Turtle
# def display_admin_actions():
#     clear_screen()
#     display_message("Admin Actions", 150)
#     display_message("1. Create Course", 125)
#     display_message("2. Add Student to Course", 100)
#     display_message("3. Remove Student from Course", 75)
    
# #def button(): # for student?
  
  
# # Function to handle student interactions
# def student_interaction():
#     display_student_actions()
#     action = screen.textinput("Student Actions", "Enter action number (1-3): ")
#     # Handle student actions based on input

  
#     #experimenting on student

#     pen = turtle.Turtle()
#     pen.hideturtle()
    
#     button_x = -50
#     button_y = -50
#     buttonlength = 100
#     buttonwidth = 50
    
    



# # Function to handle admin interactions
# def admin_interaction():
#     display_admin_actions()
#     #turtle.onscreenclick(buttonClick, 1)
#     password = screen.textinput(".", "Input Password")
#     action = screen.textinput("Admin Actions", "Enter action number (1-3): ")
    
    
    

    
    
    # Handle admin actions based on input



def get_int_range(prompt: str, min: int, max: int):
  while True:
    try:
      choice = int(input(prompt))
      if choice in range(min, max + 1):
        return choice
      else:
        print("\nInvalid input. Please try again\n")
    except ValueError:
      print("\nInvalid input. Please try again\n")

def display_login_options() -> int:
  """Displays login options for the user to select."""

  prompt = """
Select a user type:
1. Student
2. Admin

0. Quit
"""

  choice = get_int_range(prompt, 0, 2)
  return choice

def display_student_actions() -> int:
  prompt = """
Do student stuff:
1. Student thing 1
2. Student thing 2

0. Log Out
"""
  choice = get_int_range(prompt, 0, 2)
  return choice

def display_admin_actions() -> int:
  prompt = """Do admin stuff:
1. Admin thing 1
2. Admin thing 2
3. Admin thing 3

0. Log Out
"""
  choice = get_int_range(prompt, 0, 5)
  return choice
  

# Main function to run the program
def main():
  authenticationSystem = interface.AuthenticationSystem()
  over = False
  while not over:
    usertype = display_login_options()
    if usertype == 0:
      over = True
      break
    else:
      loggingIn = True
    while loggingIn:
      user = authenticationSystem.login(usertype)
      if user is None:
        failprompt = "Select an option to continue:\n" \
        "1. Try Again\n"\
        "2. Return\n"\
        "3. Quit\n"
        option = get_int_range(failprompt, 1, 3)
        if loggingIn == 1:
          loggingIn = True
        elif loggingIn == 2:
          loggingIn = False
        elif loggingIn == 3:
          over = True
        else:
          raise ValueError
      else:
        loggingIn = False
        loggedIn = True
        print(f"Welcome, {str(user)}")

        while loggedIn:
          ### STUDENT ###
          if usertype == 1:
            # user = student object already
            action = display_student_actions()
            if action == 1:
              pass
            if action == 2:
              pass
            # ...

          ### ADMIN ###
          elif usertype == 2:
            # user = admin object already
            action = display_admin_actions()
            if action == 1:
              #admin action / change the name of the student

              pass
            if action == 2:
              #see classes

              pass

            if action == 3:
              #see students

              pass

            if action == 4:
              #add student to courses

              pass

            if action == 5:
              # remove stuent from course
              pass
            # ...

          else:
            raise ValueError("User has impossible role!")
          if action == 0:
            loggedIn = False
  # test()
  


### [TURTLE] ###
#     while True:
#         role = screen.textinput("Login", "Enter your role (admin/student): ").lower()
        
#         if role == "admin":
#             admin_interaction()
#         elif role == "student":
#             student_interaction()
#         else:
#             display_message("Invalid role. Please enter 'admin' or 'student'.")
#             continue

# # Set up the screen
# screen = turtle.Screen()
# screen.setup(width=650, height=650)
# screen.title("Student-Admin")
# screen.bgcolor("skyblue")

# # Set up the turtle
# pen = turtle.Turtle()
# pen.speed(0)
# pen.penup()
# pen.hideturtle()
#########################





  
# Run the program
main()
#rundown
#log in. Display admin or student 
#for admin and student create a  log in and student email system

