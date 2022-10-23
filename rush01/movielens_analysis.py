import re
from functools import reduce
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pytest


class Movies:
    """
    Analyzing data from movies.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file
        self.movies_list = []
        with open(path_to_the_file) as f:
            self.movies_list = f.read().splitlines()[1:]
        self.movies_string = '\n'.join(self.movies_list)
        for line in self.movies_list:
            test_line = re.findall('([0-9]+),(.+),([a-z-A-Z |\(\)]+)$', line)
            if not test_line or len(test_line[0]) != 3:
                raise Exception('EXCEPTION: Incorrect file format')

    def get_title_by_id(self, movie_id):
        line = re.search(f'^{movie_id},(.+),', self.movies_string, re.MULTILINE)
        if line:
            return re.sub(' \([0-9]{4}\)', '', line.group(1))

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts.
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        release_years = {int(key): len(re.findall(f' \({key}\)', self.movies_string)) for key in set(re.findall(' \(([0-9]{4})\)', self.movies_string))}
        return dict(sorted(release_years.items(), key=lambda x: -x[1]))

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
        Sort it by counts descendingly.
        """
        all_genres = re.findall(',([A-Z-a-z|]+)$', self.movies_string, re.MULTILINE)
        all_genres = reduce(lambda x, y: x.__add__(y), map(lambda x: x.split('|'), all_genres))
        genres = {key: all_genres.count(key) for key in set(all_genres)}
        return dict(sorted(genres.items(), key=lambda x: -x[1]))

    def most_genres(self, n: int = 5):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        movies = {}
        titles = re.findall('^[0-9]+,"*(.+),', self.movies_string, re.MULTILINE)
        titles = list(map(lambda x: re.sub(' \([0-9]{4}\)', '', x), titles))
        for i, key in enumerate(titles):
            tmp = self.movies_list[i][self.movies_list[i].rfind(',') + 1:]
            movies[key] = len(tmp.split('|')) if tmp != '(no genres listed)' else 0
        return dict(sorted(movies.items(), key=lambda x: -x[1])[:n])


