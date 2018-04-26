def is_leap_year(year):
    ret = bool(0)

    # Divisible by 4 equals leap year
    if year % 4 == 0:
        ret = bool(1)

    # Skip the leap year every 100 years, when it is not divisible by 400
    if year % 100 == 0 and year % 400 != 0:
        ret = bool(0)

    return ret
