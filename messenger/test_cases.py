import unittest
import interact
import messages
import control


class Interact(unittest.TestCase):

    def setUp(self):
        self.messages_ = messages.Messages("messages.txt")

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
        
        

if __name__ == '__main__':
    unittest.main()