from classes import student, course, criteria, admin, interface

# not a unit test just a basic test
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
  
def get_yes_no(prompt: str) -> bool:
  while True:
      choice = input(prompt).upper()
      if choice == "Y":
        return True
      elif choice == "N":
        return False
      else:
        print("\nInvalid input. Please try again\n")

def display_student_actions() -> int:
  prompt = """
Do student stuff:
1. Add course to schedule
2. Remove course from schedule
3. List all enrolled courses.
4. List all wishlisted courses.
5. Display notifications
6. Clear notifications


0. Log Out
"""
  
  choice = get_int_range(prompt, 0, 6)
  return choice

def display_admin_actions() -> int:
  prompt = """
Do admin stuff:
1. Edit student name
2. Add course to student schedule
3. Remove course from student schedule
4. Make new course

0. Log Out
"""
  choice = get_int_range(prompt, 0, 5)
  return choice


# Main function to run the program
def main():
  
  
  cecs = criteria.Criteria('Computer Engineering & Science (CECS)')
  games = criteria.Criteria('Gaming (GAME)')

  

  g0 = course.Course('Among Us Fundamentals, Sec01', 1, 'GAME-344', games)
  g1 = course.Course('Among Us Fundamentals, Sec02', 1, 'GAME-344', games)
  g2 = course.Course('Fortnite Construction and Strategem, Sec01', 1, 'GAME-090', games)
  g3 = course.Course('Blue Archive Meta, Sec01', 1, 'GAME-115', games)
  
  c0 = course.Course('Intro to Software Engineering, Sec05', 32, 'CECS-343', cecs)
  c1 = course.Course('Data Structures, Sec01', 1, 'CECS-274', cecs)
  c2 = course.Course('Intro to Object-Oriented Programming, Sec01', 1, 'CECS-277', cecs)
  c3 = course.Course('Intro to Object-Oriented Programming, Sec02', 1, 'CECS-277', cecs)

  
  classesList = [g0, g1, g2, g3, c0, c1, c2, c3]

  criteriaList = [games, cecs]
  
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
        if option == 1:
          loggingIn = True
        elif option == 2:
          loggingIn = False
        elif option == 3:
          loggingIn = False
          over = True
        else:
          raise ValueError
      else:
        loggingIn = False
        loggedIn = True
        #print([course.name for course in user.courses], '\n')
        print(f"Welcome, {str(user)}")

        while loggedIn:
          ### STUDENT ###

          #
          if usertype == 1:
            # user = student object already
            action = display_student_actions()


            #################################### COURSE ADD/SEARCH #####################################
            if action == 1:
              results = []
              failprompt = "Select an option to continue:\n" \
              "1. Try Again\n"\
              "2. Return\n"
              added = False
              searching = True
              while searching:
                try:
                  print("\nCourse Search\nList of Departments:")
                  for criterion in criteriaList:
                    print(f" - {criterion.name}")
                  query = input("\nPlease enter the course ID (ex. CECS-343)\n"\
                                "or matching four letter code (ex. CECS) : ").upper()
                  for sec in range(len(classesList)):
                    qLen = len(query)
                    if classesList[sec].id == query or query[:qLen] == classesList[sec].id[:qLen]:
                       results.append(classesList[sec])
                  if len(results) <= 0:
                    raise(ValueError())
                  else: 
                    searching = False
                except(ValueError):
                  print("Invalid course ID.")
                  tryagain = get_int_range(failprompt, 1, 2)
                  if tryagain == 2:
                    searching = False
                    results = []

              if not searching and len(results) > 0:
                selecting = True
                while selecting:
                  resultstring = f"\nThere are {len(results)} result(s).\nSelect one to view course info:\n"
                  for i in range(len(results)):
                    resultstring += (f"{i+1}. {results[i].name}\n")
                  resultstring += (f"{len(results)+1}. Cancel\n")
                  choice = get_int_range(resultstring, 1, len(results)+1)

                  if choice == len(results)+1:
                    selecting = False
                  else: 
                    section = results[choice-1]
                    print(section, '\n')
                    added = get_yes_no("Enroll in this course? [Y/N]\n")

                    if added:
                      selecting = False
                      print(f"Adding user to {section.name}")
                      user.add_course(section)
                    else: 
                      print("\nReturning to results.\n")


            #################################### COURSE REMOVE #####################################
            if action == 2:
              if len(user.courses) <= 0:
                print("You have no courses to remove. Returning to previous menu.\n")
              else:
                while True:
                  prompt = 'Please select a class you would like to\nremove or leave the waitlist of.\n'
                  for i in range(len(user.courses)):
                    prompt += (f"{i+1}. {user.courses[i].name}\n")
                  prompt += (f"{len(user.courses)+1}. Cancel\n")
                  choice = get_int_range(prompt, 1, len(user.courses)+1)
                  
                  if choice == len(user.courses)+1:
                    print("Returning to previous menu.\n")
                    break
                    
                  else: 
                    section = user.courses[choice-1]
                    print(section, '\n')
                    removed = get_yes_no("Remove this course? [Y/N]\n")
    
                    if removed:
                      print(f"Removing user from {section.name}")
                      user.remove_course(section)
                      break
                  
                    else: 
                      print("\nReturning to course list.\n")
                
            # ...
            if action == 3:
              print('Listing enrolled courses ...')
              i = 1
              for sec in user.courses:
                  if user not in sec.waitlist:
                    print(f'{i}. {sec.name}')
                    i += 1

            if action == 4:
              print("Listing waitlisted courses ...")
              i = 1
              for sec in user.courses:
                if user in sec.waitlist:
                  print(f'{i}. {sec.name}')
                  i += 1

            if action == 5: 
              print("Displaying notifications ...")
              user.read_notify()

            if action == 6:
              print("Clearing notifications ...")
              user.clear_notify()

          ### ADMIN ###
          elif usertype == 2:
            # user = admin object already
            action = display_admin_actions()
            if action == 1:
              #admin action / change the name of the student
              students = authenticationSystem.get_student_list()
              for i in range(len(students)):
                print(f"{i+1}. {students[i].name}")
              print()
              student = get_int_range("Select a student: ", 1, len(students))
              oldname = students[student - 1].name
              print(f"\nStudent: {students[student - 1]}")
              user.edit_student_info(students[student - 1])
              print(f"\nStudent {oldname} is now {students[student - 1]}")

            if action == 2:
              #add course to student
              students = authenticationSystem.get_student_list()
              for i in range(len(students)):
                print(f"{i+1}. {students[i].name}")
              print()
              student = get_int_range("Select a student: ", 1, len(students))
              print(f"\nStudent: {students[student - 1]}'s Current Courses")
              print([course.name for course in students[student - 1].courses])
              user.add_course_to_student(students[student - 1], c0)
              print(f"\nStudent: {students[student - 1]}'s Current Courses after Adding")
              print([course.name for course in students[student - 1].courses], '\n')
              

            if action == 3:
              #remove course from student
              students = authenticationSystem.get_student_list()
              for i in range(len(students)):
                print(f"{i+1}. {students[i].name}")
              print()
              student = get_int_range("Select a student: ", 1, len(students))
              print(f"\nStudent: {students[student - 1]}'s Current Courses")
              print([course.name for course in students[student - 1].courses])
              user.remove_course_from_student(students[student - 1], c0)
              print(f"\nStudent: {students[student - 1]}'s Current Courses after Removing")
              print([course.name for course in students[student - 1].courses], '\n')

              pass

            if action == 4:
              #create course
              new_course = user.create_course(games)
              print(new_course)
            # ...

          else:
            raise ValueError("User has impossible role!")
          if action == 0:
            loggedIn = False
  # test()

#########################################################



# pyg() # run pygame
# Run the program
main()
#rundown
#log in. Display admin or student 
#for admin and student create a  log in and student email system

