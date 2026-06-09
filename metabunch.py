#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class BunchMeta(type):

    def __new__(mcls, clsname, bases, clsdict):
        defaults = {}
        slots = []
        d = dict(clsdict)
        slots = ["x", "y", "color", "__init__", "__repr__"]
        for key, val in clsdict.items():
            pass

        def init(cls, **kwds):
            for k, v in defaults:
                setattr(cls, k, v)

        def repr(cls):
            print(defaults)

        d = dict(__slots__=slots, __init__=init, __repr__=repr)
        return super().__new__(mcls, clsname, bases, d)


class Bunch(metaclass=BunchMeta):
    pass


class Point(Bunch):
    x = 2.3
    y = 4.6
    color = "gray"


if __name__ == "__main__":
    p = Point()
    Point(x=11.2, y=12.3, color="yellow")
