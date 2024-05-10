import classes.course as course
import datetime
import sys
sys.tracebacklimit = 0

#message imports
import os
from email.message import EmailMessage
import ssl
import smtplib



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

    def read_notify(self, subject, body, recipients):
      '''
      Sends emails to students.

      Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        recipients (list): A list of recipients to check woh will get an email.
      '''
      #send to an if statement 
      for email, student_info in recipients.items():
          if student_info[1] == self:
              email_reciever = email
              break
          
      email_sender = "csulbnotifications@gmail.com"
      email_password = os.environ['EMAIL_PASSWORD']
      
      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_reciever
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

      
      
    def clear_notify(self):
      '''
      Clears the list of notifications.
      '''
      self.notifications.clear()

