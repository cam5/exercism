from datetime import datetime

def add_gigasecond(birth_date):
    # datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

    gigasecond = 1000000000
    gigastamp  = birth_date.timestamp() + gigasecond
    gigaday    = datetime.fromtimestamp(gigastamp)

    return gigaday.replace(hour=1)
