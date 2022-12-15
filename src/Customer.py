from src.Rentals import Rentals
from src.StatementService import StatementService


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = Rentals()

    def add_rental(self, arg):
        self.__rentals.append(arg)

    def get_name(self):
        return self.__name

    def text_statement(self):
        return StatementService.generate_text_statement(self.__name, self.__rentals)

    def html_statement(self):
        return StatementService.generate_html_statement(self.__name, self.__rentals)


