# Score categories
# Change the values as you see fit
YACHT = 'Yacht'
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


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
