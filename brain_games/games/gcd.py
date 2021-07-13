import random


RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER1 = 100
MAX_NUMBER2 = 200


# Euclid algorithm
def calculate_gcd(num1, num2):
    if (num1 <= num2) and (num2 % num1 == 0):
        return num1
    while num1 != num2:
        if num1 < num2:
            min = num1
            diff = num2 - min
        else:
            min = num2
            diff = num1 - min
        num1 = min
        num2 = diff
    return num1


def make_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER1)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER2)
    question = '{} {}'.format(str(num1), str(num2))
    answer = str(calculate_gcd(num1, num2))
    return (question, answer)
