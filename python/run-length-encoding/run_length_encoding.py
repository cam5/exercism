import re

def decode(string):
    return string


def encode(string):
    buffer_string = ''
    prev_char     = ''
    ret_val       = ''
    total_count   = 1

    for l in string:
        at_end        = total_count == len(string)
        new_character = False

        if (l != prev_char):
            new_character = True

        if (False == new_character):
            buffer_string += prev_char

        if (True == new_character or at_end):
            buffer_length = len(buffer_string)

            if (0 == buffer_length):
                ret_val += prev_char
            else:
                ret_val += '{0}{1}'.format((1 + buffer_length), prev_char)
            buffer_string = ''

        prev_char = l
        total_count += 1

    return ret_val
