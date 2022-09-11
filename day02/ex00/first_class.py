class MustRead:
    def __init__(self, filename: str = 'data.csv'):
        self.__file_to_read = filename

    def print_file(self) -> None:
        with open(self.__file_to_read, 'r') as file:
            for line in file:
                print(line, end='')


if __name__ == '__main__':
    ob = MustRead()
    ob.print_file()
