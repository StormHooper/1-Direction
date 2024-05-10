import pygame, sys
from classes import student, course, criteria, admin, interface
import os
from email.message import EmailMessage
import ssl
import smtplib


pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

fullscreen = True  # Set to True for fullscreen mode
flags = pygame.FULLSCREEN if fullscreen else 0
#screen = pygame.display.set_mode((screen_width, screen_height), flags)

#just changed to make it window sized
screen = pygame.display.set_mode((screen_width, screen_height))

#background image
#image = pygame.image.load("wall.jpg")
#image = pygame.image.load("sukuna.webp")
#image = pygame.image.load("among-us-sus.png")
#image = pygame.image.load("milad-fakurian-MBgK-AHSrVs-unsplash.jpg")
image = pygame.image.load("cool-background.png")

#image = pygame.transform.scale(image, (screen_width, screen_height))
# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Class Management System')



logged_in = False
failed = False
check_int = False
x = None
user_type = None
color_inactive = pygame.Color('black')
color_active = pygame.Color('white')
color_name = color_inactive
input_box_name = pygame.Rect(300, 250, 200, 32)
name = ""
course_name = ""
capacity = ""
course_id = ""
temp1 = ""
temp2 = ""
temp3 = ""
active = None
active1 = None
active2 = None
active3 = None
confirmed1 = False
confirmed2 = False
confirmed3 = False
confirmed4 = False


def create_centered_button(x, y, text, color, action):
    # Calculate text width (adjust the font size as needed)
    font_size = 16
    text_width = len(text) * font_size

    # Calculate button dimensions
    button_width = max(200, text_width + 20)  # Minimum width of 200
    button_height = 50

    # Center the button horizontally
    button_x = (x - button_width // 2) + 100

    # Create the button
    button = Button(button_x, y, button_width, button_height, color, text, action)
    return button

# Function to get integer input within a range
def get_int_range(prompt: str, min: int, max: int) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in range(min, max + 1):
                return choice
            else:
                pass
                
        except ValueError:
            pass
            

# Function to display student actions
def display_student_actions(user) -> int:
    # Function to handle button clicks for student actions

    choice = None

    def handle_button_click(button_index):
        nonlocal choice
        choice = button_index

    # Function to exit the program
    def exit_program():
        pygame.quit()
        sys.exit()

    # Display student actions
    font = pygame.font.Font(None, 32)
    student_name_text = f"Welcome {user}!"
    student_name = font.render(student_name_text, True, (0, 0, 0))
    student_action_text = font.render("Student Actions:", True, (0, 0, 0))
    text_width, _ = font.size(student_name_text)
    center_x = (screen.get_width() - text_width) // 2
    screen.blit(student_name, (center_x, 50))
    screen.blit(student_action_text, (200, 50))
    # Add more student actions as needed


    # Create buttons for each option
    # view_courses_button = Button(300, 200, 200, 50, (0, 128, 0), "View courses", lambda: handle_button_click(1))
    # add_button = Button(300, 260, 200, 50, (0, 128, 0), "Add course to schedule", lambda: handle_button_click(2))
    # remove_button = Button(300, 320, 200, 50, (0, 128, 0), "Remove course from schedule", lambda: handle_button_click(3))
    # notifications_button = Button(300, 380, 200, 50, (0, 128, 0), "View notifications", lambda: handle_button_click(4))
    # log_out_button = Button(300, 440, 200, 50, (0, 0, 255), "Log out", lambda: handle_button_click(0))
    # exit_button = Button(300, 500, 200, 50, (255, 0, 0), "Exit", exit_program)

    view_courses_button = create_centered_button(300, 200, "View courses", (0, 128, 0), lambda: handle_button_click(1))
    add_button = create_centered_button(300, 260, "Add course to schedule", (0, 128, 0), lambda: handle_button_click(2))
    remove_button = create_centered_button(300, 320, "Remove course from schedule", (0, 128, 0), lambda: handle_button_click(3))
    notifications_button = create_centered_button(300, 380, "View notifications", (0, 128, 0), lambda: handle_button_click(4))
    log_out_button = create_centered_button(300, 440, "Log out", (0, 0, 255), lambda: handle_button_click(0))
    exit_button = create_centered_button(300, 500, "Exit", (255, 0, 0), exit_program)


    # Main loop for handling events and drawing buttons
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button events
            view_courses_button.handle_event(event)
            add_button.handle_event(event)
            remove_button.handle_event(event)
            notifications_button.handle_event(event)
            log_out_button.handle_event(event)
            exit_button.handle_event(event)

        # Clear the screen
        #screen.fill((169, 169, 169))
        screen.blit(image, (0, 0)) 
        #screen.fill((75,75,75))

        screen.blit(student_name, (center_x, 100))
        screen.blit(student_action_text, (310, 150))

        # Draw buttons
        view_courses_button.draw()
        add_button.draw()
        remove_button.draw()
        notifications_button.draw()
        log_out_button.draw()
        exit_button.draw()

        # Update the display
        pygame.display.flip()
    return choice

def display_student_courses(student_course_list):
    # Function to handle button clicks for course selection
    def handle_button_click(button_index):
        nonlocal choice
        choice = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    # Initialize choice to None
    choice = None


    font = pygame.font.Font(None, 32)
    courses = []
    space_for_button = 0

    #screen.fill((169, 169, 169))
    screen.blit(image, (0, 0)) 
    if len(student_course_list) > 0:
        for i, course in enumerate(student_course_list):
            course_name = font.render(f"{i + 1}. {student_course_list[i].name}", True, (0, 0, 0))
            courses.append(course_name)
        space_for_button = 0
        for i, course in enumerate(courses):
            screen.blit(course, (100, 200 + i * 50))
            space_for_button = i

    while choice is None:

        back_button = Button(300, 300 + space_for_button * 50, 200, 50, (255, 255, 0), "Back", lambda: handle_button_click(-1))
        exit_button = Button(300, 375 + space_for_button * 50, 200, 50, (255, 0, 0), "Exit", exit_program)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            back_button.handle_event(event)
            exit_button.handle_event(event)

        back_button.draw()
        exit_button.draw()
        if len(student_course_list) == 0:
            font = pygame.font.Font(None, 32)
            no_notifications = font.render("You currently have no classes in your schedule", True, (0, 0, 0))
            screen.blit(no_notifications, (140, 225))
        pygame.display.flip()


    return choice

def display_course_selection(user, course_list) -> int:
    # Function to handle button clicks for course selection
    def handle_button_click(button_index):
        nonlocal choice
        choice = button_index

    def handle_button_click2(button_index):
        nonlocal choice2
        choice2 = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    # Initialize choice to None
    choice = None
    choice2 = None

    # Initialize scroll position
    scroll_position = 0

    # Define constants for scroll bar
    SCROLLBAR_WIDTH = 10
    SCROLLBAR_COLOR = (100, 100, 100)
    SCROLLBAR_BG_COLOR = (200, 200, 200)

    # Create buttons for each course
    def create_buttons():
        buttons = []
        for i, course in enumerate(course_list):
            button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), course.name, lambda i=i: handle_button_click(i))
            buttons.append(button)
        back_button = Button(100, 200 + len(course_list) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click(-1))
        exit_button = Button(100, 200 + len(course_list) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
        return buttons, back_button, exit_button

    # Function to calculate visible courses based on scroll position
    def calculate_visible_courses(course_list, scroll_position):
        visible_courses = []
        y = 200
        for i, course in enumerate(course_list):
            if y >= 200:  # Check if course is within visible area
                visible_courses.append((i, course))
            y += 60  # Increase y position for next course
        return visible_courses

    # Main loop for handling events and drawing buttons
    if choice is None:
        buttons, back_button, exit_button = create_buttons()
    while choice is None:
        # Calculate visible courses based on scroll position
        visible_courses = calculate_visible_courses(course_list, scroll_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button events
            for button_index, course in visible_courses:
                buttons[button_index].handle_event(event)
            back_button.handle_event(event)
            exit_button.handle_event(event)
            # Handle scroll events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    scroll_position = max(0, scroll_position - 1)
                elif event.button == 5:  # Scroll down
                    scroll_position = min(len(course_list) - 3, scroll_position + 1)

        # Clear the screen
        #screen.fill((169, 169, 169))
        screen.blit(image, (0, 0)) 
        # Draw course buttons
        for button_index, course in visible_courses:
            buttons[button_index].rect.y = 200 + (button_index - scroll_position) * 60
            buttons[button_index].draw()
        back_button.rect.y = 200 + (len(course_list) - scroll_position) * 60
        exit_button.rect.y = 200 + (len(course_list) + 1 - scroll_position) * 60
        back_button.draw()
        exit_button.draw()

        # Draw scrollbar background
        pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

        # Calculate scrollbar height and position
        scrollbar_height = min(300, 300 * 300 / len(course_list))  # 300 is the height of the visible area
        scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(course_list) - 3)

        # Draw scrollbar
        pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))

        # Update the display
        pygame.display.flip()
        if choice == -1:
            return choice
        if choice != None and choice != -1:
            pass


        if choice != -1 and choice != None and course_list[choice].is_full() and course_list[choice] not in user.courses and user not in course_list[choice].waitlist:
            pass

            invalid = True
            choice2 = None
            while invalid:
                # add_waitlist = Button(100, 140, 600, 50, (0, 255, 0), "Join Waitlist", lambda: handle_button_click2(1))
                # no_waitlist= Button(100, 200, 600, 50, (0, 255, 0), "Refuse Waitlist", lambda: handle_button_click2(2))
                # back_button = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click2(-1))

                add_waitlist = create_centered_button(300, 140, "Join Waitlist", (0, 128, 0), lambda: handle_button_click2(1))
                no_waitlist = create_centered_button(300, 200, "Refuse Waitlist", (0, 128, 0), lambda: handle_button_click2(2))
                back_button = create_centered_button(300, 320, "Back", (255, 255, 0), lambda: handle_button_click2(-1))

         
                exit_button = create_centered_button(300, 380, "Exit", (255, 0, 0), exit_program)

                #exit_button = Button(100, 200 + 2 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    add_waitlist.handle_event(event)
                    no_waitlist.handle_event(event)
                    back_button.handle_event(event)
                    exit_button.handle_event(event)

                screen.blit(image, (0, 0))


                add_waitlist.draw()
                no_waitlist.draw()
                back_button.draw()
                exit_button.draw()
                if choice2 == 1:
                    invalid = False
                    course_list[choice].add_wait(user)
                    user.notify(f"You have been added to the waitlist of {course_list[choice].name}!")
                    choice = -1
                elif choice2 == 2:
                    invalid = False
                    choice = -1
                elif choice2 == -1:
                    invalid = False
                    choice = None
                    buttons, back_button, exit_button = create_buttons()
                pygame.display.flip()

    if course_list[choice] in user.courses or user in course_list[choice].waitlist:
        return -1
    return choice

