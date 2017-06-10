import pytest
import theclock


def test_unit_ball_queue_add_one():
    """Verify that if one ball is added using the add function, it's actually added."""
    min_queue = theclock.BallClock.Queue.Queue(4, 0)
    min_queue.add(2193)
    assert min_queue.balls == [2193]


def test_unit_ball_queue_add_five():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 0)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    assert min_queue.balls == list_balls


def test_unit_ball_queue_add_one_with_placeholder():
    """Verify that if one ball is added using the add function, it's actually added."""
    min_queue = theclock.BallClock.Queue.Queue(4, 1)
    min_queue.add(2193)
    assert min_queue.balls == [2193] and min_queue.get_order() == []


def test_unit_ball_queue_add_five_with_placeholder():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 1)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    assert min_queue.balls == list_balls and min_queue.get_order() == list_balls[1:]


def test_unit_ball_queue_add_five_pop_lifo_once():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 0)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_lifo())
    assert pop_out == list_balls[-1:]


def test_unit_ball_queue_add_five_pop_lifo_all():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 0)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    assert pop_out == list(reversed(list_balls))


def test_unit_ball_queue_add_five_placeholder_pop_lifo_all():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 1)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_lifo())
    with pytest.raises(Exception):
        pop_out.append(min_queue.pop_lifo())


def test_unit_ball_queue_add_five_pop_fifo_once():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 0)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_fifo())
    assert pop_out == list_balls[:1]


def test_unit_ball_queue_add_five_pop_fifo_all():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 0)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    assert pop_out == list_balls


def test_unit_ball_queue_add_five_placeholder_pop_fifo_all():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 1)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_fifo())
    with pytest.raises(Exception):
        pop_out.append(min_queue.pop_fifo())


def test_unit_ball_queue_add_five_pop_mix_all():
    """Verify that if five balls are added using the add function, they're actually added."""
    min_queue = theclock.BallClock.Queue.Queue(10, 0)
    list_balls = [2183, 4929, 11, 32932, 32]
    for num in list_balls:
        min_queue.add(num)
    pop_out = []
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_fifo())
    pop_out.append(min_queue.pop_lifo())
    pop_out.append(min_queue.pop_fifo())
    assert pop_out == [2183, 32, 4929, 32932, 11]


