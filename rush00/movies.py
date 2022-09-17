import re
from functools import reduce


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
        try:
            with open(path_to_the_file) as f:
                self.movies_list = f.read().splitlines()[1:]
        except FileNotFoundError as ex:
            print(ex)
        self.movies_string = '\n'.join(self.movies_list)

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

    def most_genres(self, n):
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