def display_student_courses_remove(student_course_list) -> int:
    # Function to handle button clicks for course selection
    screen.blit(image, (0, 0)) 
    def handle_button_click(button_index):
        nonlocal choice
        choice = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    font = pygame.font.Font(None, 32)

    # Initialize choice to None
    choice = None

    # Initialize scroll position
    scroll_position = 0

    # Define constants for scroll bar
    if len(student_course_list) > 0:
        SCROLLBAR_WIDTH = 10
        SCROLLBAR_COLOR = (100, 100, 100)
        SCROLLBAR_BG_COLOR = (200, 200, 200)

    # Create buttons for each course
    buttons = []

    for i, course in enumerate(student_course_list):
        button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), course.name, lambda i=i: handle_button_click(i))
        buttons.append(button)
    if len(student_course_list) > 0:
        back_button = Button(100, 200 + len(student_course_list) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click(-1))
        exit_button = Button(100, 200 + len(student_course_list) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
    else:
        back_button = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click(-1))
        exit_button = Button(100, 200 + 1 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)

    # Function to calculate visible courses based on scroll position
    def calculate_visible_courses(student_course_list, scroll_position):
        visible_courses = []
        y = 200
        for i, course in enumerate(student_course_list):
            if y >= 200:  # Check if course is within visible area
                visible_courses.append((i, course))
            y += 60  # Increase y position for next course
        return visible_courses

    # Main loop for handling events and drawing buttons
    while choice is None:
        # Calculate visible courses based on scroll position
        visible_courses = calculate_visible_courses(student_course_list, scroll_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button events
            for button_index, course in visible_courses:
                buttons[button_index].handle_event(event)
            back_button.handle_event(event)
            exit_button.handle_event(event)
            # Handle scroll events
            if event.type == pygame.MOUSEBUTTONDOWN and len(student_course_list) > 0:
                if event.button == 4:  # Scroll up
                    scroll_position = max(0, scroll_position - 1)
                elif event.button == 5:  # Scroll down
                    scroll_position = min(len(student_course_list) - 3, scroll_position + 1)

        # Clear the screen
        #screen.fill((169, 169, 169))
        screen.blit(image, (0, 0)) 
        # Draw course buttons
        for button_index, course in visible_courses:
            buttons[button_index].rect.y = 200 + (button_index - scroll_position) * 60
            buttons[button_index].draw()
        if len(student_course_list) > 0:
            back_button.rect.y = 200 + (len(student_course_list) - scroll_position) * 60
            exit_button.rect.y = 200 + (len(student_course_list) + 1 - scroll_position) * 60
            back_button.draw()
            exit_button.draw()
        else:
            back_button.rect.y = 200 + (1 - scroll_position) * 60
            exit_button.rect.y = 200 + (1 + 1 - scroll_position) * 60
            back_button.draw()
            exit_button.draw()

        # Draw scrollbar background
        if len(student_course_list) > 0:
            pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

        # Calculate scrollbar height and position
        if len(student_course_list) > 0:
            scrollbar_height = min(300, 300 * 300 / len(student_course_list))  # 300 is the height of the visible area
            scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(student_course_list))
        else:
            scrollbar_height = min(300, 300 * 300 / 2)  # 300 is the height of the visible area
            scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (2 - 3)

        # Draw scrollbar
        if len(student_course_list) > 0:
            pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))
        if len(student_course_list) == 0:
            student_action_text = font.render("You have no classes in your schedule", True, (0, 0, 0))
            screen.blit(student_action_text, (200, 200))

        # Update the display
        pygame.display.flip()

    return choice


