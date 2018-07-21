def decode(string):
    return string


def encode(string):
    prev_letter = ''
    prev_index  = 0
    groups      = []
    strlen      = len(string) - 1

    for i in range(len(string)):
        letter        = string[i];
        new_character = False
        at_end        = (i == strlen)

        if (letter != prev_letter):
            new_character = True

        if (at_end):
            if not (new_character):
                groups.append(string[prev_index:(i + 1)])
            else:
                groups.append(string[i])

        if (new_character and 0 != i):
            groups.append(string[prev_index:i])
            prev_index  = i

        prev_letter = letter

    retval = ''

    for g in groups:
        char = g[0]
        if (1 == len(g)):
            retval += char
        else:
            retval += '{0}{1}'.format(len(g), char)

    return retval
