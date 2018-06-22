# Score categories
# Change the values as you see fit
YACHT = 'Yacht'
ONES = 'Ones'
TWOS = 'Twos'
THREES = 'Threes'
FOURS = 'Fours'
FIVES = 'Fives'
SIXES = 'Sixes'
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None

NUMBER_CATEGORY_DICT = {
    ONES: 1,
    TWOS: 2,
    THREES: 3,
    FOURS: 4,
    FIVES: 5,
    SIXES: 6
}

def score(dice, category):
    if (category == YACHT):
        check    = True
        prev_num = 0

        for num in dice:
            """Checking the first dice"""
            if (prev_num == 0):
                prev_num = num
            else:
                """We're checking against previously rolled dice"""
                # Is it equal to the last one?
                check = (num == prev_num)
                if (False == check):
                    # No? Then it's not a valid "Yacht"
                    break

        return 50 if check == True else 0

    if (category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]):
        target_num = NUMBER_CATEGORY_DICT[category]

        return dice.count(target_num) * target_num


