from src.Rentals import Rentals


class StatementService:

    @staticmethod
    def generate_text_statement(name, rentals: Rentals):
        statement = "Rental Record for " + name + "\n"
        for rental in rentals:
            statement += "\t" + rental.get_movie().get_title() + "\t" + str(rental.calculate_amount()) + "\n"
        statement += "Amount owed is " + str(rentals.total_amount()) + "\n"
        statement += "You earned " + str(rentals.total_frequent_renter_points()) + " frequent renter points"
        return statement

    @staticmethod
    def generate_html_statement(name, rentals: Rentals):
        statement = "<h1>Rental Record for " + name + "</h1><br><p>"
        for rental in rentals:
            statement += rental.get_movie().get_title() + "\t" + str(rental.calculate_amount()) + "<br>"
        statement += "Amount owed is " + str(rentals.total_amount()) + "<br>"
        statement += "You earned " + str(rentals.total_frequent_renter_points()) + " frequent renter points</p>"
        return statement
