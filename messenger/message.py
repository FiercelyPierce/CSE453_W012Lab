########################################################################
# COMPONENT:
#    MESSAGE
# Author:
#    Br. Helfrich, Kyle Mueller, Jerry Lane
# Summary: 
#    This class stores the notion of a message
########################################################################

##################################################
# MESSAGE CLASS
# One message to be displayed to the user or not
##################################################
class Message:

    # Static variable for the next id
    _id_next = 100

    ##################################################
    # MESSAGE DEFAULT CONSTRUCTOR
    # Set a message to empty
    ##################################################
    def __init__(self):
        self._empty = True
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._id = Message._id_next
        Message._id_next += 1

    ##################################################
    # MESSAGE NON-DEFAULT CONSTRUCTOR
    # Create a message and fill it
    ##################################################   
    def __init__(self, text, author, date, access):
        self._text = text
        self._author = author
        self._date = date
        self._access = access
        self._id = Message._id_next
        Message._id_next += 1
        self._empty = False

    ##################################################
    # MESSAGE :: GET ID
    # Determine the unique ID of this message
    ##################################################   
    def get_id(self):
        return self._id

    ##################################################
    # MESSAGE :: DISPLAY PROPERTIES
    # Display the attributes/properties but not the
    # content of this message
    ##################################################  
    def display_properties(self, access):
        if self._empty:
            return
        if access.can_read([self._id, self._author, self._date, self._access]):
            print(f"\t[{self._id}] Message from {self._author} at {self._date}")

    ##################################################
    # MESSAGE :: DISPLAY TEXT
    # Display the contents or the text of the message
    ################################################## 
    def display_text(self, access):
        if access.can_read([self._id, self._author, self._date, self._access]):
            print(f"\tMessage: {self._text}")
        else:
            print(f"\tUnknown Message")

    ##################################################
    # MESSAGE :: UPDATE TEXT
    # Update the contents or text of the message
    ################################################## 
    def update_text(self, new_text):
        self._text = new_text

    ##################################################
    # MESSAGE :: CLEAR
    # Delete the contents of a message and mark it as 
    # empty
    ################################################## 
    def clear(self):
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._empty = True

    ##################################################
    # MESSAGE :: GET MESSAGE
    # Return the content of a message as a list
    ################################################## 
    def get_message(self):
        return [self._id, self._author, self._date, self._access]