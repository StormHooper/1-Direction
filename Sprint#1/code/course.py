#####################################
# The following imports are used to #
# avoid circular imports.           #
# Only for type checking.           #
#####################################

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  import classes.student as student

# This import is used for declaring an optional argument
from typing import Optional, List

import classes.criteria as criteria


class Course:
    def __init__(self, name:str, capacity: int, id: str, *criteria: Optional[criteria.Criteria]):
      '''
      Constructor for the Course class.
      
      Args:
        capacity (int): The maximum number of students that can be enrolled in the course.
        id (int): An ID to identify whether courses are unique or are different sections of the same class.
      '''
      self.name = name
      self.id = id
      self.capacity = capacity
      self.students = [] 
      self.waitlist = []
      self.criteria = [criterion for criterion in criteria]
      self.notify()


    def __str__(self): #STRING OUTPUT FOR COURSE
      return(
        f'Course: {self.name}\n' \
        f' | ID: {self.id}\n' \
        f' | Capacity: {len(self.students)}/{self.capacity}\n' \
        f' | Students: {list(map(str,self.students))}\n' \
        f' | Waitlist: {list(map(str,self.waitlist))}\n' \
        f' | Criteria: {list(map(str,self.criteria))}\n'
      )

    def notify(self) -> None:
      '''
      Notifies all students which include this class in their criteria that the course has been opened.
      '''      
      for criterion in self.criteria:
        for student in criterion:
          notified = False
          for course in student.courses:
            if course.id == self.id:
              student.notify( \
                f'A new section for course {self.name} ({self.id}) ' \
                'has been opened. ' \
                'You were previously registered or waitlisted ' \
                'for this course. ' \
                f'({course.name})')
              notified = True
              break
          if not notified:
            student.notify( \
              f'A new section for course {self.name} ({self.id}) '\
              'has been opened.')
          
            
          
        

    def is_full(self) -> bool:
      return len(self.students) >= self.capacity

    def add_student(self, student: student.Student) -> None:
      '''
      Adds a student to the course.
      
      Args:
        student (Student): The student to be added to the course.
      '''
      if student not in self.students:
        self.students.append(student)

    def remove_student(self, student: student.Student) -> None:
      '''
      Removes a student from the course.
      
      Args:
        student (Student): The student to be removed from the course.
      '''

      if student in self.students:
        self.students.remove(student)
        
        if len(self.waitlist) > 0 and not self.is_full():
          self.add_student(self.remove_wait())
          
      elif student in self.waitlist:
        self.remove_wait(student) 
      

    def add_wait(self, student:student.Student):
      '''
      Adds a student to the waitlist.
      
      Args:
        student (Student): The student to be added to the waitlist.
      '''
      self.waitlist.append(student)

    def remove_wait(self, student: Optional[student.Student] = None) -> student.Student:
      '''
      Removes a student from the waitlist. If no student is specified, the first   student in the waitlist is removed.
      
      Args:
        student (Student): The student to be removed from the waitlist.
      '''
      if student is None:
        push = self.waitlist[0]
        self.waitlist.remove(push)
        return push
      elif student in self.waitlist:
        self.waitlist.remove(student)
        return student
      else:
        print(f"Unexpected exception has occured in course: {self.name}")
      

