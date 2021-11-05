from typing import List, Dict
import csv


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


class MovieCatalog:
    """
    Catalog for creating movies from CSV file.
    """

    def __init__(self, filename="movies.csv"):
        """Create instance of MovieCatalog and load csv. file.

        Args:
            filename (str): Name of CSV file containing data of movies """
        self.__file = open(filename)
        # Dictionary of movies, keyed by name.
        self.__movies = dict()

    def __scan(self, title: str) -> Dict:
        """Find movies by name.

        It will try to search in dictionary first.
        If there is no such movie, it reads from file.
        Args:
            title (str): Movie name to search for
        Returns:
            Dict: Movie data from CSV
        Raises:
            KeyError: When there is no such movie.
        """
        movie_data = self.__movies.get(title)
        if movie_data is None:
            for row in csv.DictReader(self.__file):
                row_title = row["title"]
                self.__movies[row_title] = row
                if title == row_title:
                    return row
            raise KeyError("The movie does not exist in the database.")
        return movie_data

    def get_movie(self, movie_title: str) -> Movie:
        """Read CSV and return movies from it."""
        movie_data = self.__scan(movie_title)
        genre_list = movie_data["genres"].split("|")
        year = int(movie_data["year"])
        movie = Movie(movie_data["title"], year, genre_list)
        return movie
