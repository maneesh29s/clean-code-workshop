from Movie import Movie

class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    def addRental(self, arg):
        self.__rentals.append(arg)

    def getName(self):
        self.__name

    def statement(self):
        totalAmount = 0
        frequentRenterPoints = 0
        result = "Rental Record for " + self.getName() + "\n"
        for each in self.__rentals:
            thisAmount = 0
            match each.getDaysRented().getPriceCode():
                case Movie.REGULAR:
                    thisAmount += 2
                    if each.getDaysRented() > 2:
                        thisAmount += (each.getDaysRented() - 2) * 1.5
                case Movie.NEW_RELEASE:
                    thisAmount += each.getDaysRented() * 3
                case Movie.CHILDREN:
                    thisAmount += 1.5
                    if each.getDaysRented() > 3:
                        thisAmount += (each.getDaysRented() - 3) * 1.5
            
            frequentRenterPoints+=1
            if each.getMovie().getPriceCode() == Movie.NEW_RELEASE and each.getDaysRented() > 1:
                frequentRenterPoints+=1
            result += "\t" + each.getMovie().getTitle() + "\t" + str(thisAmount) + "\n"
            totalAmount += thisAmount

        result += "Amount owed is " + str(totalAmount) + "\n"
        result += "You earned " + str(frequentRenterPoints) + " frequent renter points"
        return result