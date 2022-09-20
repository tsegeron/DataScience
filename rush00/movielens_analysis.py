import requests
import json
from movies import Movies
from tags import Tags
from ratings import Ratings
from links import Links
import re
from datetime import datetime
from functools import reduce


if __name__ == '__main__':
    # m = Movies('data/movies.csv')
    # print(m.dist_by_release())
    # print(m.dist_by_genres())
    # print(m.most_genres(11))

    # t = Tags('data/tags.csv')
    # print(t.most_words(5))
    # print(t.longest(5))
    # print(t.most_words_and_longest(5))
    # print(t.most_popular(5))
    # print(t.tags_with('high'))

    # r = Ratings('data/ratings.csv')
    # print(r.movies.dist_by_year())
    # print(r.movies.dist_by_rating())
    # print(r.movies.top_by_num_of_ratings(5))
    # print(r.movies.top_by_ratings(5))
    # print(r.movies.top_by_ratings(5, 'median'))
    # print(r.movies.top_controversial(5))
    # print(r.users.dist_by_ratings_number())
    # print(r.users.dist_by_ratings_metric())
    # print(r.users.dist_by_ratings_metric(metric='median'))
    # print(r.users.top_n_by_variance())

    li = Links('data/links.csv')
    print(li.get_imdb(['0114709'], ['movieId', 'Director', 'Budget', 'Cumulative Worldwide Gross', 'Runtime']))

    pass
