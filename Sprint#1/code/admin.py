from typing import List, Optional
import classes.student as student
import classes.course as course


class Admin:
    def __init__(
      self, admin_name: str, admin_id: int, 
      student_edit: Optional[bool] = False, 
      student_addcourse: Optional[bool] = False,
      student_removecourse: Optional[bool] = False
      ):
      '''
      Constructor for the Admin class. By default, all permissions are false unless assigned true.

      Args:
        name (str): The name of the admin.
        id (int): An ID to identify whether admins are unique or are different sections of the same class.
        studetn_edit (bool): A boolean value that determines whether the admin can edit student information.
        student_addcourse (bool): A boolean value that determines whether the admin can add courses to students.
        student_removecourse (bool): A boolean value that determines whether the admin can remove courses from students.
      '''
      self._name = admin_name
      self._id = admin_id
      self._student_edit = student_edit
      self._student_addcourse = student_addcourse
      self._student_removecourse = student_removecourse


    @property
    def id(self):
        return self._id
  
    @property
    def name(self):
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