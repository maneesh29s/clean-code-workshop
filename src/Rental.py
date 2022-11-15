class Rental:
    def __init__(self, movie, daysRented):
        self.__movie = movie
        self.__daysRented = daysRented

    def getDaysRented(self):
        return self.__daysRented

    def getMovie(self):
        return self.__movie