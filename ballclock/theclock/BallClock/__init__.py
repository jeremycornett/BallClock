"""
Author:      Jeremy Cornett
Date:        06/07/2017
"""

import theclock.BallClock.Queue


class BallClock(object):
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
        self.queue_hold = theclock.BallClock.Queue.Queue(127, 0)
        self.queue_hour = theclock.BallClock.Queue.Queue(12, 1, queue_full_first=self.queue_hold,
                                                         queue_full_remain=self.queue_hold)
        self.queue_five_min = theclock.BallClock.Queue.Queue(11, 0, queue_full_first=self.queue_hour,
                                                             queue_full_remain=self.queue_hold)
        self.queue_minutes = theclock.BallClock.Queue.Queue(4, 0, queue_full_first=self.queue_five_min,
                                                            queue_full_remain=self.queue_hold)
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
