from random import randint
import logging
import requests
import json


class Research:
    def __init__(self, filename: str = None):
        self.__file_to_read = filename
        logging.info('Research type object created')

    def file_reader(self, has_header: bool = True) -> list[list[int, int]]:
        logging.info("Reading file")
        data = []
        if self.__file_to_read is None:
            logging.error("Filename to read wasn't provided")
            raise Exception('Empty path was provided')
        ok_pair = (['0', '1'], ['1', '0'])
        with open(self.__file_to_read, 'r') as file:
            for line in file:
                pair = line.strip('\n').split(',')
                if len(pair) != 2 or not all([word for word in pair]) or (not has_header and pair not in ok_pair):
                    logging.error("Filename to read wasn't provided")
                    raise Exception('The input file has the wrong format')
                if has_header:
                    has_header = False
                    continue
                data.append([int(pair[0]), int(pair[1])])

        return data

    @staticmethod
    def send_report_to_slack(url, msg: str) -> None:
        logging.info('Sending message to Slack')
        requests.post(url, json.dumps(msg))

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info('Research.Calculations type object created')

        def counts(self) -> list[int, int]:
            logging.info('Calculating heads and tails')
            return [sum(map(lambda x: int(x[0]), self.data)), sum(map(lambda x: int(x[1]), self.data))]

        @staticmethod
        def fractions(data: list[int, int]) -> list[int, int]:
            x, y = data
            logging.info('Calculating heads and tails fractions')
            return [x*100 / sum(data), y*100 / sum(data)]

    class Analytics(Calculations):
        @staticmethod
        def predict_random(num_of_pred: int) -> list[list]:
            logging.info("Predicting next head and tail pairs")
            res = []
            for i in range(0, num_of_pred):
                x = randint(0, 1)
                res.append([x, int(not x)])
            return res

        def predict_last(self):
            logging.info("Finding out the last element in data")
            return self.data[-1]

        @staticmethod
        def save_file(data, name_of_file: str, extension: str = 'txt'):
            logging.info("Saving data to file")
            with open(name_of_file.strip('/') + '.' + extension, 'w') as file:
                file.write(data)
