import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.regular)
		self.children_movie = Movie("Frozen", PriceCode.children)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

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
