from enum import Enum


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


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).

    def __init__(self, title, price_code: PriceCode):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
