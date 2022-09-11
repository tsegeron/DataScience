class Research:
    def __init__(self, filename: str = 'data.csv'):
        self.__file_to_read = filename

    def file_reader(self) -> str:
        data = str()
        with open(self.__file_to_read, 'r') as file:
            for line in file:
                data += line
        return data


if __name__ == '__main__':
    ob = Research()
    print(ob.file_reader())
