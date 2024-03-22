from classes import student, course, criteria

#screen creation -- import
import turtle
import tkinter as tk




def test():
  namesson = student.Student('Name N. Namesson III Jr.')
  joe = student.Student('Joe')
  john = student.Student('John')
  jane = student.Student('Jane')
  jeffrey = student.Student('Jeffrey')
  imposter = student.Student('Imposter')
  
  games = criteria.Criteria('Games')
  games.add_student(imposter)
  games.add_student(joe)
  cecs = criteria.Criteria('CECS')
  cecs.add_student(joe)
  cecs.add_student(john)
  
  g0 = course.Course('Among Us Fundamentals, Sec01', 1, 'GAME-344', games)
  imposter.add_course(g0)
  c0 = course.Course('Intro to Software Engineering, Sec05', 32, 'CECS 343', cecs)
  
  c1 = course.Course('Among Us Fundamentals, Sec02', 1, 'GAME-344', games)
  
  joe.read_notify()
  john.read_notify()
  imposter.read_notify()

  namesson.add_course(c1)
  joe.add_course(c1)
  john.add_course(c1)
  jane.add_course(c1)

  # The below is equivalent to admin.add_student(s5, c1) and disregards capacity.
  c1.add_student(jeffrey)
  jeffrey.courses.append(c1)
  # end of admin.add_student
  
  print(f'Init:\n{c1}\n')
  jane.remove_course(c1)
  print(f'Remove Jane:\n{c1}\n')
  jane.add_course(c1)
  print(f'Add Jane:\n{c1}\n')
  joe.remove_course(c1)
  print(f'Remove Joe:\n{c1}\n')
  namesson.remove_course(c1)
  print(f'Remove Name:\n{c1}\n')
  jeffrey.remove_course(c1)
  print(f'Remove Jeffrey:\n{c1}\n')

def do_stuff():
   for color in ["red", "yellow", "green"]:
    my_lovely_turtle.color(color)
    my_lovely_turtle.right(120)
def press():
   do_stuff()

def main():
  test()

  #screen creation

  # Set up the screen
  screen = turtle.Screen()
  screen.title("Admin Screen")
  #screen.setup(width=600, height=400)
  screen.bgcolor("white") 

  canvas = screen.getcanvas()
  button = tk.Button(canvas.master, text="Press me", command=press)
  canvas.create_window(-200, -100, window=button)
  my_lovely_turtle = turtle.Turtle(shape="turtle")
  turtle.done()
  # Set up the turtle
  pen = turtle.Turtle()
  pen.speed(0)  # Set the drawing speed to the fastest

  # Draw something on the screen (e.g., a rectangle)

  # Write text onto the screen
  pen.penup()
  pen.goto(0, 50)
  pen.write("Log in window", align="center", font=("Arial", 10, "normal"))

  # Keep the window open until closed by the user
  screen.mainloop()


  screen = turtle.Screen()
   
   
   



main()


                        
