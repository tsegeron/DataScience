import sys


class Research:
    def __init__(self, filename: str = None):
        self.__file_to_read = filename

    class Calculations:
        @staticmethod
        def counts(data: list[list[int, int]]) -> list[int, int]:
            return [sum(map(lambda x: int(x[0]), data)), sum(map(lambda x: int(x[1]), data))]

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


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ob = Research(sys.argv[1])
        try:
            file_content = ob.file_reader()
            counts = ob.Calculations.counts(file_content)
            print(file_content)
            print(counts)
            print(ob.Calculations.fractions(counts))
        except Exception as ex:
            print(ex)
