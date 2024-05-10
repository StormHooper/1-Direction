from typing import Optional
import classes.student as Student
import classes.admin as Admin

class AuthenticationSystem():

  def __init__(self):
    """
    Constructor for the AuthenticationSystem class.

    students - A dictionary of student objects, where the keys are the student IDs and the values are the student objects.
    admins - A dictionary of admin objects, where the keys are the admin IDs and the values are the admin objects.
    """
    self.students = {
        "student@student.csulb.edu":
        ["password", Student.Student(0, "Patient Zero")],
        "elbee@student.csulb.edu": 
        ["shark", Student.Student(1, "Elbee")],
        "joey@student.csulb.edu": ["joey", Student.Student(2, "Joey")]
    }
    self.admins = {
        "admin@csulb.edu":
        ["password", Admin.Admin(0,"Admin", 
        student_edit=True,student_addcourse=True,student_removecourse=True,create_course=True)],

        #tester admin
        "1":
        ["1", Admin.Admin(0,"Admin", 
        student_edit=True,student_addcourse=True,student_removecourse=True,create_course=True)],

      
        "studentmanager@csulb.edu":
        ["password", Admin.Admin(1,"Student Manager", 
        student_edit=True,student_addcourse=True,student_removecourse=True)],

        "coursecreator@csulb.edu":
        ["password", Admin.Admin(2,"Course Creator", 
        create_course=True)]

    }
  def get_student_list(self):
    return [student[1] for student in self.students.values()]

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
    Returns the user object based on the role and email.

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

  def login(self, choice):
    """
    Logs in the user based on their role and email.
    Returns the user object if successful, None otherwise.

    Args:
        choice (int): The choice of the user.
    """
    if choice == 1:
      role = "student"
    elif choice == 2:
      role = "admin"
    else:
      raise ValueError
    """Logs in the user."""
    print(f"Logging in as a {role}.")
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    authenticated = self.authenticate(role, email, password)
    if authenticated:
      print("Login successful!")
      return self.get_user(role, email)
    else:
      print("Email or password is incorrect.")
      return None


