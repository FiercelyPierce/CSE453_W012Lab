########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, Jerry Lane
# Summary: 
#    This class allows one user to interact with the system
########################################################################

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password, access):
        self.name = name
        self.password = password
        self.access = access

userlist = [
   [ "AdmiralAbe",     "password", "Secret" ],  
   [ "CaptainCharlie", "password", "Privileged" ], 
   [ "SeamanSam",      "password", "Confidential" ],
   [ "SeamanSue",      "password", "Confidential" ],
   [ "SeamanSly",      "password", "Confidential" ]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, messages):
        self._username = username
        self._p_messages = messages

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self, access):
        id_ = self._prompt_for_id("display")
        if not self._p_messages.show(id_, access):
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self, access):
        print("Messages:")
        self._p_messages.display(access)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self, access):
        clearance = self._prompt_for_line("clearance level for this message")
        if access.can_write( [ "", "", "", clearance] ):
            self._p_messages.add(self._prompt_for_line("message"),
                                self._username,
                                self._prompt_for_line("date"),
                                clearance)
        else:
            print("You cannot write to this clearance level.")

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, access):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_, access):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
        if access.can_read(self._p_messages.get_message(id_)):
            if access.can_write(self._p_messages.get_message(id_)):
                self._p_messages.update(id_, self._prompt_for_line("message"))
                print()
            else:
                print(f"\tThis message cannot be updated by you.\n")
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self, access):
        id = self._prompt_for_id("delete")
        if access.can_read(self._p_messages.get_message(id)):
            self._p_messages.remove(id)
        else:
            print(f"Unknown Messaget\n")

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")