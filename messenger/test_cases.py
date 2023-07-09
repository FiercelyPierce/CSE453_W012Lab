########################################################################
# COMPONENT:
#    test_cases
# Author:
#    Bryer Johnson
# Summary: 
#    Test cases
########################################################################
from os import path
import unittest
import interact
import messages
import control

class Interact(unittest.TestCase):
    FILE_NAME = path.join(path.dirname(path.abspath(__file__)), "messages.txt")
    messages_ = messages.Messages(FILE_NAME)

    def test_show_existing_message(self):
        interact_ = interact.Interact("CaptainCharlie", self.messages_)
        expected_output = "[1] Message from Winston Churchill at 16 May 1940\n\tMessage: You ask what is our aim? I can answer in one word: Victory!"
        self.assertEqual(interact_.show(control.Control("CaptainCharlie", "password", self.messages_)), expected_output)

    def test_show_nonexistent_message(self):
        interact_ = interact.Interact("SeamanSam", self.messages_)
        expected_output = "ERROR! Message ID '0' does not exist"
        self.assertEqual(interact_.show(control.Control("SeamanSam", "password", self.messages_)), expected_output)

    def test_add_message_with_write_access(self):
        interact_ = interact.Interact("CaptainCharlie", self.messages_)
        interact_.add(control.Control("CaptainCharlie", "password", self.messages_))
        interact_.show(control.Control("CaptainCharlie", "password", self.messages_))
        expected_output = "[5] Message from CaptainCharlie at [date]\n\tMessage: [message]"
        self.assertIn(expected_output, interact_.show(control.Control("CaptainCharlie", "password", self.messages_)))
        
    def can_read_and_can_write(self):
        self.messages_ = messages.Messages("messages.txt")
        
        """ 
        User with Privileged access
        """
        control_privileged = control.Control("CaptainCharlie", "password", self.messages_)
        self.assertTrue(control_privileged.can_read(["1", "Author", "Date", "Public"]))
        self.assertTrue(control_privileged.can_read(["2", "Author", "Date", "Confidential"]))
        self.assertTrue(control_privileged.can_read(["3", "Author", "Date", "Privileged"]))
        self.assertFalse(control_privileged.can_read(["4", "Author", "Date", "Secret"]))

        self.assertTrue(control_privileged.can_write(["1", "Author", "Date", "Public"]))
        self.assertFalse(control_privileged.can_write(["2", "Author", "Date", "Confidential"]))
        self.assertTrue(control_privileged.can_write(["3", "Author", "Date", "Privileged"]))
        self.assertTrue(control_privileged.can_write(["4", "Author", "Date", "Secret"]))

        """
        User with Confidential access
        """
        control_confidential = control.Control("SeamanSam", "password", self.messages_)
        self.assertTrue(control_confidential.can_read(["1", "Author", "Date", "Public"]))
        self.assertTrue(control_confidential.can_read(["2", "Author", "Date", "Confidential"]))
        self.assertFalse(control_confidential.can_read(["3", "Author", "Date", "Privileged"]))
        self.assertFalse(control_confidential.can_read(["4", "Author", "Date", "Secret"]))

        self.assertTrue(control_confidential.can_write(["1", "Author", "Date", "Public"]))
        self.assertTrue(control_confidential.can_write(["2", "Author", "Date", "Confidential"]))
        self.assertFalse(control_confidential.can_write(["3", "Author", "Date", "Privileged"]))
        self.assertFalse(control_confidential.can_write(["4", "Author", "Date", "Secret"]))

        """
        User with Secret access
        """
        control_secret = control.Control("AdmiralAbe", "password", self.messages_)
        self.assertTrue(control_secret.can_read(["1", "Author", "Date", "Public"]))
        self.assertTrue(control_secret.can_read(["2", "Author", "Date", "Confidential"]))
        self.assertTrue(control_secret.can_read(["3", "Author", "Date", "Privileged"]))
        self.assertTrue(control_secret.can_read(["4", "Author", "Date", "Secret"]))

        self.assertTrue(control_secret.can_write(["1", "Author", "Date", "Public"]))
        self.assertTrue(control_secret.can_write(["2", "Author", "Date", "Confidential"]))
        self.assertTrue(control_secret.can_write(["3", "Author", "Date", "Privileged"]))
        self.assertFalse(control_secret.can_write(["4", "Author", "Date", "Secret"]))

        

if __name__ == '__main__':
    unittest.main()