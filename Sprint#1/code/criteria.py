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
        self.name = name
        self.students = []
    def __str__(self):
      return self.name
      
    def add_student(self, student: student.Student) -> None:
      if student not in self.students:
        self.students.append(student)
    def remove_student(self, student: student.Student) -> None:
      if student in self.students:
        self.students.remove(student)
    
    def __iter__(self):
      return iter(self.students) 

      
