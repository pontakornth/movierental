from enum import Enum


class PriceCode(Enum):
    regular = {
        "base": 2.0,
        "base_days": 2,
        "day_price": 1.5
    }

    children = {
        "base": 1.5,
        "base_days": 3,
        "day_price": 1.5
    }

    new_release = {
        "base": 0,
        "base_days": 0,
        "day_price": 3
    }

    def price(self, days: int):
        """Get price base on days rented."""
        price_code = self.value
        if days < price_code["base_days"]:
            return price_code["base"]
        price = price_code["base"] + price_code["day_price"] * (days - price_code["base_days"])
        return price


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
