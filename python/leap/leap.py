def is_leap_year(year):
    # Start off with the assumption it isn't a leap yar.
    ret = False

    # Divisible by 4 equals leap year
    if year % 4 == 0:
        ret = True

    # Skip the leap year every 100 years, when it is not divisible by 400
    if year % 100 == 0 and year % 400 != 0:
        ret = False

    return ret
