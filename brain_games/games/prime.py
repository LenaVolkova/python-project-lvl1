from random import randint


RULES = "Answer \"yes\" if the number is prime. Otherwise answer \"no\"."
MIN_NUMBER = 1
MAX_NUMBER = 4000


def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def make_question():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(random_number)
    if is_prime(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
