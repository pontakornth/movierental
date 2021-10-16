import logging

from movie import PriceCode


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        price_code = self.get_movie().get_price_code()
        return price_code.price(self.get_days_rented())
        # else:
        #     log = logging.getLogger()
        #     log.error(
        #         f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
        # return amount

    def get_rental_points(self):
        price_code = self.get_movie().get_price_code()

        return price_code.get_rental_points(self.get_days_rented())