def display_notifications(user) -> int:


    def handle_button_click(button_index):
        nonlocal choice
        choice = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    choice = None

    font = pygame.font.Font(None, 22)
    notifications = []
    space_for_button = 0

    #screen.fill((169, 169, 169))
    screen.blit(image, (0, 0)) 
    if len(user.notifications) > 0:
        for i, notification in enumerate(user.notifications):
            # Split notification into multiple lines based on a specified length
            max_line_length = 30  # Adjust as needed
            lines = [notification[j:j+max_line_length] for j in range(0, len(notification), max_line_length)]
            for line_index, line in enumerate(lines):
                # Ensure line is a Unicode string
                line = str(line)
                message = font.render(line, True, (0, 0, 0))
                notifications.append(message)
        space_for_button = 0
        for i, notification in enumerate(notifications):
            screen.blit(notification, (25, 200 + i * 25))
            space_for_button = i

    while choice is None:

        back_button = Button(300, 250 + space_for_button * 25, 200, 50, (255, 255, 0), "Back", lambda: handle_button_click(-1))
        exit_button = Button(300, 325 + space_for_button * 25, 200, 50, (255, 0, 0), "Exit", exit_program)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            back_button.handle_event(event)
            exit_button.handle_event(event)

        back_button.draw()
        exit_button.draw()
        if len(user.notifications) == 0:
            font = pygame.font.Font(None, 32)
            no_notifications = font.render("You currently have no new notifications", True, (0, 0, 0))
            screen.blit(no_notifications, (185, 200))
        pygame.display.flip()

    return choice

# Function to display admin actions
def display_admin_actions(user) -> int:
    choice = None

    def handle_button_click(button_index):
        nonlocal choice
        choice = button_index

    # Function to exit the program
    def exit_program():
        pygame.quit()
        sys.exit()

    # Display student actions
    font = pygame.font.Font(None, 32)
    admin_name_text = f"Welcome {user}!"
    admin_name = font.render(admin_name_text, True, (0, 0, 0))
    admin_action_text = font.render("Admin Actions:", True, (0, 0, 0))
    text_width, _ = font.size(admin_name_text)
    center_x = (screen.get_width() - text_width) // 2
    screen.blit(admin_name, (center_x, 150))
    screen.blit(admin_action_text, (200, 75))
    # Add more student actions as needed


    # Create buttons for each option

    # create_new_student_button = Button(300, 140, 200, 50, (0, 128, 0), "Create New Student Email", lambda: handle_button_click(5))


    # edit_student_name_button = Button(300, 200, 200, 50, (0, 128, 0), "Edit student name", lambda: handle_button_click(1))
    # add_course_student_button = Button(300, 260, 200, 50, (0, 128, 0), "Add course to a student", lambda: handle_button_click(2))
    # remove_course_student_button = Button(300, 320, 200, 50, (0, 128, 0), "Remove course from student", lambda: handle_button_click(3))
    # create_course_button = Button(300, 380, 200, 50, (0, 128, 0), "Create a new course", lambda: handle_button_click(4))
    # log_out_button = Button(300, 440, 200, 50, (255, 255, 0), "Log out", lambda: handle_button_click(0))
    # exit_button = Button(300, 500, 200, 50, (255, 0, 0), "Exit", exit_program)

    # Example usage:
    # create_new_student_button = create_button(300, 140, "Create New Student Email", (0, 128, 0), lambda: handle_button_click(5))
    # edit_student_name_button = create_button(300, 200, "Edit student name", (0, 128, 0), lambda: handle_button_click(1))
    # add_course_student_button = create_button(300, 260, "Add course to a student", (0, 128, 0), lambda: handle_button_click(2))
    # remove_course_student_button = create_button(300, 320, "Remove course from student", (0, 128, 0), lambda: handle_button_click(3))
    # create_course_button = create_button(300, 380, "Create a new course", (0, 128, 0), lambda: handle_button_click(4))
    # log_out_button = create_button(300, 440, "Log out", (255, 255, 0), lambda: handle_button_click(0))
    # exit_button = create_button(300, 500, "Exit", (255, 0, 0), exit_program)

    #create_new_student_button = create_centered_button(300, 140, "Create New Student Email", (0, 128, 0), lambda: handle_button_click(5))
    edit_student_name_button = create_centered_button(300, 200, "Edit student name", (0, 128, 0), lambda: handle_button_click(1))
    add_course_student_button = create_centered_button(300, 260, "Add course to a student", (0, 128, 0), lambda: handle_button_click(2))
    remove_course_student_button = create_centered_button(300, 320, "Remove course from student", (0, 128, 0), lambda: handle_button_click(3))
    create_course_button = create_centered_button(300, 380, "Create a new course", (0, 128, 0), lambda: handle_button_click(4))
    log_out_button = create_centered_button(300, 440, "Log out", (255, 255, 0), lambda: handle_button_click(0))
    exit_button = create_centered_button(300, 500, "Exit", (255, 0, 0), exit_program)

  

    # Main loop for handling events and drawing buttons
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button events
            #create_new_student_button.handle_event(event)
            edit_student_name_button.handle_event(event)
            add_course_student_button.handle_event(event)
            remove_course_student_button.handle_event(event)
            create_course_button.handle_event(event)
            log_out_button.handle_event(event)
            exit_button.handle_event(event)

        # Clear the screen
        #screen.fill((169, 169, 169))
        screen.blit(image, (0, 0)) 
        screen.blit(admin_name, (center_x, 100))
        screen.blit(admin_action_text, (310, 150))

        # Draw buttons
        #create_new_student_button.draw()
        edit_student_name_button.draw()
        add_course_student_button.draw()
        remove_course_student_button.draw()
        create_course_button.draw()
        log_out_button.draw()
        exit_button.draw()

        # Update the display
        pygame.display.flip()
    return choice

def handle_input_events_admin(event, user, students, choice1):
    global input_box_name, color_name, color_active, color_inactive, name, active
    new_name = None
    #print(active1)
    #nonlocal input_box_name, color_name, color_active, color_inactive
    if event.type == pygame.MOUSEBUTTONDOWN:
        #print(name)
        #print('adskfdskafksadf')
        # If the user clicks on the input box, toggle active
        if input_box_name.collidepoint(event.pos):
            active = input_box_name
            color_name = color_active
        else:
            active = None
            color_name = color_inactive
    if event.type == pygame.KEYDOWN:
        #print('Hi')
        #print(active1)
        if active:
            if event.key == pygame.K_RETURN:
                # Perform action here (e.g., login)
                temp_name = name
                name = ""
                user.edit_student_info(students[choice1], temp_name)
                return True
                # Clear the input fields after login
            elif event.key == pygame.K_BACKSPACE:
                if active == input_box_name:
                    name = name[:-1]
            else:
                if active == input_box_name:
                    name += event.unicode

