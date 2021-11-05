from typing import List


def create_linear_price_formula(base_days, base_price, price_per_day):
    """Create a calculation function based on base days and price."""

    def linear_formula(days_rented):
        """Linear formula of price"""
        if days_rented < base_days:
            return base_price
        return base_price + price_per_day * (days_rented - base_days)

    return linear_formula


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).

    def __init__(self, title: str, year: int, genres: List[str]):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genres = genres

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genres(self):
        return self.__genres

    def __str__(self):
        return self.__title
