import logging
from datetime import datetime
from enum import Enum
from movie import Movie


def create_linear_price_formula(base_days, base_price, price_per_day):
    """Create a calculation function based on base days and price."""

    def linear_formula(days_rented):
        """Linear formula of price"""
        if days_rented < base_days:
            return base_price
        return base_price + price_per_day * (days_rented - base_days)

    return linear_formula


class PriceCode(Enum):
    regular = {
        "price": create_linear_price_formula(2, 2.0, 1.5),
        "rental_points": lambda days: 1,
    }

    children = {
        "price": create_linear_price_formula(3, 1.5, 1.5),
        "rental_points": lambda days: 1,
    }

    new_release = {
        "price": create_linear_price_formula(0, 0, 3),
        "rental_points": lambda days: days,
    }

    def price(self, days: int):
        """Get price base on days rented."""
        price_code = self.value
        return price_code["price"](days)

    def get_rental_points(self, days: int):
        """Get rental points base on days."""
        return self.value["rental_points"](days)

    @staticmethod
    def for_movie(movie: Movie):
        """Generate price code from movie.

        If the movie is from the same year, it is a new release movie.
        If it has Children genre, it is a children movie.
        Otherwise, it is normal (regular) movie.
        """
        present_year = datetime.now().year
        if movie.get_year() == present_year:
            return PriceCode.new_release
        elif "Children" in movie.get_genres():
            return PriceCode.children
        return PriceCode.regular


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

    def __init__(self, movie, days_rented, price_code: PriceCode):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price_code(self):
        return self.price_code

    def get_price(self):
        price_code = self.get_price_code()
        return price_code.price(self.get_days_rented())
        # else:
        #     log = logging.getLogger()
        #     log.error(
        #         f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
        # return amount

    def get_rental_points(self):
        price_code = self.get_price_code()

        return price_code.get_rental_points(self.get_days_rented())
