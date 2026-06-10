#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class BunchMeta(type):

    def __new__(mcls, clsname, bases, clsdict):
        defaults = {}
        dunders = {}
        for key, val in clsdict.items():
            if key[:2] == "__" and key[-2:] == "__":
                dunders[key] = val
            else:
                defaults[key] = val

        def init(cls, **kwds):
            for k in defaults:
                v = kwds.pop(k, defaults[k])
                setattr(cls, k, v)
            if kwds:
                unused = ", ".join(kwds)
                raise AttributeError(f"No slots left for {unused}")

        def repr(cls):
            s = ", ".join(
                f"{k}={getattr(cls, k)!r}"
                for k in defaults
                if getattr(cls, k) != defaults[k]
            )
            return f"{clsname}({s})"

        d = dict(__slots__=list(defaults), __init__=init, __repr__=repr)
        forbidden = d.keys() & dunders.keys()
        if forbidden:
            raise AttributeError(f"{', '.join(forbidden)} must not be overridden")
        d.update(dunders)
        return super().__new__(mcls, clsname, bases, d)


class Bunch(metaclass=BunchMeta):
    pass


class Point(Bunch):
    x = 2.3
    y = 4.6
    color = "gray"


if __name__ == "__main__":
    p = Point()
    # print(p.x, p.y, p.color)
    p = Point(x=11.2, y=12.3, color="yellow")
    print(p.x)
    print(repr(p))