def change_student_name_admin(user, students):
    global name
    new_name = ""
    x = False
    choice1 = None
    choice2 = None

    def handle_button_click1(button_index):
        nonlocal choice1
        choice1 = button_index

    def handle_button_click2(button_index):
        nonlocal choice2
        choice2 = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    font = pygame.font.Font(None, 32)

    # Initialize scroll position
    scroll_position = 0

    # Define constants for scroll bar
    if len(students) > 0:
        SCROLLBAR_WIDTH = 10
        SCROLLBAR_COLOR = (100, 100, 100)
        SCROLLBAR_BG_COLOR = (200, 200, 200)

    # Create buttons for each course
    buttons = []

    for i, student in enumerate(students):
        button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), student.name, lambda i=i: handle_button_click1(i))
        buttons.append(button)
    if len(students) > 0:
        back_button = Button(100, 200 + len(students) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
        exit_button = Button(100, 200 + len(students) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
    else:
        back_button = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
        exit_button = Button(100, 200 + 1 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)

    # Function to calculate visible courses based on scroll position
    def calculate_visible_students(students, scroll_position):
        visible_students = []
        y = 200
        for i, student in enumerate(students):
            if y >= 200:  # Check if course is within visible area
                visible_students.append((i, student))
            y += 60  # Increase y position for next course
        return visible_students

    # Main loop for handling events and drawing buttons
    while choice1 is None:
        # Calculate visible courses based on scroll position
        visible_students = calculate_visible_students(students, scroll_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button events
            for button_index, student in visible_students:
                buttons[button_index].handle_event(event)
            back_button.handle_event(event)
            exit_button.handle_event(event)
            # Handle scroll events
            if event.type == pygame.MOUSEBUTTONDOWN and len(students) > 0:
                if event.button == 4:  # Scroll up
                    scroll_position = max(0, scroll_position - 1)
                elif event.button == 5:  # Scroll down
                    scroll_position = min(len(students) - 3, scroll_position + 1)

        # Clear the screen
        #screen.fill((169, 169, 169))
        screen.blit(image, (0, 0)) 
        # Draw course buttons
        for button_index, student in visible_students:
            buttons[button_index].rect.y = 200 + (button_index - scroll_position) * 60
            buttons[button_index].draw()
        if len(students) > 0:
            back_button.rect.y = 200 + (len(students) - scroll_position) * 60
            exit_button.rect.y = 200 + (len(students) + 1 - scroll_position) * 60
            back_button.draw()
            exit_button.draw()
        else:
            back_button.rect.y = 200 + (1 - scroll_position) * 60
            exit_button.rect.y = 200 + (1 + 1 - scroll_position) * 60
            back_button.draw()
            exit_button.draw()

        # Draw scrollbar background
        if len(students) > 0:
            pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

        # Calculate scrollbar height and position
        if len(students) > 0:
            scrollbar_height = min(300, 300 * 300 / len(students))  # 300 is the height of the visible area
            scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(students))
        else:
            scrollbar_height = min(300, 300 * 300 / 2)  # 300 is the height of the visible area
            scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (2 - 3)

        # Draw scrollbar
        if len(students) > 0:
            pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))
        if len(students) == 0:
            student_action_text = font.render("You have no classes in your schedule", True, (0, 0, 0))
            screen.blit(student_action_text, (200, 200))

        # Update the display
        pygame.display.flip()

    if choice1 == -1:
        return choice1

    back_button = Button(100, 300 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click2(-1))
    exit_button = Button(100, 300 + 2 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)

    name = ""
    while choice2 is None:
        x = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle input events
            #x = False
            x = handle_input_events_admin(event, user, students, choice1)
            # Handle button events
            exit_button.handle_event(event)
            back_button.handle_event(event)

        #print(new_name)
#        screen.fill((169, 169, 169))
        screen.blit(image, (0, 0)) 
        font = pygame.font.Font(None, 32)
        new_student_name = font.render("New Student Name", True, (0, 0, 0))
        screen.blit(new_student_name, (298, 225))
        pygame.draw.rect(screen, color_name, input_box_name, 2)

        back_button.draw()
        exit_button.draw()
        text_surface_name = font.render(name, True, (0, 0, 0))

        screen.blit(text_surface_name, (302, 255))

        if x == True:
            students[choice1].notify(f"{user}, an admin, has changed your name!")
            return choice1

        pygame.display.flip()
        #print(new_name)

    if choice2 == -1:
        change_student_name_admin(user, students)

