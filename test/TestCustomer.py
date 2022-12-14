import unittest
from src.Customer import Customer
from src.Movie import Movie
from src.Rental import Rental


class TestCustomer(unittest.TestCase):
    def test_should_generate_statement_when_asked(self):
        customer = Customer("Maneesh")
        customer.add_rental(Rental(Movie("Spiderman",Movie.NEW_RELEASE),10))
        customer.add_rental(Rental(Movie("Batman", Movie.REGULAR), 15))
        customer.add_rental(Rental(Movie("̆Barbie", Movie.CHILDREN), 5))

        self.assertEqual(customer.statement(), """Rental Record for Maneesh
	Spiderman	30
	Batman	21.5
	̆Barbie	4.5
Amount owed is 56.0
You earned 4 frequent renter points""")


if __name__ == '__main__':
    unittest.main()
