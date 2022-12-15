from src.Rental import Rental


class Rentals(list[Rental]):
    def total_frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self:
            frequent_renter_points += rental.calculate_frequent_renter_points()
        return frequent_renter_points

    def total_amount(self):
        total_amount = 0
        for rental in self:
            total_amount += rental.calculate_amount()
        return total_amount
