#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class MyMeta(type):
    def __str__(cls):
        return "Beautiful class '%s'" % cls.__name__


class MyClass:
    __metaclass__ = MyMeta


x = MyClass()
print(type(x))
# emits: Beautiful class 'MyClass'