def add_course_student_admin(user, students, course_list):
    choice1 = None
    choice2 = None

    def handle_button_click1(button_index):
        nonlocal choice1
        choice1 = button_index

    def handle_button_click2(button_index):
        nonlocal choice2
        choice2 = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    #screen.fill((169, 169, 169))
    font = pygame.font.Font(None, 32)

    # Initialize scroll position
    scroll_position = 0

    # Define constants for scroll bar
    if len(students) > 0:
        SCROLLBAR_WIDTH = 10
        SCROLLBAR_COLOR = (100, 100, 100)
        SCROLLBAR_BG_COLOR = (200, 200, 200)

    # Create buttons for each course
    buttons1 = []

    for i, student in enumerate(students):
        button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), student.name, lambda i=i: handle_button_click1(i))
        buttons1.append(button)
    if len(students) > 0:
        back_button1 = Button(100, 200 + len(students) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
        exit_button1 = Button(100, 200 + len(students) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
    else:
        back_button1 = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
        exit_button1 = Button(100, 200 + 1 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)


    # Function to calculate visible courses based on scroll position
    def calculate_visible_students(students, scroll_position):
        visible_students = []
        y = 200
        for i, student in enumerate(students):
            if y >= 200:  # Check if course is within visible area
                visible_students.append((i, student))
            y += 60  # Increase y position for next course
        return visible_students

    # Main loop for handling events and drawing buttons
    while choice1 is None:
        # Calculate visible courses based on scroll position
        visible_students = calculate_visible_students(students, scroll_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button events
            for button_index, student in visible_students:
                buttons1[button_index].handle_event(event)
            back_button1.handle_event(event)
            exit_button1.handle_event(event)
            # Handle scroll events
            if event.type == pygame.MOUSEBUTTONDOWN and len(students) > 0:
                if event.button == 4:  # Scroll up
                    scroll_position = max(0, scroll_position - 1)
                elif event.button == 5:  # Scroll down
                    scroll_position = min(len(students) - 3, scroll_position + 1)

        # Clear the screen
        screen.blit(image, (0, 0)) 
        # Draw course buttons
        for button_index, student in visible_students:
            buttons1[button_index].rect.y = 200 + (button_index - scroll_position) * 60
            buttons1[button_index].draw()
        if len(students) > 0:
            back_button1.rect.y = 200 + (len(students) - scroll_position) * 60
            exit_button1.rect.y = 200 + (len(students) + 1 - scroll_position) * 60
            back_button1.draw()
            exit_button1.draw()
        else:
            back_button1.rect.y = 200 + (1 - scroll_position) * 60
            exit_button1.rect.y = 200 + (1 + 1 - scroll_position) * 60
            back_button1.draw()
            exit_button1.draw()

        # Draw scrollbar background
        if len(students) > 0:
            pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

        # Calculate scrollbar height and position
        if len(students) > 0:
            scrollbar_height = min(300, 300 * 300 / len(students))  # 300 is the height of the visible area
            scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(students))
        else:
            scrollbar_height = min(300, 300 * 300 / 2)  # 300 is the height of the visible area
            scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (2 - 3)

        # Draw scrollbar
        if len(students) > 0:
            pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))
        if len(students) == 0:
            student_action_text = font.render("There aren't any students", True, (0, 0, 0))
            screen.blit(student_action_text, (200, 200))

        # Update the display

        pygame.display.flip()

        if choice1 == -1:
            return -1, -1

        elif choice1 != -1 and choice1 != None:
            scroll_position = 0

            # Define constants for scroll bar
            if len(course_list) > 0:
                SCROLLBAR_WIDTH = 10
                SCROLLBAR_COLOR = (100, 100, 100)
                SCROLLBAR_BG_COLOR = (200, 200, 200)

            # Create buttons for each course
            buttons2 = []

            for i, course in enumerate(course_list):
                button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), course.name, lambda i=i: handle_button_click2(i))
                buttons2.append(button)
            if len(course_list) > 0:
                back_button2 = Button(100, 200 + len(course_list) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click2(-2))
                exit_button2 = Button(100, 200 + len(course_list) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
            else:
                back_button2 = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click2(-2))
                exit_button2 = Button(100, 200 + 1 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)

            # Main loop for handling events and drawing buttons
            while choice1 != -1:
                # Calculate visible courses based on scroll position
                visible_courses = calculate_visible_students(course_list, scroll_position)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # Handle button events
                    for button_index, course in visible_courses:
                        buttons2[button_index].handle_event(event)
                    back_button2.handle_event(event)
                    exit_button2.handle_event(event)
                    # Handle scroll events
                    if event.type == pygame.MOUSEBUTTONDOWN and len(course_list) > 0:
                        if event.button == 4:  # Scroll up
                            scroll_position = max(0, scroll_position - 1)
                        elif event.button == 5:  # Scroll down
                            scroll_position = min(len(course_list) - 3, scroll_position + 1)

                # Clear the screen
                screen.blit(image, (0, 0)) 
                # Draw course buttons
                for button_index, course in visible_courses:
                    buttons2[button_index].rect.y = 200 + (button_index - scroll_position) * 60
                    buttons2[button_index].draw()
                if len(course_list) > 0:
                    back_button2.rect.y = 200 + (len(course_list) - scroll_position) * 60
                    exit_button2.rect.y = 200 + (len(course_list) + 1 - scroll_position) * 60
                    back_button2.draw()
                    exit_button2.draw()
                else:
                    back_button2.rect.y = 200 + (1 - scroll_position) * 60
                    exit_button2.rect.y = 200 + (1 + 1 - scroll_position) * 60
                    back_button2.draw()
                    exit_button2.draw()

                # Draw scrollbar background
                if len(course_list) > 0:
                    pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

                # Calculate scrollbar height and position
                if len(course_list) > 0:
                    scrollbar_height = min(300, 300 * 300 / len(course_list))  # 300 is the height of the visible area
                    scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(course_list))
                else:
                    scrollbar_height = min(300, 300 * 300 / 2)  # 300 is the height of the visible area
                    scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (2 - 3)

                # Draw scrollbar
                if len(course_list) > 0:
                    pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))
                if len(course_list) == 0:
                    course_action_text = font.render("There aren't any classes", True, (0, 0, 0))
                    screen.blit(course_action_text, (200, 200))


                # Update the display
                pygame.display.flip()

                if choice2 == -2:
                    choice1 = None
                    choice2 = None
                    scroll_position = 0
                    break

                elif choice2 != None and choice2 >= 0:
                    if course_list[choice2].is_full():
                        return -1, -1
                    return choice1, choice2


