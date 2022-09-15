import sys


def create_table(filename: str):
    with open(filename) as infile:
        with open('employees.tsv', 'w') as outfile:
            outfile.write(f'Name\tSurname\tE-mail\n')
            for line in infile:
                splitted = line.split('.')
                outfile.write(f'{splitted[0].title()}\t{splitted[1].split("@")[0].title()}\t{line}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_table(sys.argv[1])
