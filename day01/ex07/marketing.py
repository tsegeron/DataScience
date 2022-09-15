import sys


def call_center(clients, participants, recipients):
    return clients - recipients


def potential_clients(clients, participants, recipients):
    return (participants | recipients) - clients


def loyalty_program(clients, participants, recipients):
    return (clients | recipients) - participants


def foo(task):
    if task not in ('call_center', 'potential_clients', 'loyalty_program'):
        raise ValueError('Incorrect request')
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    return list(eval(f'{task}(set(clients), set(participants), set(recipients))'))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            print(foo(sys.argv[1].lower()))
        except ValueError as ex:
            print(ex)
