"""12 Days of Christmas exercise from exercism.io"""

BASE = "On the {} day of Christmas "
VERSES = ["twelve Drummers Drumming, ",
          "eleven Pipers Piping, ",
          "ten Lords-a-Leaping, ",
          "nine Ladies Dancing, ",
          "eight Maids-a-Milking, ",
          "seven Swans-a-Swimming, ",
          "six Geese-a-Laying, ",
          "five Gold Rings, ",
          "four Calling Birds, ",
          "three French Hens, ",
          "two Turtle Doves, ",
          "a Partridge in a Pear Tree."]


def num_to_suffixed_text(num):
    """Just a little lookup"""
    return ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
            'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][num - 1]

def get_verse(num):
    output = []

    output.append(BASE.format(num_to_suffixed_text(num)))
    output.append("my true love gave to me, ")

    for gift in range(1, num):
        output.append(VERSES[gift])

    if num == 1:
        output.append('a Partridge in a Pear Tree.')
    else:
        output.append('and a Partridge in a Pear Tree.')

    return output


def recite(start_verse, end_verse):
    """Recite the day of christmas, given a start and end verse."""
    verses = []

    if start_verse == end_verse:
        verses = get_verse(start_verse)

    for verse in range(start_verse, end_verse):
        verses += get_verse(verse)

    return verses
