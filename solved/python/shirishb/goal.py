#! /usr/bin/env python

# No unique solution. :-(

from __future__ import print_function

## Approach # 1 (function + global)
"""
count=0

def g(*args):
    global count
    count += 1
    if len(args) == 1:
        oos = "".join(["o" for x in range(count-1)])
        count = 0
        return "g" + oos + args[0]
    return g
"""
## Approach # 2 (function + attribute)
"""
def g(*args):
    if not hasattr(g, "count"):
        g.count = 0
    g.count += 1
    if len(args) == 1:
        oos = "".join(["o" for x in range(g.count-1)])
        g.count = 0
        return "g" + oos + args[0]
    return g
"""
## Approach # 3 (class)
"""
class Goal():
    def __init__(self, *arg):
        self.string = "g"

    def __call__(self, *arg):
        if len(arg) ==1:
            str = self.string + arg[0]
            self.string = "g"
            return str
        else:
            self.string+="o"
            return self
g = Goal()
"""
## Approach # 4 (lambda function)
"""
TODO
"""
## Approach # 5 (function + default value)
def g(al = None, go=["g"]):
    if al == None:
        go.append("o")
        return g
    else:
        goal = "".join(go) + al
        go[:] = ["g"]
        return goal

## Test
print(g('al'))
print(g()('al'))
print(g()()('al'))
print(g()()()()()()()()()()('al'))
