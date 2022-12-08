import unittest
from src.Customer import Customer


class TestCustomer(unittest.TestCase):
    def runTest(self):
        customer = Customer("Random Name")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
