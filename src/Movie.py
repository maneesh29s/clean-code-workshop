class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2
    BLUE_RAY = 3

    def __init__(self, title, price_code):
        self.__title = title
        self.__priceCode = price_code

    def get_price_code(self):
        return self.__priceCode

    def set_price_code(self, arg):
        self.__priceCode = arg

    def get_title(self):
        return self.__title