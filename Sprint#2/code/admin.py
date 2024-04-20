from typing import List, Optional, Union
import classes.student as student
import classes.course as course
import classes.criteria as criteria


class Admin:
    def __init__(
      self, admin_id: int, admin_name: str, 
      student_edit: Optional[bool] = False, 
      student_addcourse: Optional[bool] = False,
      student_removecourse: Optional[bool] = False,
      create_course: Optional[bool] = False
      ):
      '''
      Constructor for the Admin class. By default, all permissions are false unless assigned true.

      Args:
        name (str): The name of the admin.
        id (int): An ID to identify whether admins are unique or are different sections of the same class.
        student_edit (bool): A boolean value that determines whether the admin can edit student information.
        student_addcourse (bool): A boolean value that determines whether the admin can add courses to students.
        student_removecourse (bool): A boolean value that determines whether the admin can remove courses from students.
      '''
      self._name = admin_name
      self._id = admin_id
      self._student_edit = student_edit
      self._student_addcourse = student_addcourse
      self._student_removecourse = student_removecourse
      self._create_course = create_course


    @property
    def id(self):
        return self._id
  
    @property
    def name(self):
        return self._name

    def __str__(self):
      return self._name

    def edit_student_info(self, student_obj: student.Student) -> None:
        """
        Edit student information.

        Args:
            student_obj (student.Student): The student object whose information needs to be edited.
        """
        if self._student_edit:  # Assuming permissions[0] indicates permission to edit student info
            new_name = input("Enter the new name for the student: ")
            student_obj.name = new_name
            print("Student information updated successfully.")
        else:
            print("You don't have permission to edit student information.")

    def add_course_to_student(self, student_obj: student.Student, course_obj: course.Course) -> None:
        """
        Add a course to a student.

        Args:
            student_obj (student.Student): The student object.
            course_obj (course.Course): The course object to be added to the student's courses.
        """
        if self._student_addcourse:  # Assuming permissions[1] indicates permission to add courses to students
            if not course_obj.is_full():
                student_obj.add_course(course_obj)
                print(f"Course {course_obj.name} added to {student_obj.name}.")
            else:
                print("Course is full. Cannot add the course to the student.")
        else:
            print("You don't have permission to add courses to students.")

    def remove_course_from_student(self, student_obj: student.Student, course_obj: course.Course) -> None:
        """
        Remove a course from a student.

        Args:
            student_obj (student.Student): The student object.
            course_obj (course.Course): The course object to be removed from the student's courses.
        """
        if self._student_removecourse:  # Assuming permissions[2] indicates permission to remove courses from students
            if course_obj in student_obj.courses:
                student_obj.remove_course(course_obj)
                print(f"Course {course_obj.name} removed from {student_obj.name}.")
            else:
                print(f"Student {student_obj.name} is not enrolled in course {course_obj.name}.")
        else:
            print("You don't have permission to remove courses from students.")

    def create_course(self, notify_students) -> Union[course.Course, None]:
      """
      Create a new course interactively by taking user input.

      Returns:
          course.Course: The newly created course object.
      """
      if self._create_course:
          # Get course name from user input
          course_name = input("Enter the name of the course: ")

          # Get maximum capacity from user input
          while True:
              capacity_input = input("Enter the maximum capacity of the course: ")
              try:
                  capacity = int(capacity_input)
                  break
              except ValueError:
                  print("Invalid input. Please enter a valid integer.")

          # Get course ID from user input
          course_id = input("Enter the ID of the course: ")

          '''# Get criteria from user input
          criteria_list = []
          add_criteria = input("Do you want to add eligibility criteria? (Y/N): ").upper()
          invalid = True
          while invalid:
            if add_criteria == "Y":
                criteria_name = input("Enter the name of the criteria: ")
                criteria_list.append(criteria_name)
                invalid = False
            elif add_criteria == "N":
                invalid = False
            else:
                print("Invalid input. Please try again.")
          
          # Create Criteria objects
          criteria_objects = [criteria.Criteria(name) for name in criteria_list]
          '''
          # Create the course object with the gathered information
          new_course = course.Course(course_name, capacity, course_id, notify_students)
          print(f"Course {new_course.name} created successfully.")
          return new_course
      else:
          print("You don't have permission to create courses.")
          return None