"""12 Days of Christmas exercise from exercism.io"""

BASE = "On the {} day of Christmas my true love gave to me, "
VERSES = ["twelve Drummers Drumming, "
          "eleven Pipers Piping, "
          "ten Lords-a-Leaping, "
          "nine Ladies Dancing, "
          "eight Maids-a-Milking, "
          "seven Swans-a-Swimming, "
          "six Geese-a-Laying, "
          "five Gold Rings, "
          "four Calling Birds, "
          "three French Hens, "
          "two Turtle Doves, "
          "a Partridge in a Pear Tree."]


def num_to_suffixed_text(num):
    """Just a little lookup"""
    return ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
            'eighth', 'ninth', 'tenth', 'eleventh', 'twelth'][-num]

def get_verse(num, start_verse, end_verse):
    output = ''
    num -= num

    if num > start_verse:
        output += "\n\n"

    output += BASE.format(num_to_suffixed_text(num))

    for gift in VERSES[start_verse:end_verse]:
        output += reversed(VERSES[gift])

    return output

def recite(start_verse, end_verse):
    """Recite the twelfth day of christmas, given a start and end verse."""
    output = ''

    if (start_verse == end_verse):
        output = get_verse(start_verse, start_verse, end_verse)

    for verse in range(start_verse, end_verse):
        output += get_verse(verse, start_verse, end_verse)

    return output
