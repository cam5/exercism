import re

def hey(phrase):
    phrase   = phrase.strip()
    question = re.compile(r'.*\?$')
    letters  = ''.join([l for l in phrase if re.match(r'\w', l)])
    yelling  = False

    if (True == letters.isupper()):
        yelling = True

    if (True == yelling):
        if (question.match(phrase)):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'

    if (question.match(phrase)):
        return 'Sure.'

    if (letters.strip() == ''):
        return 'Fine. Be that way!'


    return 'Whatever.'
