from src.MovieType import *


class Movie:
    REGULAR = Regular()
    NEW_RELEASE = New_Release()
    CHILDREN = Children()
    BLUE_RAY = Blue_Ray()

    def __init__(self, title, movie_type):
        self.__title = title
        self.__movie_type = movie_type

    def get_movie_type(self):
        return self.__movie_type

    def get_title(self):
        return self.__title
