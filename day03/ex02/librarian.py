#!/usr/bin/env python

import os


if __name__ == '__main__':
    print(os.environ['VIRTUAL_ENV'])
    os.system('pip install beautifulsoup4 PyTest')
    os.system('pip freeze > requirements.txt')
