def infile_replacer(infile: str, outfile: str, to_replace: str = ',', replace_with: str = '\t'):
    with open(infile) as file:
        data = file.readlines()
    with open(outfile, 'w') as out:
        flag = True
        for line in data:
            newline = ''
            for word in line.split(to_replace):
                quotes = word.count('"')
                if quotes % 2 != 0 or quotes == 0:
                    if quotes:
                        flag = not flag
                if flag:
                    newline += word + replace_with
                else:
                    newline += word + to_replace

            out.write(newline.strip(replace_with))


if __name__ == '__main__':
    infile_replacer('ds.csv', 'ds.tsv')
