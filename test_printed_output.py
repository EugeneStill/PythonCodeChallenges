import unittest
from unittest.mock import patch
from io import StringIO

class Printer:
    def print_value(self):
        print("Hello, World!")

class TestPrinter(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_value(self, mock_stdout):
        printer = Printer()
        printer.print_value()
        printed_output = mock_stdout.getvalue().strip()
        self.assertEqual(printed_output, "Hello, World!")

# Test execution
if __name__ == "__main__":
    unittest.main()







