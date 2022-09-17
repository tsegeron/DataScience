import re


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

    def __get_tags(self):
        return re.findall(',([^,]+),[0-9]+$', self.tags_string, re.MULTILINE)

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = {key: len(key.replace('-', ' ').split()) for key in self.__get_tags()}
        return dict(sorted(big_tags.items(), key=lambda x: -x[1])[:n])

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = {key: len(key) for key in self.__get_tags()}
        return list(map(lambda x: x[0], sorted(big_tags.items(), key=lambda x: -x[1])[:n]))

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        big_tags = {key: len(key) + len(key.replace('-', ' ').split()) for key in self.__get_tags()}
        return list(map(lambda x: x[0], (sorted(big_tags.items(), key=lambda x: -x[1])[:n])))

    def most_popular(self, n):
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
