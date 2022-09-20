import re
import requests
from bs4 import BeautifulSoup

# k_sqohloz7 - imdb key
class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file
        self.moviepage_url = 'https://www.imdb.com/title/tt{imdbid}'
        self.raw_data = ''
        with open(self.path_to_the_file) as f:
            self.raw_data = f.read()
        self.all_movieIds = re.findall(',([0-9]+),', self.raw_data, re.MULTILINE)   # throw exception if empty

    @staticmethod
    def get_imdb(list_of_movies: list[str], list_of_fields: list[str]) -> list[list]:
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
        Sort it by movieId descendingly.
        """
        moviepage_url = 'https://www.imdb.com/title/tt{imdbid}'
        imdb_info = []
        for movie_id in list_of_movies:
            movie_info = [movie_id]

            movie_page = requests.get(moviepage_url.format(imdbid=movie_id))
            soup = BeautifulSoup(movie_page.text, 'html.parser')
            # soup.get()
            imdb_info.append(movie_info)
        return imdb_info

    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        return directors

    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        return budgets

    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
     Sort it by the difference descendingly.
        """
        return profits

    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
     Sort it by runtime descendingly.
        """
        return runtimes

    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
     The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        return costs