def remove_course_student_admin(user, students):
  choice1 = None
  choice2 = None

  def handle_button_click1(button_index):
      nonlocal choice1
      choice1 = button_index

  def handle_button_click2(button_index):
      nonlocal choice2
      choice2 = button_index

  def exit_program():
      pygame.quit()
      sys.exit()

  #screen.fill((169, 169, 169))
  font = pygame.font.Font(None, 32)

  # Initialize scroll position
  scroll_position = 0

  # Define constants for scroll bar
  if len(students) > 0:
      SCROLLBAR_WIDTH = 10
      SCROLLBAR_COLOR = (100, 100, 100)
      SCROLLBAR_BG_COLOR = (200, 200, 200)

  # Create buttons for each course
  buttons1 = []

  for i, student in enumerate(students):
      button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), student.name, lambda i=i: handle_button_click1(i))
      buttons1.append(button)
  if len(students) > 0:
      back_button1 = Button(100, 200 + len(students) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
      exit_button1 = Button(100, 200 + len(students) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
  else:
      back_button1 = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
      exit_button1 = Button(100, 200 + 1 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)


  # Function to calculate visible courses based on scroll position
  def calculate_visible_students(students, scroll_position):
      visible_students = []
      y = 200
      for i, student in enumerate(students):
          if y >= 200:  # Check if course is within visible area
              visible_students.append((i, student))
          y += 60  # Increase y position for next course
      return visible_students

  # Main loop for handling events and drawing buttons
  while choice1 is None:
      # Calculate visible courses based on scroll position
      visible_students = calculate_visible_students(students, scroll_position)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          # Handle button events
          for button_index, student in visible_students:
              buttons1[button_index].handle_event(event)
          back_button1.handle_event(event)
          exit_button1.handle_event(event)
          # Handle scroll events
          if event.type == pygame.MOUSEBUTTONDOWN and len(students) > 0:
              if event.button == 4:  # Scroll up
                  scroll_position = max(0, scroll_position - 1)
              elif event.button == 5:  # Scroll down
                  scroll_position = min(len(students) - 3, scroll_position + 1)

      # Clear the screen
      screen.blit(image, (0, 0)) 
      # Draw course buttons
      for button_index, student in visible_students:
          buttons1[button_index].rect.y = 200 + (button_index - scroll_position) * 60
          buttons1[button_index].draw()
      if len(students) > 0:
          back_button1.rect.y = 200 + (len(students) - scroll_position) * 60
          exit_button1.rect.y = 200 + (len(students) + 1 - scroll_position) * 60
          back_button1.draw()
          exit_button1.draw()
      else:
          back_button1.rect.y = 200 + (1 - scroll_position) * 60
          exit_button1.rect.y = 200 + (1 + 1 - scroll_position) * 60
          back_button1.draw()
          exit_button1.draw()

      # Draw scrollbar background
      if len(students) > 0:
          pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

      # Calculate scrollbar height and position
      if len(students) > 0:
          scrollbar_height = min(300, 300 * 300 / len(students))  # 300 is the height of the visible area
          scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(students))
      else:
          scrollbar_height = min(300, 300 * 300 / 2)  # 300 is the height of the visible area
          scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (2 - 3)

      # Draw scrollbar
      if len(students) > 0:
          pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))
      if len(students) == 0:
          student_action_text = font.render("There aren't any students", True, (0, 0, 0))
          screen.blit(student_action_text, (200, 200))

      # Update the display
      #print(choice1)
      #print(choice2)
      pygame.display.flip()

      if choice1 == -1:
          #print('hi')
          return -1, -1

      elif choice1 != -1 and choice1 != None:
          scroll_position = 0

          student_course_list = students[choice1].courses
          # Define constants for scroll bar
          if len(student_course_list) > 0:
              SCROLLBAR_WIDTH = 10
              SCROLLBAR_COLOR = (100, 100, 100)
              SCROLLBAR_BG_COLOR = (200, 200, 200)

          # Create buttons for each course
          buttons2 = []

          for i, course in enumerate(student_course_list):
              button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), course.name, lambda i=i: handle_button_click2(i))
              buttons2.append(button)
          if len(student_course_list) > 0:
              back_button2 = Button(100, 200 + len(student_course_list) * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click2(-2))
              exit_button2 = Button(100, 200 + len(student_course_list) * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
          else:
              back_button2 = Button(100, 200 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click2(-2))
              exit_button2 = Button(100, 200 + 1 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)

          # Main loop for handling events and drawing buttons
          while choice1 != -1:
              # Calculate visible courses based on scroll position
              visible_courses = calculate_visible_students(student_course_list, scroll_position)

              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()
                  # Handle button events
                  for button_index, course in visible_courses:
                      buttons2[button_index].handle_event(event)
                  back_button2.handle_event(event)
                  exit_button2.handle_event(event)
                  # Handle scroll events
                  if event.type == pygame.MOUSEBUTTONDOWN and len(student_course_list) > 0:
                      if event.button == 4:  # Scroll up
                          scroll_position = max(0, scroll_position - 1)
                      elif event.button == 5:  # Scroll down
                          scroll_position = min(len(student_course_list) - 3, scroll_position + 1)

              # Clear the screen
              screen.blit(image, (0, 0)) 
              # Draw course buttons
              for button_index, course in visible_courses:
                  buttons2[button_index].rect.y = 200 + (button_index - scroll_position) * 60
                  buttons2[button_index].draw()
              if len(student_course_list) > 0:
                  back_button2.rect.y = 200 + (len(student_course_list) - scroll_position) * 60
                  exit_button2.rect.y = 200 + (len(student_course_list) + 1 - scroll_position) * 60
                  back_button2.draw()
                  exit_button2.draw()
              else:
                  back_button2.rect.y = 200 + (1 - scroll_position) * 60
                  exit_button2.rect.y = 200 + (1 + 1 - scroll_position) * 60
                  back_button2.draw()
                  exit_button2.draw()

              # Draw scrollbar background
              if len(student_course_list) > 0:
                  pygame.draw.rect(screen, SCROLLBAR_BG_COLOR, (780, 200, SCROLLBAR_WIDTH, 300))

              # Calculate scrollbar height and position
              if len(student_course_list) > 0:
                  scrollbar_height = min(300, 300 * 300 / len(student_course_list))  # 300 is the height of the visible area
                  scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (len(student_course_list))
              else:
                  scrollbar_height = min(300, 300 * 300 / 2)  # 300 is the height of the visible area
                  scrollbar_position = 200 + scroll_position * (300 - scrollbar_height) / (2 - 3)

              # Draw scrollbar
              if len(student_course_list) > 0:
                  pygame.draw.rect(screen, SCROLLBAR_COLOR, (780, scrollbar_position, SCROLLBAR_WIDTH, scrollbar_height))
              if len(student_course_list) == 0:
                  course_action_text = font.render("There aren't any classes", True, (0, 0, 0))
                  screen.blit(course_action_text, (200, 200))


              # Update the display
              pygame.display.flip()

              if choice2 == -2:
                  choice1 = None
                  choice2 = None
                  scroll_position = 0
                  break

              elif choice2 != None and choice2 >= 0:
                  return choice1, choice2


def handle_input1_course_admin(event):
    global input_box_name, color_name, color_active, color_inactive, course_name, active1, confirmed1, temp1
    #nonlocal input_box_name, color_name, color_active, color_inactive
    if event.type == pygame.MOUSEBUTTONDOWN:
        # If the user clicks on the input box, toggle active
        if input_box_name.collidepoint(event.pos):
            active1 = input_box_name
            color_name = color_active
        else:
            color_name = color_inactive
            active1 = None
    if event.type == pygame.KEYDOWN:
        if active1:
            if event.key == pygame.K_RETURN:
                # Perform action here (e.g., login)
                temp1 = course_name
                confirmed1 = True
                course_name = ""
                # Clear the input fields after login
            elif event.key == pygame.K_BACKSPACE:
                if active1 == input_box_name:
                    course_name = course_name[:-1]
            else:
                if active1 == input_box_name:
                    course_name += event.unicode

def handle_input2_course_admin(event):
  global input_box_name, color_name, color_active, color_inactive, capacity, active2, check_int, confirmed2, temp2

  #nonlocal input_box_name, color_name, color_active, color_inactive
  if event.type == pygame.MOUSEBUTTONDOWN:

      # If the user clicks on the input box, toggle active
      if input_box_name.collidepoint(event.pos):
          active2 = input_box_name
          color_name = color_active
      else:
          color_name = color_inactive
          active2 = None
  if event.type == pygame.KEYDOWN:
      if active2:
          if event.key == pygame.K_RETURN:
              # Perform action here (e.g., login)
              temp2 = capacity
              if not temp2.isdigit() or int(temp2) < 1:
                  check_int = True
                  capacity = ""
                  return
              check_int = False
              confirmed2 = True
              capacity = ""
              # Clear the input fields after login
          elif event.key == pygame.K_BACKSPACE:
              if active2 == input_box_name:
                  capacity = capacity[:-1]
          else:
              if active2 == input_box_name:
                  capacity += event.unicode

def handle_input3_course_admin(event):
  global input_box_name, color_name, color_active, color_inactive, course_id, active3, confirmed3, temp3
  #nonlocal input_box_name, color_name, color_active, color_inactive
  if event.type == pygame.MOUSEBUTTONDOWN:

      # If the user clicks on the input box, toggle active
      if input_box_name.collidepoint(event.pos):
          active3 = input_box_name
          color_name = color_active
      else:
          color_name = color_inactive
          active3 = None
  if event.type == pygame.KEYDOWN:
      if active3:
          if event.key == pygame.K_RETURN:
              # Perform action here (e.g., login)
              temp3 = course_id
              confirmed3 = True
              course_id = ""
              # Clear the input fields after login
          elif event.key == pygame.K_BACKSPACE:
              if active3 == input_box_name:
                  course_id = course_id[:-1]
          else:
              if active3 == input_box_name:
                  course_id += event.unicode


def create_course_admin(criteria_list):
    global course_name, capacity, course_id, check_int, color_name, color_active, color_inactive, confirmed1, \
        confirmed2, confirmed3, confirmed4, temp1, temp2, temp3
    choice1 = None
    choice2 = None
    choice3 = None
    choice4 = None
    looping = True


    def handle_button_click1(button_index):
        nonlocal choice1
        choice1 = button_index

    def handle_button_click2(button_index):
        nonlocal choice2
        choice2 = button_index

    def handle_button_click3(button_index):
        nonlocal choice3
        choice3 = button_index

    def handle_button_click4(button_index):
        global confirmed4
        nonlocal choice4
        confirmed4 = True
        choice4 = button_index

    def exit_program():
        pygame.quit()
        sys.exit()

    font = pygame.font.Font(None, 32)



    while choice1 is None:
        check_int = False
        back_button = Button(100, 300 + 1 * 60, 600, 50, (255, 255, 0), "Back", lambda: handle_button_click1(-1))
        exit_button = Button(100, 300 + 2 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
        confirmed1 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle input events
            #x = False
            handle_input1_course_admin(event)
            # Handle button events
            exit_button.handle_event(event)
            back_button.handle_event(event)

        screen.blit(image, (0, 0)) 
        font = pygame.font.Font(None, 32)
        new_student_name = font.render("Course Name", True, (0, 0, 0))
        screen.blit(new_student_name, (298, 225))
        pygame.draw.rect(screen, color_name, input_box_name, 2)

        back_button.draw()
        exit_button.draw()
        text_surface_name = font.render(course_name, True, (0, 0, 0))

        screen.blit(text_surface_name, (302, 255))

        pygame.display.flip()
        if confirmed1 == True:
            choice1 = 1

        if choice1 == -1:
            return -1, -1, -1, -1

        pygame.time.delay(10)




        if choice1 is not None:
            color_name = color_inactive
            choice2 = None
            while choice2 is None:
                confirmed2 = False
                back_button = Button(100, 300 + 1 * 60, 600, 50, (255, 255, 0), "Back",
                                     lambda: handle_button_click2(-1))
                exit_button = Button(100, 300 + 2 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # Handle input events
                    handle_input2_course_admin(event)
                    # Handle button events
                    exit_button.handle_event(event)
                    back_button.handle_event(event)

                screen.blit(image, (0, 0)) 
                if check_int == True:
                    error_message = font.render("Please enter a valid integer", True, (255, 0, 0))
                    screen.blit(error_message, (250, 150))
                font = pygame.font.Font(None, 32)
                new_student_name = font.render("Capacity Of Course", True, (0, 0, 0))
                screen.blit(new_student_name, (298, 225))
                pygame.draw.rect(screen, color_name, input_box_name, 2)

                back_button.draw()
                exit_button.draw()
                text_surface_name = font.render(capacity, True, (0, 0, 0))

                screen.blit(text_surface_name, (302, 255))

                pygame.display.flip()
                if confirmed2 == True:
                    choice2 = 1

                if choice2 == -1:
                    choice1 = None
                    break

                if choice2 is not None:
                    color_name = color_inactive
                    choice3 = None
                    while choice3 is None:
                        confirmed3 = False
                        back_button = Button(100, 300 + 1 * 60, 600, 50, (255, 255, 0), "Back",
                                             lambda: handle_button_click3(-1))
                        exit_button = Button(100, 300 + 2 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            # Handle input events
                            handle_input3_course_admin(event)
                            # Handle button events
                            exit_button.handle_event(event)
                            back_button.handle_event(event)

                        screen.blit(image, (0, 0)) 

                        font = pygame.font.Font(None, 32)
                        new_student_name = font.render("ID Of Course", True, (0, 0, 0))
                        screen.blit(new_student_name, (298, 225))
                        pygame.draw.rect(screen, color_name, input_box_name, 2)

                        back_button.draw()
                        exit_button.draw()
                        text_surface_name = font.render(course_id, True, (0, 0, 0))

                        screen.blit(text_surface_name, (302, 255))

                        if confirmed3 == True:
                            choice3 = 1

                        if choice3 == -1:
                            choice2 = None
                            break

                        pygame.display.flip()



                        if choice3 is not None:
                            color_name = color_inactive
                            choice4 = None
                            buttons = []
                            for i, criteria in enumerate(criteria_list):
                                button = Button(100, 200 + i * 60, 600, 50, (0, 128, 0), criteria.name,
                                                lambda i=i: handle_button_click4(i))
                                buttons.append(button)
                            back_button = Button(100, 300 + 1 * 60, 600, 50, (255, 255, 0), "Back",
                                                 lambda: handle_button_click4(-1))
                            exit_button = Button(100, 300 + 2 * 60, 600, 50, (255, 0, 0), "Exit", exit_program)
                            while choice4 is None:
                                confirmed4 = False
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    # Handle button events
                                    for button in buttons:
                                        button.handle_event(event)
                                    back_button.handle_event(event)
                                    exit_button.handle_event(event)


                                screen.blit(image, (0, 0)) 
                                # Draw course buttons
                                for button in range(len(buttons)):
                                    buttons[button].rect.y = 200 + (button) * 60
                                    buttons[button].draw()
                                back_button.draw()
                                exit_button.draw()
                                criteria_title = font.render("Choose A Criteria", True, (0, 0, 0))
                                screen.blit(criteria_title, (300, 125))
                                # Update the display
                                pygame.display.flip()


                                if choice4 == -1:
                                    choice3 = None
                                    confirmed4 = False
                                    break


                                elif confirmed1 == True and confirmed2 == True and confirmed3 == True and confirmed4 == True:
                                    return temp1, temp2, temp3, choice4

class Button():
    def __init__(self, x, y, width, height, color, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.text:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()



# Main function
def main():

    over = False
    user_type = None
    authenticationSystem = interface.AuthenticationSystem()
    # Variables for email and password input
    email = ""
    password = ""
    input_box_email = pygame.Rect(150, 200, 500, 32)
    input_box_password = pygame.Rect(150, 250, 500, 32)
    input_box_name = pygame.Rect(300, 300, 200, 32)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('white')
    color_email = color_inactive
    color_password = color_inactive
    color_name = color_inactive
    active = None


    # Function to handle input events
    def handle_input_events(event):
        nonlocal email, password, color_email, color_password, active
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicks on the input box, toggle active
            if input_box_email.collidepoint(event.pos):
                active = input_box_email
                color_email = color_active
                color_password = color_inactive
            elif input_box_password.collidepoint(event.pos):
                active = input_box_password
                color_password = color_active
                color_email = color_inactive
            elif input_box_name.collidepoint(event.pos):
                active = input_box_name
                color_name = color_active
            else:
                active = None
                color_email = color_inactive
                color_password = color_inactive
        if event.type == pygame.KEYDOWN:
            #print(active)
            if active:
                if event.key == pygame.K_RETURN:
                    # Perform action here (e.g., login)
                    if user_type == "student":
                        student_login(email, password)
                    elif user_type == "admin":
                        admin_login(email, password)
                    # Clear the input fields after login
                    email = ""
                    password = ""
                    active = None
                    color_email = color_inactive
                    color_password = color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    if active == input_box_email:
                        email = email[:-1]
                    elif active == input_box_password:
                        password = password[:-1]
                else:
                    if active == input_box_email:
                        email += event.unicode
                    elif active == input_box_password:
                        password += event.unicode

    # Function to handle student login
    def student_login(email, password):
        global failed
        nonlocal user_type, color_email, color_password, active
        user_type = None
        #print(failed)
        failed = False
        usertype = 1
        loggingIn = True
        while loggingIn:
            user = authenticationSystem.login(email, password, usertype)
            if user is None:
                # Reset email and password fields
                failed = True
                #print(failed)
                email = ""
                password = ""
                active = None
                color_email = color_inactive
                color_password = color_inactive
                # Return to the main menu
                user_type = None
                return failed
            else:
                loggingIn = False
                loggedIn = True
                #user.notify("You have been notified")

                while loggedIn:
                    logged_in = True
                    user_type = "student"
                    for course in authenticationSystem.courses:
                        if len(course.waitlist) > 0:
                            for i in range(len(course.waitlist)):
                                if len(course.students) != course.capacity:
                                    students = authenticationSystem.students
                                    course.students.append(course.waitlist[i])
                                    course.waitlist[i].courses.append(course)
                                    course.waitlist[i].notify(f"Added to  {course.name} from waitlist!")
                                    course.waitlist[i].read_notify(f"Waitlist update!", f"You have been added to {course.name} from the waitlist!", students)
                                    course.remove_wait(course.waitlist[i])

                    action = display_student_actions(user)
                    if action == 1:
                        student_course_list = user.courses
                        selected_course_index = display_student_courses(student_course_list)

                    elif action == 2:
                        course_list = authenticationSystem.get_course_list()
                        selected_course_index = display_course_selection(user, course_list)
                        if selected_course_index != -1:
                            user.notify(f"You added {course_list[selected_course_index].name} to your schedule!")
                            user.add_course(course_list[selected_course_index])
                        #user.add_course(authenticationSystem.get_course_list()[1])
                    elif action == 3:
                        #user.remove_course(c0)
                        student_course_list = user.courses
                        selected_course_index = display_student_courses_remove(student_course_list)
                        if selected_course_index != -1:
                            user.notify(f"You removed {student_course_list[selected_course_index].name} from your schedule!")
                            user.remove_course(student_course_list[selected_course_index])
                    elif action == 4:
                        selected_course_index = display_notifications(user)
                        if selected_course_index == -1:
                            user.clear_notify()
                    elif action == 0:
                        loggedIn = False

    # Function to handle admin login
    def admin_login(email, password):
        global failed
        nonlocal user_type, color_email, color_password, active
        user_type = None
        usertype = 2
        loggingIn = True
        while loggingIn:
            user = authenticationSystem.login(email, password, usertype)
            if user is None:
                # Reset email and password fields
                failed = True
                email = ""
                password = ""
                active = None
                color_email = color_inactive
                color_password = color_inactive
                # Return to the main menu
                user_type = None
                return
            else:
                loggingIn = False
                loggedIn = True
                user_type = "admin"

                while loggedIn:
                    action = display_admin_actions(user)
                    if action == 1:
                        students = authenticationSystem.get_student_list()
                        selected_student_index = change_student_name_admin(user, students)

                    elif action == 2:
                        students = authenticationSystem.get_student_list()
                        course_list = authenticationSystem.get_course_list()
                        student, course = add_course_student_admin(user, students, course_list)
                        if student != -1 and course != -1:
                            students[student].notify(f"{user}, an admin, has added {course_list[course].name} to your schedule!")
                            user.add_course_to_student(students[student], course_list[course])

                    elif action == 3:
                        students = authenticationSystem.get_student_list()
                        student, course = remove_course_student_admin(user, students)
                        if student != -1 and course != -1:
                            students[student].notify(f"{user} removed you from {students[student].courses[course].name}!")
                            user.remove_course_from_student(students[student], students[student].courses[course])

                    elif action == 4:
                        criteria_list = authenticationSystem.criteria
                        name, capacity, id, criteria = create_course_admin(criteria_list)
                        if name != -1 and capacity != -1 and id != -1 and criteria != -1:
                            criteria = criteria_list[criteria]
                            course = user.create_course(name, int(capacity), id, criteria)
                            authenticationSystem.courses.append(course)
                            students = authenticationSystem.students
                            for student in students.items():
                                student[1][1].read_notify(f"A new course has been created", f"{user} created a new course!", students)
                    elif action == 0:
                        loggedIn = False

    #Create buttons
    student_button = Button(100, 200, 200, 50, (0, 128, 0), "Student", lambda: set_user_type("student"))
    admin_button = Button(500, 200, 200, 50, (0, 0, 255), "Admin", lambda: set_user_type("admin"))
    exit_button = Button(300, 400, 200, 50, (255, 0, 0), "Exit", lambda: set_over())
    main_button = Button(300, 313, 200, 50, (0, 0, 255), "Main menu", lambda: set_user_type_main(None))


    # Function to set user type
    def set_user_type(user_type_selected):
        nonlocal user_type, email, password
        user_type = user_type_selected
        email = ""  # Reset email
        password = ""  # Reset password
        failed = False

    def set_user_type_main(user_type_selected):
        nonlocal user_type, email, password
        global failed
        user_type = user_type_selected
        email = ""  # Reset email
        password = ""  # Reset password
        failed = False

    # Function to set 'over' flag to True
    def set_over():
        nonlocal over
        over = True

    # Main loop
    while not over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            # Handle input events
            handle_input_events(event)
            # Handle button events
            if not user_type:
                student_button.handle_event(event)
                admin_button.handle_event(event)
            exit_button.handle_event(event)
            main_button.handle_event(event)

        #BACKGROUND
        screen.blit(image, (0, 0)) 


        # Draw buttons if user type not selected
        if not user_type:

            student_button.draw()
            admin_button.draw()

            if failed == True:
                incorrect_login = font.render("Incorrect login", True, (255, 0, 0))
                screen.blit(incorrect_login, (325, 50))

        # Draw email and password input fields if a user type is selected
        if user_type and not logged_in:
            pygame.draw.rect(screen, color_email, input_box_email, 2)
            pygame.draw.rect(screen, color_password, input_box_password, 2)
            font = pygame.font.Font(None, 32)
            text_surface_email = font.render("Email:", True, (0, 0, 0))
            text_surface_password = font.render("Password:", True, (0, 0, 0))
            screen.blit(text_surface_email, (50, 200))
            screen.blit(text_surface_password, (30, 250))
            font = pygame.font.Font(None, 32)
            text_surface_email = font.render(email, True, (0, 0, 0))
            text_surface_password = font.render("*" * len(password), True, (0, 0, 0))
            screen.blit(text_surface_email, (150, 200))
            screen.blit(text_surface_password, (150, 250))
            main_button.draw()
       
        

        # Draw exit button
        exit_button.draw()

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()

    # email_password needs to be changed if program is used outside this program
    # email_password is used here and in the student file
    '''email_sender = "csulbnotifications@gmail.com"
    email_password = os.environ['EMAIL_PASSWORD']
    subject = "Thank you for listening to our presentation!"
    body = "Please give us an A (づ｡◕‿‿◕｡)づ"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = "patrick.mcgrath01@student.csulb.edu"
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, "patrick.mcgrath01@student.csulb.edu", em.as_string())'''
