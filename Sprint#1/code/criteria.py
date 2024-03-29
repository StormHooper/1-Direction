#####################################
# The following imports are used to #
# avoid circular imports.           #
# Only for type checking.           #
#####################################

from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
  import classes.student as student

class Criteria:
    def __init__(self, name: str):
      '''
      Constructor for the Criteria class.

      Args:
        name (str): The name of the criteria.
      '''
      self.name = name
      self.students = []
      
    def __str__(self):
      return self.name
      
    def add_student(self, student: student.Student) -> None:
      '''
      Adds a student to the list of students.

      Args:
        student (Student): The student to be added to the list of students.
      '''
      if student not in self.students:
        self.students.append(student)
    def remove_student(self, student: student.Student) -> None:
      '''
      Removes a student to the list of students.

      Args:
        student (Student): The student to be removed from the list of students.
      '''
      if student in self.students:
        self.students.remove(student)
    
    def __iter__(self):
      return iter(self.students) 

      