class Rental:
    def __init__(self, movie, days_rented):
        self.__movie = movie
        self.__daysRented = days_rented

    def get_days_rented(self):
        return self.__daysRented

    def get_movie(self):
        return self.__movie
