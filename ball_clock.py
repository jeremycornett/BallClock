"""
Author:      Jeremy Cornett
Date:        06/07/2017
"""

import argparse
import sys


def main(balls):
    """The main entry point for this script.
    :param balls: The number of balls in the ball clock machine.
    :type balls: int
    :return: None
    """
    print "I'm a ball machine with {} balls and I have no idea how many days I can keep " \
          "track of time, yet.".format(balls)


def valid_input(the_input):
    """Validate that the ball count is a known valid number.
    :param the_input: Hopefully he number of balls in the ball clock machine.
    :type the_input: str
    :return: If the input was valid (True) or not (False).
    :rtype: bool
    """
    try:
        count = int(the_input)
    except:
        print "ValueError: '{}' is not valid input. Integers between 27 and 127 only. 0 to exit.".format(the_input)
        return False
    if count == 0:
        return True
    if count < 27 or 127 < count:
        print "ValueError: The number of balls ({}) to test must be between 27 and 127. 0 to exit.".format(count)
        return False
    return True


def test_example_1():
    """The first example values given in the readme."""
    assert main(30) == 15


def test_example_2():
    """The second example values given in the readme."""
    assert main(45) == 378


if __name__ == '__main__':
    while True:
        user_input = raw_input()
        if not valid_input(user_input):
            continue
        ball_count = int(user_input)
        if ball_count == 0:
            break
        main(ball_count)
