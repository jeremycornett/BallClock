"""
Author:      Jeremy Cornett
Date:        06/07/2017
"""

import argparse


def main(balls):
    """The main entry point for this script."""
    print "I'm a ball machine with {} balls and I have no idea how many days I can keep " \
          "track of time, yet.".format(balls)
    return balls


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
                        help='The number of balls in the ball clock. You can enter multiple numbers.')
    args = parser.parse_args()
    if args.balls is None or len(args.balls) == 0:
        main(-1)
    for a_number in args.balls:
        main(a_number)
