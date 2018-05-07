def reverse(input=''):
    input_list = list(input)
    ret        = list()

    for l in input_list:
        ret.insert(0, l)

    return ''.join(ret)
