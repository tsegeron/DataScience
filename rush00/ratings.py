from datetime import datetime
from movies import Movies
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
        self.users = Ratings.Users('data/movies.csv', self.ratings_string)

    class Movies(Movies):
        def __init__(self, path_to_file, ratings_string):
            super().__init__(path_to_file)
            self.ratings_string = ratings_string
            self.movie_ids = re.findall(',([0-9]+),', self.ratings_string, re.MULTILINE)

        @staticmethod
        def get_median(vals):
            if len(vals) % 2:
                return vals[len(vals) // 2]
            return (vals[len(vals) // 2] + vals[len(vals) // 2 - 1]) * .5

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
            return dict(sorted({self.get_title_by_id(int(key)): self.movie_ids.count(key)
                                for key in set(self.movie_ids)}.items(), key=lambda x: -x[1])[:n])

        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            movies_id_rates = {
                key: sorted(map(float, re.findall(f',{key},([0-5]\.[05]),', self.ratings_string, re.MULTILINE)))
                for key in self.movie_ids}
            res = []
            if metric == 'average':
                res = sorted({key: sum(val) / len(val)
                              for key, val in movies_id_rates.items()}.items(), key=lambda x: x[1], reverse=True)[:n]
            elif metric == 'median':
                res = sorted({key: self.get_median(val)
                              for key, val in movies_id_rates.items()}.items(), key=lambda x: x[1], reverse=True)[:n]
            return {self.get_title_by_id(key): round(val * 100) / 100 for key, val in res}

        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
            Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            movies_id_rates = {}
            for key in self.movie_ids:
                vals = list(map(float, re.findall(f',{key},([0-5]\.[05]),', self.ratings_string, re.MULTILINE)))
                mean = sum(vals) / len(vals)
                movies_id_rates[key] = sum(map(lambda x: (x - mean)**2, vals)) / len(vals)
            res = sorted(movies_id_rates.items(), key=lambda x: x[1], reverse=True)[:n]
            return {self.get_title_by_id(key): round(val * 100) / 100 for key, val in res}

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
            self.all_rates = re.findall('^([0-9]+),', self.ratings_string, re.MULTILINE)
            self.all_ids = set(self.all_rates)

        def dist_by_ratings_number(self, n: int = 5):
            """
            Finds the distribution of users by the number of ratings made by them.

            :return: top-n items of Dict of user_id:number_of_ratings, descendingly sorted by number_of_ratings
            """
            return dict(sorted({int(key): self.all_rates.count(key)
                                for key in set(self.all_ids)}.items(), key=lambda x: -x[1])[:n])

        def dist_by_ratings_metric(self, n: int = 5, metric: str ='average'):
            """
            Finds the distribution of users by `average` or `median` ratings made by them.

            :return: top-n items of Dict of user_id:metric_value, descendingly sorted by number_of_ratings
            """
            users_rates = {
                int(key): sorted(map(float, re.findall(f'^{key},.+,([0-5]\.[05]),', self.ratings_string, re.MULTILINE)))
                for key in self.all_ids}
            if metric == 'average':
                return dict(sorted({key: round(sum(val) * 100 / len(val)) / 100
                                    for key, val in users_rates.items()}.items(), key=lambda x: -x[1])[:n])
            elif metric == 'median':
                return dict(sorted({key: self.get_median(val)
                                    for key, val in users_rates.items()}.items(), key=lambda x: -x[1])[:n])

        def top_n_by_variance(self, n: int = 5):
            """
            Finds top-n users with the biggest variance of their ratings.

            :return: dict of top-n users with the biggest variance of their ratings
            """
            users_rates = {}
            for key in self.all_ids:
                vals = list(map(float, re.findall(f'^{key},.+,([0-5]\.[05]),', self.ratings_string, re.MULTILINE)))
                users_rates[int(key)] = sum(map(lambda x: (x - sum(vals) / len(vals)) ** 2, vals)) / len(vals)
            return dict(sorted(users_rates.items(), key=lambda x: -x[1])[:n])
