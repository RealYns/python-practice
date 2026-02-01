import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('someone', 'something', 50000)

    def test_give_default_raise(self):

        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)


    def test_give_raise(self):

        self.employee.give_raise(6000)
        self.assertEqual(self.employee.salary, 56000)

if __name__ == '__main__':
    unittest.main()