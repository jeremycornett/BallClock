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
    validate_input(balls)

    print "I'm a ball machine with {} balls and I have no idea how many days I can keep " \
          "track of time, yet.".format(balls)


def validate_input(ball_count):
    """Validate that the ball count is a known valid number.
    :param ball_count: The number of balls in the ball clock machine.
    :type ball_count: int
    :return: None
    """
    if ball_count < 27 or 127 < ball_count:
        raise ValueError("The number of balls ({}) to test must be between 27 and 127.".format(ball_count))


def test_example_1():
    """The first example values given in the readme."""
    assert main(30) == 15


def test_example_2():
    """The second example values given in the readme."""
    assert main(45) == 378


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Given a number of balls, how many days can the ball clock keep '
                                                 'track of time?')
    parser.add_argument('balls', metavar='N', type=int, nargs='*',
                        help='The number of balls in the ball clock (between 27 and 127). '
                             'You can enter multiple numbers.')
    args = parser.parse_args()
    if args.balls is None or len(args.balls) == 0:
        main(-1)
    list_errors = []
    for a_number in args.balls:
        try:
            main(a_number)
        except ValueError as err:
            list_errors.append(err)

    for an_error in list_errors:
        print "ValueError: {}".format(an_error)
    sys.exit(len(list_errors))
