import unittest
from name_function import get_formatted_name


class TestNameCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', 'lee')
        self.assertEqual(formatted_name, 'Janis Lee Joplin')


if __name__ == "__main__":
    unittest.main()
