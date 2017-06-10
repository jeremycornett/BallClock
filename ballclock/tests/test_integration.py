import pytest
import theclock

def test_integration_input_2():
    """Ensure the program won't take an under range count for the balls."""
    with pytest.raises(ValueError):
        theclock.main(2)


def test_integration_input_30():
    """The first example values given in the readme."""
    assert theclock.main(30) == 15


def test_integration_input_45():
    """The second example values given in the readme."""
    assert theclock.main(45) == 378


def test_integration_input_200():
    """Ensure the program won't take an under range count for the balls."""
    with pytest.raises(ValueError):
        theclock.main(200)


def test_integration_input_foobar():
    """Ensure the program won't take an under range count for the balls."""
    with pytest.raises(ValueError):
        theclock.main("foobar")

