from .Movie import Movie


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    def add_rental(self, arg):
        self.__rentals.append(arg)

    def get_name(self):
        return self.__name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for each in self.__rentals:
            this_amount = 0
            price_code = each.get_movie().get_price_code()

            if price_code == Movie.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += (each.get_days_rented() - 2) * 1.5

            elif price_code == Movie.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3

            elif price_code == Movie.CHILDREN:
                this_amount += 1.5
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented() - 3) * 1.5

            frequent_renter_points += 1
            if each.get_movie().get_price_code() == Movie.NEW_RELEASE and each.get_days_rented() > 1:
                frequent_renter_points += 1
            result += "\t" + each.get_movie().get_title() + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result
