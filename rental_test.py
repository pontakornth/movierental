import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", Movie.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		tests = [
			# (movie, days rented, result)
			(self.new_movie, 1, 3.0),
			(self.new_movie, 5, 15.0),
			(self.regular_movie, 1, 2.0),
			(self.regular_movie, 2, 2.0),
			(self.regular_movie, 3, 3.5),
			(self.childrens_movie, 3, 1.5),
			(self.childrens_movie, 4, 3.0),
		]
		for test in tests:
			with self.subTest():
				movie, days, result = test
				rental = Rental(movie, days)
				self.assertEqual(rental.get_price(), result)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 3)
		self.assertEqual(rental.get_rental_points(), 3)

		rental = Rental(self.regular_movie, 99)
		self.assertEqual(rental.get_rental_points(), 1)

		rental = Rental(self.childrens_movie, 99)
		self.assertEqual(rental.get_rental_points(), 1)
