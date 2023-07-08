########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Pierce Cirks, Jerry Lane
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################
import interact

class Control():
    """
    This class represents the control of access to both users and messages.
    """

    def __init__(self, username, password, messages):
        """
        This function is the default constructor for the Control class.
        Parameter: username - text string containing the user's input name
                   password - text string containing the user's input password
                   messages - list containing all message data
        Return:    nothing
        """
        self._username = username
        self._password = password
        self._userlist = interact.userlist
        self._messages = messages
        self._classifications = [ "Public", "Confidential", "Privileged", "Secret" ]
    
    def authenticate(self):
        """
        This function will authenticate the user into the system
        """
        for user in self._userlist:
            if self._username == user[0] and self._password == user[1]:
                return True
        return False
    

    def can_read(self, message):
        """
        This function controls read access according to the Bell-LaPadula model, allowing
        read-down capability from higher classification to lower, but disallowing read-up
        capability, thus providing confidentiality assurance.
        Parameter: message - text string containing message data, including access requirement
        Return:    boolean - allow if user is equal or higher than message classification
        """
        message_access = self._get_message_access(message)
        user_access = self._get_user_access()
        if user_access >= message_access:
            return True
        return False
    

    def can_write(self, message):
        """
        This function controls write access according to the Bell-LaPadula model, allowing
        write-up capability from lower classification to higher, but disallowing write-down
        capability, thus providing confidentiality assurance.
        Parameter: message - text string containing message data, including access requirement
        Return:    boolean - allow if user is equal or lower than message classification
        """
        message_access = self._get_message_access(message)
        user_access = self._get_user_access()
        if user_access <= message_access and message_access >= 0:
            return True
        return False


    def _get_user_access(self):
        """
        This function takes no parameters and returns the numerical access level of the user. 
        Parameter: none
        Return:    integer - numerical access level of the user
        """
        for user in self._userlist:
            if self._username in user:
                access = user[2]
                return self._classifications.index(access)
        return 0

    
    def _get_message_access(self, message):
        """
        This function accepts a list message as a parameter and returns the numerical
        access level of the message.
        Parameter: message - list holding all the message data
        Return:    integer - numerical value of the access level of the message
        """
        access = message[3]
        if access not in self._classifications:
            return -1
        return self._classifications.index(access)