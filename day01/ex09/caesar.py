import sys


def endecrypting(string: str, shift: int, decode_flag: bool) -> str:
    if shift == 0:
        return string
    decode_flag = -1 if decode_flag else 1

    en_or_de_crypted = ''
    for char in string:
        if char.isalpha():
            capital = ord('a' if ord(char) > 96 else 'A')
            en_or_de_crypted += chr((ord(char) - capital + (shift % 26) * decode_flag) % 26 + capital)
        else:
            en_or_de_crypted += char
    return en_or_de_crypted


def foo():
    if not len(sys.argv) == 4:
        raise Exception('Incorrect number of arguments is given.')
    if sys.argv[1].lower() not in ('encode', 'decode'):
        raise Exception('Method unrecognized.')
    if not sys.argv[2].isascii():
        raise Exception('The script does not support your language yet.')
    if not sys.argv[3].isdigit():
        raise Exception('Incorrect shift value. Not an integer.')
    print(endecrypting(sys.argv[2], int(sys.argv[3]), sys.argv[1].lower() == "decode"))


if __name__ == '__main__':
    try:
        foo()
    except Exception as ex:
        print('EXCEPTION:', ex)
