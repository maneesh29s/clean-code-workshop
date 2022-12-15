import unittest

from src.Movie import Movie, Blue_Ray
from src.Rental import Rental


class TestRental(unittest.TestCase):
    def test_should_calculate_correct_amount_when_movie_type_is_blue_ray(self):
        rental = Rental(Movie("Batman", Movie.BLUE_RAY), 10)

        self.assertEqual(rental.calculate_amount(), 40)

    def test_should_calculate_correct_frequent_renter_points_when_movie_type_is_blue_ray(self):
        rental = Rental(Movie("Batman", Movie.BLUE_RAY), 10)

        self.assertEqual(rental.calculate_frequent_renter_points(), 3)


if __name__ == '__main__':
    unittest.main()
