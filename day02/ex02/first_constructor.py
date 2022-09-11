import sys


class Research:
    def __init__(self, filename: str = None):
        self.__file_to_read = filename

    def file_reader(self) -> str:
        data = ''
        if self.__file_to_read is None:
            raise Exception('Empty path was provided')
        ok_pair = (['0', '1'], ['1', '0'])
        with open(self.__file_to_read, 'r') as file:
            for line in file:
                pair = line.strip('\n').split(',')
                if len(pair) != 2 or not all([word for word in pair]) or (data != '' and pair not in ok_pair):
                    raise Exception('The input file has the wrong format')
                data += line

        return data


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ob = Research(sys.argv[1])
        try:
            print(ob.file_reader())
        except Exception as ex:
            print(ex)
