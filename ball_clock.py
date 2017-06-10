"""
Author:      Jeremy Cornett
Date:        06/07/2017
"""

import pytest

class BallQueue:
    """Create the ball queue and the default behavior of such a ball queue."""

    def __init__(self, max, placeholders, queue_full_first=None, queue_full_remain=None):
        """Initialize the ball queue with the given information.
        :param maximum: The maximum number of balls the queue can hold.
        :type maximum: int
        :param placeholders: The total number of balls that have to go in placeholders for this queue.
        :type placeholders: int
        :param queue_full_first: The queue which gets a single ball LIFO from this queue.
        :type queue_full_first: BallQueue
        :param queue_full_remain: The queue which gets the remainder balls LIFO from this queue.
        :type queue_full_remain: BallQueue
        """
        self.balls = []
        self.maximum = max
        self.placeholder_total = placeholders
        self.queue_first = queue_full_first
        self.queue_remainder = queue_full_remain

    def add(self, the_ball):
        """Given this ball, adjust the queue and any subsequent queues.
        :param the_ball: The ball to add to the queue.
        :type the_ball: int
        """
        self.balls.append(the_ball)
        if len(self.balls) > self.maximum:
            if self.queue_first is not None:
                first_ball = self.pop_lifo()
            if self.queue_remainder is not None:
                while len(self.balls) != self.placeholder_total:
                    self.queue_remainder.add(self.pop_lifo())
            if self.queue_first is not None:
                self.queue_first.add(first_ball)

    def pop_fifo(self):
        """Return the next ball - FIFO.
        :return: The next ball.
        """
        if len(self.balls) <= self.placeholder_total:
            raise Exception("Queue is out of balls.")
        return self.balls.pop(self.placeholder_total)

    def pop_lifo(self):
        """Return the last ball - LIFO
        :return: The last ball
        """
        if len(self.balls) <= self.placeholder_total:
            raise Exception("Queue is out of balls.")
        return self.balls.pop()

    def get_order(self):
        """Return the order of balls in this queue."""
        return self.balls[self.placeholder_total:]


class BallClock:
    """
    Okay, so these ball queues, they fill up, and then empty the last added ball into the next queue, and then dumps
    all of the remainder balls out into the original queue again.
    The question is, if we identify each ball uniquely, remember the start order, how many inputs into the
    second queue will it take for the overall order of the balls to repeat? Round down the nearest day. We don't
    even care what time the ball-clock can show. We just need to know when the order is repeated the first time.

    Queue Hold
        Max: None
        Placeholders: 0
    Queue Hour
        Max: 12
        Placeholders: 1
        Empty Event: LIFO 12 into Queue Hold.
    Queue FiveMin
        Max: 11
        Placeholders: 0
        Empty Event: LIFO 1 into Queue Hour, LIFO 11 into Queue Hold.
    Queue OneMin
        Max: 4
        Placeholders: 0
        Empty Event: LIFO 1 into Queue FiveMin, LIFO 4 into Queue Hold.

    Ball Clock INITIAL STATE
        Fill all placeholders in each queue. Remaining balls go in Queue Hold.
        Order: This initial order is the testing order.

    Ball Clock CHECK STATE
        Increment Event: FIFO 1 into Queue Min.
        Order: All non-placeholder balls in Queues Hold, OneMin, FiveMin, and Hour placed front to back.
    """

    def __init__(self):
        """Keep track of all initial information available about the ball clock."""
        self.debug = False
        self.debug_start = 1
        self.debug_end = 10
        self.queue_hold = BallQueue(127, 0)
        self.queue_hour = BallQueue(12, 1, queue_full_first=self.queue_hold, queue_full_remain=self.queue_hold)
        self.queue_five_min = BallQueue(11, 0, queue_full_first=self.queue_hour, queue_full_remain=self.queue_hold)
        self.queue_minutes = BallQueue(4, 0, queue_full_first=self.queue_five_min, queue_full_remain=self.queue_hold)
        self.initial_order = []
        self.count_minutes = 0

    def load(self, count):
        """Load the specified number of balls into the ball clock's queues and placeholders. Store the initial order.
        :param count: The number of balls to load.
        :type count: int
        :return: None
        """
        # The placeholder balls don't count as part of the original input number.
        self.initial_order = range(1, count + 1)
        self.queue_hold.balls = list(self.initial_order)
        self.queue_hour.add(0)

    def run(self):
        """Start the ball clock to see how long it can keep track of days based upon the ball ordering.
        :return: The number of days since the order was repeated.
        :rtype: int
        """
        while True:
            self.count_minutes += 1
            a_ball = self.queue_hold.pop_fifo()
            self.queue_minutes.add(a_ball)
            if self.debug and self.debug_start <= self.count_minutes <= self.debug_end:
                print "COUN: {}".format(self.count_minutes)
            if self.initial_order == self.get_order():
                if self.debug:
                    print self.count_minutes
                break
            if self.debug and self.debug_start <= self.count_minutes <= self.debug_end:
                print "TIME: {}:{}{}".format(len(self.queue_hour.balls),
                                             len(self.queue_five_min.balls) * 5 / 10,
                                             len(self.queue_minutes.balls) + len(self.queue_five_min.balls) % 2 * 5)
                print
        return self.count_minutes / 1440

    def get_order(self):
        """Get the current order.
        :return: A list representing the current order of all the balls.
        """
        list_current_order = []
        list_current_order.extend(self.queue_hold.get_order())
        list_current_order.extend(self.queue_minutes.get_order())
        list_current_order.extend(self.queue_five_min.get_order())
        list_current_order.extend(self.queue_hour.get_order())
        if self.debug and self.debug_start <= self.count_minutes <= self.debug_end:
            print "HOLD: {}".format(self.queue_hold.get_order())
            print " MIN: {}".format(self.queue_minutes.get_order())
            print "FMIN: {}".format(self.queue_five_min.get_order())
            print "HOUR: {}".format(self.queue_hour.get_order())
            print "PHRS: {}".format(self.queue_hour.balls)
        return list_current_order


def main(input):
    """The main entry point for this script.
    :param balls: The number of balls in the ball clock machine.
    :type balls: int
    :return: The number of days that the clock represents unique time before a ball position is repeated.
    :rtype: int
    """

    try:
        count = int(input)
    except:
        raise ValueError ("'{}' is not valid input. Integers between 27 and 127 only. 0 to exit.".format(input))
    if count == 0:
        return 0
    if count < 27 or 127 < count:
        raise ValueError ("The number of balls ({}) to test must be between 27 and 127. 0 to exit.".format(count))

    the_clock = BallClock()
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


def test_input_2():
    """Ensure the program won't take an under range count for the balls."""
    with pytest.raises(ValueError):
        main(2)

def test_input_30():
    """The first example values given in the readme."""
    assert main(30) == 15


def test_input_45():
    """The second example values given in the readme."""
    assert main(45) == 378


def test_input_200():
    """Ensure the program won't take an under range count for the balls."""
    with pytest.raises(ValueError):
        main(200)


def test_input_foobar():
    """Ensure the program won't take an under range count for the balls."""
    with pytest.raises(ValueError):
        main("foobar")


if __name__ == '__main__':
    while True:
        user_input = raw_input()
        result = main(user_input)
        if result == 0:
            break
