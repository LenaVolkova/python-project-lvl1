from random import randint


def is_prime(num):
    i = 2
    answer = 'yes'
    while i <= (num / 2):
        if num % i == 0:
            answer = 'no'
            i = num
        else:
            i += 1
    return answer


def make_question():
    random_number = randint(1, 4000)
    question = str(random_number)
    answer = is_prime(random_number)
    return (question, answer)
