import unittest
from rental import Rental, PriceCode
from movie import Movie
from datetime import datetime


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		current_year = datetime.now().year
		self.new_movie = Movie("Mulan", current_year, [])
		self.regular_movie = Movie("CitizenFour", current_year - 2, [])
		self.children_movie = Movie("Frozen", current_year - 2, ["Children"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		current_year = datetime.now().year
		m = Movie("CitizenFour", current_year - 2, [])
		self.assertEqual("CitizenFour", m.get_title())

	def test_rental_price(self):
		tests = [
			# (movie, days rented, result)
			(self.new_movie, 1, 3.0),
			(self.new_movie, 5, 15.0),
			(self.regular_movie, 1, 2.0),
			(self.regular_movie, 2, 2.0),
			(self.regular_movie, 3, 3.5),
			(self.children_movie, 3, 1.5),
			(self.children_movie, 4, 3.0),
		]
		for movie, days, result in tests:
			with self.subTest(msg=f"Test {movie} rented {days}, expect price of {result}"):
				rental = Rental(movie, days)
				self.assertEqual(rental.get_price(), result)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 3)
		self.assertEqual(rental.get_rental_points(), 3)

		rental = Rental(self.regular_movie, 99)
		self.assertEqual(rental.get_rental_points(), 1)

		rental = Rental(self.children_movie, 99)
		self.assertEqual(rental.get_rental_points(), 1)
