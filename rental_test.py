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

	@unittest.skip("TODO add test of frequent renter points when you add it to Rental")
	def test_rental_points(self):
		self.fail("TODO add  test of frequent renter points")