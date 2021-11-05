# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental, PriceCode
from customer import Customer
from datetime import datetime


def make_movies():
    now = datetime.now()
    this_year = now.year
    movies = [
        Movie("The Irishman", this_year, ["Action"]),
        Movie("CitizenFour", this_year - 1, ["Action"]),
        Movie("Frozen", this_year - 1, ["Children"]),
        Movie("El Camino", this_year, ["Action"]),
        Movie("Particle Fever", this_year - 2, ["Fever"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
