"""
Author:      Jeremy Cornett
Date:        06/07/2017
"""


def main(balls):
    """The main entry point for this script.
    :param balls: The number of balls in the ball clock machine.
    :type balls: int
    :return: The number of days that the clock represents unique time before a ball position is repeated.
    :rtype: int
    """
    elapsed_days = 0
    print "I'm a ball machine with {} balls and I have no idea how many days I can keep " \
          "track of time, yet.".format(balls)

    """
    Okay, so these ball queues, they fill up, and then empty the last added ball into the next queue, and then dumps
    all of the remainder balls out into the original queue again.
    The question is, if we identify each ball uniquely, remember the start order, how many inputs into the
    second queue will it take for the overall order of the balls to repeat? Round down the nearest day. We don't 
    even care what time the ball-clock can show. We just need to know when the order is repeated the first time.
    
    Queue Hold
        Max: None
        Placeholders: 0
        Load Event: FIFO 1 into Queue Min.
    Queue OneMin
        Max: 4 
        Placeholders: 0
        Empty Event: LIFO 1 into Queue FiveMin, LIFO 4 into Queue Hold.
    Queue FiveMin
        Max: 11
        Placeholders: 0
        Empty Event: LIFO 1 into Queue Hour, LIFO 11 into Queue Hold.
    Queue Hour
        Max: 12
        Placeholders: 1
        Empty Event: LIFO 12 into Queue Hold.
    
    INITIAL STATE
        Fill all placeholders in each queue. Remaining balls go in Queue Hold.
        Order: This initial order is the testing order.
        
    CHECK STATE
        Order: All non-placeholder balls in Queues Hold, OneMin, FiveMin, and Hour placed front to back.
    """

    return elapsed_days


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
