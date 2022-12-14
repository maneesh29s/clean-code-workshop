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
        for rental in self.__rentals:
            rental_amount = rental.calculate_amount()
            total_amount += rental_amount
            frequent_renter_points += rental.calculate_frequent_renter_points()

            result += "\t" + rental.get_movie().get_title() + "\t" + str(rental_amount) + "\n"

        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result
