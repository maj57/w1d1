#!/usr/bin/env python3

def function2(some_input):
    for i in some_input:
        print(i)
    return ''


def function1(some_input):
    return function2(some_input)


print(function1(['a','b','c','d']))
