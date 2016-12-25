#!/usr/bin/python
import operator


def sort_a_list(l):
    getcount = itemgetter(1)
    sorted(l, key=getcount)


def sort_by_mark(l):
    getcount = itemgetter(1)
    map(getcount, l)
    sorted(l, key=getcount)


def sort_by_name(l):
    itemgetter(item)
