# Score categories
# Change the values as you see fit
YACHT = 'Yacht'
ONES = 'Ones'
TWOS = 'Twos'
THREES = 'Threes'
FOURS = 'Fours'
FIVES = 'Fives'
SIXES = 'Sixes'
FULL_HOUSE = 'Full House'
FOUR_OF_A_KIND = 'Four of a Kind'
LITTLE_STRAIGHT = 'Little Straight'
BIG_STRAIGHT = 'Big Straight'
CHOICE = 'Choice'

NUMBER_CATEGORY_DICT = {
    ONES: 1,
    TWOS: 2,
    THREES: 3,
    FOURS: 4,
    FIVES: 5,
    SIXES: 6
}

def score(dice, category):
    def die_totals(dice):
        die_counter = {}

        for num in dice:
            if not num in die_counter:
                die_counter[num] = 1
            else:
                die_counter[num] += 1

        return die_counter

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

    if (category == BIG_STRAIGHT):
        return 30 if [2, 3, 4, 5, 6] == sorted(dice) else 0

    if (category == LITTLE_STRAIGHT):
        return 30 if [1, 2, 3, 4, 5] == sorted(dice) else 0

    if (category == FULL_HOUSE):
        die_counter = die_totals(dice)
        total       = 0

        for num, count in die_counter.items():
            if not count == 2 and not count == 3:
                return 0
            total += (num * count)

        return total

    if (category == CHOICE):
        return sum(dice)

    if (category == FOUR_OF_A_KIND):
        die_counter = die_totals(dice)

        for num, count in die_counter.items():
            if count >= 4:
                return 4 * num

        return 0
