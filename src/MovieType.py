class MovieType:
    def amount(self, days_rented):
        pass

    def frequent_renter_points(self, days_rented):
        pass


class Regular(MovieType):
    def amount(self, days_rented):
        amount = 2
        if days_rented > 2:
            amount += (days_rented - 2) * 1.5
        return amount

    def frequent_renter_points(self, days_rented):
        return 1


class New_Release(MovieType):
    def amount(self, days_rented):
        return days_rented * 3

    def frequent_renter_points(self, days_rented):
        if days_rented > 1:
            return 2
        return 1


class Children(MovieType):
    def amount(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += (days_rented - 3) * 1.5
        return amount

    def frequent_renter_points(self, days_rented):
        return 1


class Blue_Ray(MovieType):
    def amount(self, days_rented):
        return days_rented * 4

    def frequent_renter_points(self, days_rented):
        return 3
