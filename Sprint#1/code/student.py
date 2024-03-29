import classes.course as course
import datetime
import sys
sys.tracebacklimit = 0



class Student:
    def __init__(self, id: int, name:str):
      '''
      Constructor for the Student class.

      Args:
        id (int): An ID to identify whether students are unique or are different sections of the same class.
        name (str): The name of the student.
      '''
      self._id = id
      self._name = name
      self.courses = []
      self.notifications = []
        

    def __str__(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    def add_course(self, course: course.Course):
      '''
      Adds a student to course if not full. 

      Args:
        course (Course): The course to be added to the student's courses.
      '''
      try:
        if course.is_full():
          invalid = True
          while invalid:
            waitlist = input("Class is full. Waitlist? [Y/N]\n")
            if waitlist.upper() == "Y":
              invalid = False
              course.add_wait(self)
              self.courses.append(course)
            elif waitlist.upper() == "N":
              invalid = False
              return
            else:
              print("Invalid input. Please try again.")           
        else:
          course.add_student(self)
          self.courses.append(course)
      except Exception as err:
        print(err)

    def remove_course(self, course: course.Course):
        course.remove_student(self)
        self.courses.remove(course)


    # THE FOLLOWING SHOULD BE UPDATED TO INTERFACE OR SOMETHING LATER, MAINLY READ_NOTIFY
    def notify(self, notification: str):
      '''
      Delivers a notification to the list of students. (MAY BE MOVED!!)

      Args:
        notification (str): The notification to be delivered.
      '''
      timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      self.notifications.append([timestamp, notification])

    def read_notify(self):
      '''
      Reads the list of notifications.
      '''
      i = 1
      print(f'Notifications for {self._name}:')
      for notification in self.notifications:
        timestamp = notification[0]
        note = notification[1]
        print(f'Notification {i} [{timestamp}]:\n{note}\n')
        i+=1
      if len(self.notifications) == 0:
        print('No notifications found.\n')
        
    def clear_notify(self):
      '''
      Clears the list of notifications.
      '''
      self.notifications.clear()
