class Queue:
    """Create the ball queue and the default behavior of such a ball queue."""

    def __init__(self, max, placeholders, queue_full_first=None, queue_full_remain=None):
        """Initialize the ball queue with the given information.
        :param maximum: The maximum number of balls the queue can hold.
        :type maximum: int
        :param placeholders: The total number of balls that have to go in placeholders for this queue.
        :type placeholders: int
        :param queue_full_first: The queue which gets a single ball LIFO from this queue.
        :type queue_full_first: Queue
        :param queue_full_remain: The queue which gets the remainder balls LIFO from this queue.
        :type queue_full_remain: Queue
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


