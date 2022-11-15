class Movie:
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, priceCode):
        self.__title = title
        self.__priceCode = priceCode

    def getPriceCode(self):
        return self.__priceCode

    def setPriceCode(self, arg):
        self.__priceCode = arg

    def getTitle(self):
        return self.__title


