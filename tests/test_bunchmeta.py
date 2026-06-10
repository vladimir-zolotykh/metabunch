import pytest
from bunchmeta import Bunch, BunchMeta


def test_defaults_are_assigned():
    class Point(Bunch):
        x = 1
        y = 2

    p = Point()

    assert p.x == 1
    assert p.y == 2


def test_keyword_arguments_override_defaults():
    class Point(Bunch):
        x = 1
        y = 2

    p = Point(x=10)

    assert p.x == 10
    assert p.y == 2


def test_multiple_keyword_arguments():
    class Point(Bunch):
        x = 1
        y = 2

    p = Point(x=10, y=20)

    assert p.x == 10
    assert p.y == 20


def test_unknown_keyword_argument_raises():
    class Point(Bunch):
        x = 1

    with pytest.raises(AttributeError, match="No slots left for"):
        Point(z=42)


def test_repr_of_default_instance():
    class Point(Bunch):
        x = 1
        y = 2

    assert repr(Point()) == "Point()"


def test_repr_shows_non_default_values():
    class Point(Bunch):
        x = 1
        y = 2

    assert repr(Point(x=10)) == "Point(x=10)"


def test_repr_shows_multiple_non_default_values():
    class Point(Bunch):
        x = 1
        y = 2

    assert repr(Point(x=10, y=20)) == "Point(x=10, y=20)"


def test_generated_slots():
    class Point(Bunch):
        x = 1
        y = 2

    assert Point.__slots__ == ["x", "y"]


def test_instances_have_no_dict():
    class Point(Bunch):
        x = 1

    p = Point()

    with pytest.raises(AttributeError):
        _ = p.__dict__


def test_custom_dunder_method_is_preserved():
    class Point(Bunch):
        x = 1

        def __str__(self):
            return "custom"

    assert str(Point()) == "custom"


@pytest.mark.parametrize("__name__", ["__init__", "__repr__", "__slots__"])
def test_overriding_generated_dunders_is_forbidden(__name__):
    namespace = {__name__: object()}

    with pytest.raises(AttributeError):
        BunchMeta("BadClass", (Bunch,), namespace)
