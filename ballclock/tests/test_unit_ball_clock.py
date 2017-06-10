import theclock


def test_unit_ball_clock_load():
    """Verify that a load of balls actually puts them in the hold queue."""
    my_clock = theclock.BallClock.BallClock()
    my_clock.load(45)
    assert my_clock.queue_hold.balls == range(1, 46) and my_clock.queue_hour.balls == [0]


def test_unit_ball_clock_get_order():
    """Ensure that the order returned by a load of balls is accurate."""
    my_clock = theclock.BallClock.BallClock()
    my_clock.load(45)
    assert my_clock.get_order() == range(1, 45 + 1)
