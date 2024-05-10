from typing import Optional
import classes.student as Student
import classes.admin as Admin
import classes.course as Course
import classes.criteria as Criteria

class AuthenticationSystem():

  def __init__(self):
    self.students = {
    
        "patrick.mcgrath01@student.csulb.edu":
        ["password", Student.Student(0, "Patrick")],
        
        "elbee@student.csulb.edu": 
        ["shark", Student.Student(1, "Elbee")],
      
        "danieljoseph.belonio01@student.csulb.edu":      
        ["password", Student.Student(2, "Joey")],

        "tyler.pham03@student.csulb.edu":
        ["bongos", Student.Student(3, "Tyler")]
    }
    self.admins = {
        "admin@csulb.edu":
        ["password", Admin.Admin(0,"Admin", 
        student_edit=True,student_addcourse=True,student_removecourse=True,create_course=True)],

        "studentmanager@csulb.edu":
        ["password", Admin.Admin(1,"Student Manager", 
        student_edit=True,student_addcourse=True,student_removecourse=True)],

        "coursecreator@csulb.edu":
        ["password", Admin.Admin(2,"Course Creator", 
        create_course=True)],

        "josh@csulb.edu":
        ["password", Admin.Admin(3,"Joshua",
        student_edit=True,student_addcourse=True,student_removecourse=True,create_course=True)]
        

    }

    self.criteria = [Criteria.Criteria('CECS'), Criteria.Criteria('GAMES')]

    self.courses = [Course.Course('Among Us Fundamentals, Sec01', 1, 'GAME-344', self.criteria[1]), Course.Course('Intro to Software Engineering, Sec05', 32, 'CECS 343', self.criteria[0]),
                    Course.Course('Among Us Fundamentals, Sec01', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec02', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec03', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec04', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec05', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec06', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec07', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec08', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec09', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec10', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec11', 1, 'GAME-344', self.criteria[1]),
                    Course.Course('Among Us Fundamentals, Sec12', 1, 'GAME-344', self.criteria[1]), 
                    Course.Course('Among Us Fundamentals, Sec13', 1, 'GAME-344', self.criteria[1])]
                   
   
  def get_student_list(self):
    return [student[1] for student in self.students.values()]

  def get_course_list(self):
    return self.courses

    # STRUCTURE:
    # "{email}" : [ "{password}", {student : Student}
  def get_student(self, id: int):
    """
    Returns the student with the given id.

    Args:
      id (int): The id of the student to be returned.
    """
    for user in self.students.values():
      if user[1].id == id:
        return user[1]
    return None

  def get_admin(self, id: int):
    """
    Returns the admin with the given id.

    Args:
      id (int): The id of the admin to be returned.
    """
    for user in self.admins.values():
      if user[1].id == id:
        return user[1]
    return None


  def authenticate(self, role: str, email: str, password: str) -> bool:
    """Authenticates the user based on their role, email, and password."""
    # Here you would implement the logic to authenticate users
    # For example, check if the email and password match records for the given role
    # For simplicity, let's assume some predefined email and password combinations

    if role.lower() == "student":
      emails = self.students
      success = True
    elif role.lower() == "admin":
      emails = self.admins
      success = True
    else:
      emails = {}
      success = False

    if email in emails and password == emails[email][0]:
      return success
    return False

  def get_user(self, role: str, email: str):
    """
    Returns the user with the given role and email.

    Args:
      role (str): The role of the user.
      email (str): The email of the user.
    """
    if role.lower() == "student":
      emails = self.students
    elif role.lower() == "admin":
      emails = self.admins
    else:
      raise ValueError("Invalid user type.")
    if email in emails:
      return emails[email][1]

  def login(self, email, password, choice):
    """
    Logs in the user with the given email and password.

    Args:
      email (str): The email of the user.
      password (str): The password of the user.
    """
    if choice == 1:
      role = "student"
    elif choice == 2:
      role = "admin"
    else:
      raise ValueError
    """Logs in the user."""
    

    authenticated = self.authenticate(role, email, password)
    if authenticated:
      return self.get_user(role, email)
    else:
      return None


