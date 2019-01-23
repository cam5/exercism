"""'Bob' from exercism.io"""

import re


def hey(phrase):
    """Core bob function... issues a reply to 'phrase'."""

    phrase = phrase.strip()
    question = re.compile(r'.*\?$')
    letters = ''.join([l for l in phrase if re.match(r'\w', l)])
    yelling = False

    if (letters.isupper() is True):
        yelling = True

    if (yelling is True):
        if (question.match(phrase)):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'

    if (question.match(phrase)):
        return 'Sure.'

    if (letters.strip() == ''):
        return 'Fine. Be that way!'

    return 'Whatever.'
