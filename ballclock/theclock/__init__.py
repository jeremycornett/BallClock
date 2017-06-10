"""
Author:      Jeremy Cornett
Date:        06/07/2017
"""

import BallClock


def a_clock(input):
    """The main entry point for this script.
    :param input: The number of balls in the ball clock machine.
    :type input: str
    :return: The number of days that the clock represents unique time before a ball position is repeated.
    :rtype: int
    """

    try:
        count = int(input)
    except:
        raise ValueError("'{}' is not valid input. Integers between 27 and 127 only. 0 to exit.".format(input))
    if count == 0:
        return 0
    if count < 27 or 127 < count:
        raise ValueError("The number of balls ({}) to test must be between 27 and 127. 0 to exit.".format(count))

    the_clock = BallClock.BallClock()
    the_clock.load(count)

    # Debug values
    # the_clock.debug = True
    # Five Minute Queue Change 1:00 - 1:10
    # the_clock.debug_start = 1
    # the_clock.debug_end = 12
    # Hour Queue Change 1:59 - 2:01
    # the_clock.debug_start = 59
    # the_clock.debug_end = 61
    # Day Queue Change 12:59 - 1:00
    # the_clock.debug_start = 1430
    # the_clock.debug_end = 1442

    elapsed_days = the_clock.run()
    print "{} days".format(elapsed_days)
    return elapsed_days


def run():
    while True:
        user_input = raw_input()
        result = a_clock(user_input)
        if result == 0:
            break
