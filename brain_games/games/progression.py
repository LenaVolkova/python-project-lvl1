import random


RULES = "What number is missing in the progression?"
MIN_FIRST_MEMBER = 0
MAX_FIRST_MEMBER = 100
MIN_STEP = 1
MAX_STEP = 10
MIN_SIZE = 5
MAX_SIZE = 10


def make_progression(member, step, size, missing_number):
    question_str = ''
    i = 0
    while i < size:
        if i == missing_number:
            question_str = ''.join([question_str, '.. '])
        else:
            question_str = ''.join([question_str, str(step * i + member)])
            question_str = ''.join([question_str, ' '])
        i += 1
    return question_str


def get_missing_member(member, step, missing_number):
    answer = member + missing_number * step
    return answer


def make_question():
    first_member = random.randint(MIN_FIRST_MEMBER, MAX_FIRST_MEMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    size = random.randint(MIN_SIZE, MAX_SIZE)
    missing_number = random.randint(0, size - 1)
    question = make_progression(first_member, step, size, missing_number)
    answer = str(get_missing_member(first_member, step, missing_number))
    return (question, answer)
