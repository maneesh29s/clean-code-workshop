import unittest
from src.Customer import Customer
from src.Movie import Movie
from src.Rental import Rental


class TestCustomer(unittest.TestCase):
    def test_should_generate_statement_when_asked(self):
        customer = Customer("Maneesh")
        customer.add_rental(Rental(Movie("Spiderman", Movie.NEW_RELEASE), 10))
        customer.add_rental(Rental(Movie("Batman", Movie.REGULAR), 15))
        customer.add_rental(Rental(Movie("Barbie", Movie.CHILDREN), 5))

        self.assertEqual(customer.text_statement(), """Rental Record for Maneesh
	Spiderman	30
	Batman	21.5
	Barbie	4.5
Amount owed is 56.0
You earned 4 frequent renter points""")

    def test_should_generate_html_statement_when_asked(self):
        customer = Customer("Maneesh")
        customer.add_rental(Rental(Movie("Spiderman", Movie.NEW_RELEASE), 10))
        customer.add_rental(Rental(Movie("Batman", Movie.REGULAR), 15))
        customer.add_rental(Rental(Movie("Barbie", Movie.CHILDREN), 5))

        self.assertEqual(customer.html_statement(),
                         """<h1>Rental Record for Maneesh</h1><br><p>Spiderman	30<br>Batman	21.5<br>Barbie	4.5<br>Amount owed is 56.0<br>You earned 4 frequent renter points</p>""")


if __name__ == '__main__':
    unittest.main()
