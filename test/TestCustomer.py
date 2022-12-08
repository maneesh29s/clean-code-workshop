import unittest
from src.Customer import Customer


class TestGetAreaRectangle(unittest.TestCase):
    @staticmethod
    def runTest():
        customer = Customer("Random Name")
        assert True


if __name__ == '__main__':
    unittest.main()
