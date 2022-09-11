from random import randint


class Research:
    def __init__(self, filename: str = None):
        self.__file_to_read = filename

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self) -> list[int, int]:
            return [sum(map(lambda x: int(x[0]), self.data)), sum(map(lambda x: int(x[1]), self.data))]

        @staticmethod
        def fractions(data: list[int, int]) -> list[int, int]:
            x, y = data
            return [x*100 / sum(data), y*100 / sum(data)]

    def file_reader(self, has_header: bool = True) -> list[list[int, int]]:
        data = []
        if self.__file_to_read is None:
            raise Exception('Empty path was provided')
        ok_pair = (['0', '1'], ['1', '0'])
        with open(self.__file_to_read, 'r') as file:
            for line in file:
                pair = line.strip('\n').split(',')
                if len(pair) != 2 or not all([word for word in pair]) or (not has_header and pair not in ok_pair):
                    raise Exception('The input file has the wrong format')
                if has_header:
                    has_header = False
                    continue
                data.append([int(pair[0]), int(pair[1])])

        return data

    class Analytics(Calculations):
        @staticmethod
        def predict_random(num_of_pred: int) -> list[list]:
            res = []
            for i in range(0, num_of_pred):
                x = randint(0, 1)
                res.append([x, int(not x)])
            return res

        def predict_last(self):
            return self.data[-1]

        @staticmethod
        def save_file(data, name_of_file: str, extension: str = 'txt'):
            with open(name_of_file.strip('/') + '.' + extension, 'w') as file:
                file.write(data)
