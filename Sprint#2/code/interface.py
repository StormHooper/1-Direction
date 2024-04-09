from typing import Optional


class Interface:
    @staticmethod
    def display_login_options() -> str:
        """Displays login options for the user to select."""
        print("Login as:")
        print("1. Student")
        print("2. Admin")
        choice = input("Enter your choice (1 or 2): ")
        return choice.strip()

    @staticmethod
    def get_email() -> str:
        """Gets user's email."""
        return input("Enter your email: ").strip()

    @staticmethod
    def get_password() -> str:
        """Gets user's password."""
        return input("Enter your password: ").strip()

class AuthenticationSystem:
    @staticmethod
    def authenticate(role: str, email: str, password: str) -> Optional[str]:
        """Authenticates the user based on their role, email, and password."""
        # Here you would implement the logic to authenticate users
        # For example, check if the email and password match records for the given role
        # For simplicity, let's assume some predefined email and password combinations

        if role.lower() == "student":
            if email == "student@example.com" and password == "studentpassword":
                return "student"
        elif role.lower() == "admin":
            if email == "admin@example.com" and password == "adminpassword":
                return "admin"
        return None

# Main program
def main():
    while True:
        choice = Interface.display_login_options()
        if choice == "1":
            role = "student"
        elif choice == "2":
            role = "admin"
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        email = Interface.get_email()
        password = Interface.get_password()

        user_role = AuthenticationSystem.authenticate(role, email, password)
        if user_role:
            print(f"Welcome, {user_role.capitalize()}!")
            break
        else:
            print("Invalid email or password. Please try again.")

if __name__ == "__main__":
    main()

# class Interface:
#   
#   def __init__(self, username, password) -> None:
#     """
#     Connect the interface to the database. (TO BE IMPLEMENTED IN SPRINT#2)
#
#     Args:
#       username (str): The username of the user.
#       passsword (str): The password of the user.
#     """
#     self._username = username
#     self._password = password
#
#   def login(self, username: str, password: str):
#     '''
#     Login for student or admin, username and passoword must be entered. 
#     (TO BE IMPLEMENTED IN SPRINT#2)
#     
#     Args:
#       username (str): Enter the username.
#     '''
#     print("=" * 20 + "\nPlease sign in\n1. Students\n2. Admin\n" + "=" * 20)
#     #self.option = input("Select an option: ")
#     #self.username = input("Username: ")
#     #self.password = input("Password: ")