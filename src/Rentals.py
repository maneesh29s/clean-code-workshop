class Rentals:

    def __init__(self):
        self.__rentals = []

    def add(self, arg):
        self.__rentals.append(arg)

    def get_rentals(self):
        return self.__rentals

    def get_total_frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self.__rentals:
            frequent_renter_points += rental.calculate_frequent_renter_points()
        return frequent_renter_points

    def get_total_amount(self):
        total_amount = 0
        for rental in self.__rentals:
            total_amount += rental.calculate_amount()
        return total_amount
