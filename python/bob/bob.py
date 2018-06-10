import re

def hey(phrase):
    question = re.compile(r'.*\?$')

    if (question.match(phrase)):
        return 'Sure.'

    return 'Whatever.'
