from datetime import datetime
from movies import Movies
from functools import reduce
import re


class Ratings:
    """
    Analyzing data from ratings.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file
        self.ratings_list = []
        try:
            with open(path_to_the_file) as f:
                self.ratings_list = f.read().splitlines()[1:]
        except FileNotFoundError as ex:
            print(ex)
        self.ratings_string = '\n'.join(self.ratings_list)

        self.movies = Ratings.Movies('data/movies.csv', self.ratings_string)

    class Movies(Movies):
        def __init__(self, path_to_file, ratings_string):
            super().__init__(path_to_file)
            self.ratings_string = ratings_string

        @staticmethod
        def __get_median(vals):
            if len(vals) % 2:
                return round(vals[len(vals) // 2] * 100) / 100
            return round((vals[len(vals) // 2] + vals[len(vals) // 2 - 1]) * 50) / 100

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts.
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            secs = list(map(lambda x: datetime.fromtimestamp(int(x)).year, re.findall('([0-9]+)$', self.ratings_string, re.MULTILINE)))
            return dict(sorted({key: secs.count(key) for key in set(secs)}.items(), key=lambda x: x[0]))

        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
            Sort it by ratings ascendingly.
            """
            ratings = re.findall('[0-5]\.[05]', self.ratings_string, re.MULTILINE)
            return dict(sorted({float(key): ratings.count(key) for key in set(ratings)}.items(), key=lambda x: x[0]))

        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings.
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            top_movies = re.findall(',([0-9]+),', self.ratings_string, re.MULTILINE)
            return dict(sorted({self.get_title_by_id(int(key)): top_movies.count(key) for key in set(top_movies)}.items(), key=lambda x: -x[1])[:n])

        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            movies_id = set(re.findall(',([0-9]+),', self.ratings_string, re.MULTILINE))
            movies_id_rates = {
                key: sorted(map(float, re.findall(f',{key},([0-5]\.[05]),', self.ratings_string, re.MULTILINE)))
                for key in movies_id}
            if metric == 'average':
                return dict(sorted({self.get_title_by_id(key): round(sum(val) * 100 / len(val)) / 100
                                    for key, val in movies_id_rates.items()}.items(), key=lambda x: -x[1])[:n])
            elif metric == 'median':
                return dict(sorted({self.get_title_by_id(key): self.__get_median(val)
                                    for key, val in movies_id_rates.items()}.items(), key=lambda x: -x[1])[:n])

        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
            Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            movies_id = set(re.findall(',([0-9]+),', self.ratings_string, re.MULTILINE))
            movies_id_rates = {}
            for key in movies_id:
                vals = list(map(float, re.findall(f',{key},([0-5]\.[05]),', self.ratings_string, re.MULTILINE)))
                movies_id_rates[self.get_title_by_id(key)] = sum(map(lambda x: (x - sum(vals)/len(vals))**2, vals)) / len(vals)
            return dict(sorted(movies_id_rates.items(), key=lambda x: -x[1])[:n])

    class Users(Movies):
        """
        In this class, three methods should work.
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
        Inherit from the class Movies. Several methods are similar to the methods from it.
        """
        def __init__(self, path_to_file, ratings_string):
            super().__init__(path_to_file, ratings_string)

        def dist_by_ratings_number(self):
            pass

        def dist_by_ratings_metric(self, metric='average'):
            pass

        def top_n_by_variance(self, n):
            pass
