import classes.course as course

class Student:
    def __init__(self, name:str):
        self.name = name
        self.courses = []
        self.notifications = []

    def __str__(self):
        return self.name

    def add_course(self, course: course.Course):
        if course.is_full():
          course.add_wait(self)
          self.courses.append(course)

        else:
          course.add_student(self)
          self.courses.append(course)

    def remove_course(self, course: course.Course):
        course.remove_student(self)
        self.courses.remove(course)


    # THE FOLLOWING ARE ONLY FOR TESTING PURPOSES, PLEASE REMOVE AND ADD TO INTERFACE OR SOMETHING LATER
    def notify(self, notification: str):
      self.notifications.append(notification)

    def read_notify(self):
      i = 1
      print(f'Notifications for {self.name}:')
      for notification in self.notifications:
        print(f'{i}:\n{notification}\n')
        i+=1
      if len(self.notifications) == 0:
        print('No notifications found.\n')
        
    def clear_notify(self):
      self.notifications.clear()
