import random


RULES = 'Answer "yes" if the number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 4000


def is_prime(num):
    if num <= 1:
        return False
    else:
        for divider in range(2, num // 2):
            if num % divider == 0:
                return False
        return True


def make_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
