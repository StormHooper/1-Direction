from typing import List, Optional
import classes.student as student
import classes.course as course

class Admin:
    def __init__(self, admin_name: str, admin_id: int, permissions: List[bool]):
        self.admin_name = admin_name
        self.admin_id = admin_id
        self.permissions = permissions

    def edit_student_info(self, student_obj: student.Student) -> None:
        """
        Edit student information.

        Args:
            student_obj (student.Student): The student object whose information needs to be edited.
        """
        if self.permissions[0]:  # Assuming permissions[0] indicates permission to edit student info
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
        if self.permissions[1]:  # Assuming permissions[1] indicates permission to add courses to students
            if not course_obj.is_full():
                student_obj.add_course(course_obj)
                course_obj.add_student(student_obj)
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
        if self.permissions[2]:  # Assuming permissions[2] indicates permission to remove courses from students
            if course_obj in student_obj.courses:
                student_obj.remove_course(course_obj)
                course_obj.remove_student(student_obj)
                print(f"Course {course_obj.name} removed from {student_obj.name}.")
            else:
                print(f"Student {student_obj.name} is not enrolled in course {course_obj.name}.")
        else:
            print("You don't have permission to remove courses from students.")
