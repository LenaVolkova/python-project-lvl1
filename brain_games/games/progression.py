import random


RULES = 'What number is missing in the progression?'
MIN_FIRST_MEMBER = 0
MAX_FIRST_MEMBER = 100
MIN_STEP = 1
MAX_STEP = 10
MIN_SIZE = 5
MAX_SIZE = 10


def make_progression(first_member, step, size):
    progression = []
    for i in range(0, size):
        progression.append(first_member + step * i)
    return progression


def make_question():
    first_member = random.randint(MIN_FIRST_MEMBER, MAX_FIRST_MEMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    size = random.randint(MIN_SIZE, MAX_SIZE)
    missing_number = random.randint(0, size - 1)
    progression = make_progression(first_member, step, size)
    answer = str(progression[missing_number])
    progression[missing_number] = '..'
    question = ' '.join([str(i) for i in progression])
    return (question, answer)
