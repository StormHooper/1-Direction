class Interface:
  
  def __init__(self, username, password) -> None:
    """
    Connect the interface to the database. (TO BE IMPLEMENTED IN SPRINT#2)

    Args:
      username (str): The username of the user.
      passsword (str): The password of the user.
    """
    self._username = username
    self._password = password

  def login(self, username: str, password: str):
    '''
    Login for student or admin, username and passoword must be entered. 
    (TO BE IMPLEMENTED IN SPRINT#2)
    
    Args:
      username (str): Enter the username.
    '''
    print("=" * 20 + "\nPlease sign in\n1. Students\n2. Admin\n" + "=" * 20)
    #self.option = input("Select an option: ")
    #self.username = input("Username: ")
    #self.password = input("Password: ")
    