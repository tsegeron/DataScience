import sys


def send_greeting_letter(email: str) -> None:
    with open('employees.tsv') as f:
        for line in f:
            splitted = line.strip('\n').split('\t')
            if splitted[2].lower() == email.lower():
                print(f'Dear {splitted[0]}, welcome to our team. '
                      f'We are sure that it will be a pleasure to work with you. '
                      f'That’s a precondition for the professionals that our company hires.')
                break


if __name__ == '__main__':
    if len(sys.argv) == 2:
        send_greeting_letter(sys.argv[1])
