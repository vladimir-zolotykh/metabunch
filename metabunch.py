#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class BunchMeta(type):

    def __new__(mcls, clsname, bases, clsdict):
        defaults = {}
        slots = []
        # d = dict(clsdict)
        # slots = ["x", "y", "color"]
        for key, val in clsdict.items():
            if not (key.startswith("__") and key.endswith("__")):
                defaults[key] = val
        slots = defaults
        # if clsname == "Point":
        #     print(f"{defaults = }")

        def init(cls, **kwds):
            for k, v in kwds.items():
                setattr(cls, k, v)

        def repr(cls):
            # print(defaults)
            return ", ".join(f"{k}={v!r}" for k, v in defaults.items())

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
    # print(p.x)
    p = Point(x=11.2, y=12.3, color="yellow")
    print(p.x)
    print(repr(p))
