from random import randint


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
    first_member = randint(0, 100)
    step = randint(1, 10)
    size = randint(5, 10)
    missing_number = randint(0, size - 1)
    question = make_progression(first_member, step, size, missing_number)
    answer = str(get_missing_member(first_member, step, missing_number))
    return (question, answer)
