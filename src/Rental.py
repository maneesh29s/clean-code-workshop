from src.Movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented):
        self.__movie = movie
        self.__daysRented = days_rented

    def get_days_rented(self):
        return self.__daysRented

    def get_movie(self):
        return self.__movie

    def calculate_amount(self):
        return self.__movie.get_movie_type().amount(self.__daysRented)

    def calculate_frequent_renter_points(self):
        return self.__movie.get_movie_type().frequent_renter_points(self.__daysRented)