class Tags:
    """
    Analyzing data from tags.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file
        self.tags_list = []
        try:
            with open(path_to_the_file) as f:
                self.tags_list = f.read().splitlines()[1:]
        except FileNotFoundError as ex:
            print(ex)
        self.tags_string = '\n'.join(self.tags_list)

        for line in self.tags_list:
            test_line = re.findall('([0-9]+),([0-9]+),(.+),([0-9]+)$', line)
            if not test_line or len(test_line[0]) != 4:
                raise Exception('EXCEPTION: Incorrect file format')

    def __get_tags(self):
        return re.findall(',([^,]+),[0-9]+$', self.tags_string, re.MULTILINE)

    def most_words(self, n:int = 5):
        """
        The method returns top-n tags with most words inside. It is a dict
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = {key: len(key.replace('-', ' ').split()) for key in self.__get_tags()}
        return dict(sorted(big_tags.items(), key=lambda x: -x[1])[:n])

    def longest(self, n: int = 5):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = {key: len(key) for key in self.__get_tags()}
        return list(map(lambda x: x[0], sorted(big_tags.items(), key=lambda x: -x[1])[:n]))

    def most_words_and_longest(self, n: int = 5):
        """
        The method returns the intersection between top-n tags with most words inside and
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        big_tags = {key: len(key) + len(key.replace('-', ' ').split()) for key in self.__get_tags()}
        return list(map(lambda x: x[0], (sorted(big_tags.items(), key=lambda x: -x[1])[:n])))

    def most_popular(self, n: int = 5):
        """
        The method returns the most popular tags.
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        popular_tags = {key: len(re.findall(f'{key}', self.tags_string, re.MULTILINE)) for key in self.__get_tags()}
        return dict(sorted(popular_tags.items(), key=lambda x: -x[1])[:n])

    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        return sorted(set(re.findall(f',([^,]*{word}.*),[0-9]+$', self.tags_string, re.MULTILINE)))


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

        for line in self.ratings_list:
            test_line = re.findall('([0-9]+),([0-9]+),([0-5]\.[05]),([0-9]+)$', line)
            if not test_line or len(test_line[0]) != 4:
                raise Exception('EXCEPTION: Incorrect file format')

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
            return (vals[len(vals) // 2] + vals[len(vals) // 2 - 1]) / 2

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

        def top_by_num_of_ratings(self, n: int = 5):
            """
            The method returns top-n movies by the number of ratings.
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            return dict(sorted({self.get_title_by_id(int(key)): self.movie_ids.count(key)
                                for key in set(self.movie_ids)}.items(), key=lambda x: -x[1])[:n])

        def top_by_ratings(self, n: int = 5, metric='average'):
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

        def top_controversial(self, n: int = 5):
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

class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file_links, path_to_the_file_movies: str = 'data/movies.csv'):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file_links = path_to_the_file_links
        self.path_to_the_file_movies = path_to_the_file_movies
        self.moviepage_url = 'https://www.imdb.com/title/tt{imdbid}'
        self.movies = {}
        self.movies_info_list = []
        self.movies_info_string = ''
        with open(self.path_to_the_file_links) as links, open(self.path_to_the_file_movies) as movies:
            for (link, movie) in zip(links, movies):
                data = {}
                link_splitted = link.strip('\n').split(',')
                movie_splitted = re.findall('^([0-9]*),(.*),([a-zA-Z-|]*)$', movie)
                if not movie_splitted:
                    continue
                movie_splitted = movie_splitted[0]
                if len(movie_splitted) != 3 or len(link_splitted) != 3 or link_splitted[0] != movie_splitted[0]:
                    raise Exception("Movies aren't sorted by movieId, or some movies are missing")
                data['movieId'] = int(link_splitted[0])
                data['imdbId'] = link_splitted[1]
                data['tmdbId'] = link_splitted[2]
                data['title'] = movie_splitted[1]
                data['genres'] = movie_splitted[2]
                self.movies[link_splitted[1]] = data
                del data
            # self.movies_info = self.get_imdb(list(self.movies.keys()),
            #                                  ['Director', 'Budget', 'Gross worldwide', 'Runtime'])
        with open('data/films_info.txt') as f:
            for line in f:
                data = line.strip('\n').split(', ')
                if len(data) > 2:
                    self.movies_info_list.append(line.strip('\n').split(', '))
                    self.movies_info_string += line

    def __get_parsed_data(self, soup, list_of_fields):
        data = []
        for field in list_of_fields:
            match field.lower():
                case 'director':
                    data.append(soup.find('a', {
                        'class': 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}).text)
                case 'budget':
                    data.append(soup.find('div', {
                        'data-testid': "title-boxoffice-section",
                        'class': 'sc-f65f65be-0 ktSkVi'}).div.text)
                case 'gross worldwide':
                    for li in soup.find_all('li', {'class': 'ipc-metadata-list__item sc-6d4f3f8c-2 fJEELB'}):
                        if li.span.text == 'Gross worldwide':
                            data.append(li.div.text)
                case 'runtime':
                    data.append(soup.find('li', {
                        'data-testid': "title-techspec_runtime"}).div.text)
                case 'rating':
                    data.append(soup.find('div', {
                        'data-testid': "hero-rating-bar__aggregate-rating__score"}).span.text)
                case 'writers':
                    for li in soup.find('ul', {
                        'class': "ipc-metadata-list ipc-metadata-list--dividers-all sc-36c36dd0-9 fEgKYH ipc-metadata-list--base"}).find_all('li', {'class': 'ipc-metadata-list__item ipc-metadata-list-item--link'}):
                        if li.a.text == 'Writers':
                            data.append([writers.text for writers in li.div.find_all('a')])
                case 'release date':
                    data.append(soup.find('li', {'data-testid': "title-details-releasedate"}).div.text)
                case 'country of origin':
                    data.append(soup.find('li', {'data-testid': "title-details-origin"}).div.text)
        return data

    def get_imdb(self, list_of_movies: list[str], list_of_fields: list[str]) -> list[list]:
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
        Sort it by movieId descendingly.
        Implemented fields to pull:
            movieId, Director, Budget, Gross worldwide, Runtime,
            Rating, Writers, Release date, Country of origin
        """
        implemented_fields = ['movieid', 'director', 'budget', 'gross worldwide', 'runtime',
                              'rating', 'writers', 'release date', 'country of origin']
        for field in list_of_fields:
            if field.lower() not in implemented_fields:
                raise Exception(f"Field ({field}) you are trying to get isn't implemented")

        moviepage_url = 'https://www.imdb.com/title/tt{imdbid}'
        imdb_info = []
        for movie_id in list_of_movies:
            movie_info = [movie_id]
            movie_page = requests.get(moviepage_url.format(imdbid=movie_id))
            if movie_page.status_code != 200:
                print(movie_id)
                raise Exception('No movie in IMDB with such imdbId')
            try:
                movie_info.extend(self.__get_parsed_data(BeautifulSoup(movie_page.text, 'html.parser'), list_of_fields))
            except Exception as _:
                pass
            imdb_info.append(movie_info)
        return sorted(imdb_info, key=lambda x: x[0], reverse=True)

    def top_directors(self, n: int = 5):
        """
        The method returns a dict with top-n directors where the keys are directors and
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        directors = {director[1]: self.movies_info_string.count(director[1]) for director in self.movies_info_list}
        return dict(sorted(directors.items(), key=lambda x: x[1], reverse=True)[:n])

    def most_expensive(self, n: int = 5):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        budgets = {self.movies[imdbId[0]]['title']: int(''.join(re.search('([0-9,]+)', imdbId[2]).group(1).split(',')))
                   for imdbId in self.movies_info_list}
        return dict(sorted(budgets.items(), key=lambda x: x[1], reverse=True)[:n])

    def most_profitable(self, n: int = 5):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
        Sort it by the difference descendingly.
        """
        profits = {self.movies[imdbId[0]]['title']: int(''.join(re.search('([0-9,]+)', imdbId[3]).group(1).split(','))) -
                                                    int(''.join(re.search('([0-9,]+)', imdbId[2]).group(1).split(',')))
                   for imdbId in self.movies_info_list}
        return dict(sorted(profits.items(), key=lambda x: x[1], reverse=True)[:n])

    def longest(self, n: int = 5):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
        Sort it by runtime descendingly.
        """
        runtimes = {}
        for imdbId in self.movies_info_list:
            if len(imdbId) == 5:
                runtimes[self.movies[imdbId[0]]['title']] = int(imdbId[4].split(' ')[0])*60 + int(imdbId[4].split(' ')[2])
        return dict(sorted(runtimes.items(), key=lambda x: x[1], reverse=True)[:n])

    def top_cost_per_minute(self, n: int = 5):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
        The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        costs = {}
        for imdbId in self.movies_info_list:
            if len(imdbId) == 5:
                cost = round(int(''.join(re.search('([0-9,]+)', imdbId[2]).group(1).split(','))) /
                             (int(imdbId[4].split(' ')[0]) * 60 + int(imdbId[4].split(' ')[2])) * 100) / 100
                costs[self.movies[imdbId[0]]['title']] = cost
        return dict(sorted(costs.items(), key=lambda x: x[1], reverse=True)[:n])


class Tests:
    movies = Movies('data/movies.csv')
    tags = Tags('data/tags.csv')
    ratings = Ratings('data/ratings.csv')
    links = Links('data/links_shorted.csv', 'data/movies_shorted.csv')

    def test_movies_dist(self):
        data = self.movies.dist_by_release()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == int
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.movies.dist_by_genres()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.movies.most_genres()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

    def test_tags(self):
        data = self.tags.most_words(5)
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.tags.longest()
        assert type(data) == list
        assert type(data[0]) == str
        assert data == sorted(data, key=len, reverse=True)
        del data

        data = self.tags.longest()
        assert type(data) == list
        assert type(data[0]) == str
        assert data == sorted(data, key=lambda x: len(x) + len(x.replace('-', ' ').split()), reverse=True)
        del data

        data = self.tags.most_popular()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.tags.tags_with('high')
        assert type(data) == list
        assert type(data[0]) == str
        assert len(data) == 3
        assert data == sorted(data)
        del data

    def test_ratings_movies(self):
        data = self.ratings.movies.dist_by_year()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == int
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1]))
        del data

        data = self.ratings.movies.dist_by_rating()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == float
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1]))
        del data

        data = self.ratings.movies.top_by_num_of_ratings()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.ratings.movies.top_by_ratings()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == float
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.ratings.movies.top_controversial()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == float
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

    def test_ratings_users(self):
        assert issubclass(type(self.ratings.users), Movies)

        data = self.ratings.users.dist_by_ratings_number()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == int
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.ratings.users.dist_by_ratings_metric()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == int
        assert type(list(data.values())[0]) == float
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.ratings.users.top_n_by_variance()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == int
        assert type(list(data.values())[0]) == float
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

    def test_links(self):
        filt = ['movieid', 'director', 'budget', 'gross worldwide', 'runtime',
                'rating', 'writers', 'release date', 'country of origin']
        data = self.links.get_imdb(['0114709', '0113497'], filt)
        assert type(data) == list
        assert type(data[0]) == list
        assert data == sorted(data, key=lambda x: x[0], reverse=True)
        del data

        data = self.links.top_directors()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.links.most_expensive()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.links.most_profitable()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.links.longest()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == int
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data

        data = self.links.top_cost_per_minute()
        assert type(data) == dict
        assert type(list(data.keys())[0]) == str
        assert type(list(data.values())[0]) == float
        assert data == dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        del data
