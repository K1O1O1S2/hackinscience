#!/usr/bin/python
import operator


def sort_a_list(l):
    getcount = operator.itemgetter(1)
    sorted(l, key=getcount)


def sort_by_mark(l):
    getcount = operator.itemgetter(1)
    map(getcount, l)
    sorted(l, key=getcount)


def sort_by_name(l):
    operator.itemgetter(item)
