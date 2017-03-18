<?php

/**
 * Calculates 10^9 seconds from a given date.
 *
 * @param \DateTime $date The input date.
 *
 * @return \DateTime A new date object.
 */
function from(\DateTime $date)
{
    $newDate = \DateTime::createFromFormat(
        \DateTime::RFC2822,
        $date->format(\DateTime::RFC2822)
    );

    return $newDate->modify('+1000000000 seconds');
}//end from()
