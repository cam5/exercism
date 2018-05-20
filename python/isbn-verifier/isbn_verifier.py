def verify(isbn):
    char_list = [d for d in list(isbn) if d != '-']

    # don't allow lists of less than 9 digits
    if (len(char_list) < 9):
        return False

    # Replace our check digit if it's an X
    if (char_list[-1] == 'X'):
        char_list[-1] = 10

    # If there's something other than a number at this point, it's invalid.
    for char in char_list:
        print(char)
        print(type(char) == 'str' and char.isalpha())
        if type(char) == 'str' and False == char.isnumeric():
            print('this one then')
            return False

    factor = 10
    val    = 0

    digit_list = [int(d) for d in char_list]

    for digit in digit_list:
        val    = val + digit * factor
        factor = factor - 1

    print(val)

    return 0 == (val % 11)
