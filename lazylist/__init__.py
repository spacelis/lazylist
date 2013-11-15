#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Author: SpaceLis
Email: Wen.Li@tudelft.nl
Github: http://github.com/spacelis
Description:
    A decoration class converting a generator to a lazy evaluated list.
"""
__author__ = 'wenli'


from functools import wraps


class LazyListWrapper(object):
    """ A wapper for each instance of lazylist

    """
    def __init__(self, generator):

        self._generator = generator
        self._cache = list()

    def __getitem__(self, item):
        if isinstance(item, int):
            try:
                return self._cache[item]
            except IndexError:
                for i in self._generator:
                    self._cache.append(i)
                    if len(self._cache) > item:
                        return self._cache[item]
        elif isinstance(item, slice):
            return [self[i] for i in range(item.start or 0, item.stop, item.step or 1)]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        pass

    def __contains__(self, item):
        pass

    def __delitem__(self):
        pass

    def __len__(self):
        pass

    def filtered(self, prop):
        """

        @type prop: the property that need to be held
        """
        @LazyList
        def dummy_generator():
            """ dummy """
            for i in self:
                if prop(i):
                    yield i
        return dummy_generator

    def __iter__(self, starting=0):
        """ Return an iterator of this sequence
        :returns: @todo

        """
        while True:
            yield self[starting]
            starting += 1


def LazyList(template):
    """ Wrapping a generator function to a list and will only
        evaluated when necessary.
    @param args:
    @param kwargs:
    @rtype : object
    """

    return LazyListWrapper(template())


def LazyListClass(template):
    """
    Return a function for creating a lazy list
    @return:
    """
    @wraps(template)
    def wrapper_aux(*args, **kwargs):

        """

        @param template: The generator to wrap
        @return:
        """
        return LazyListWrapper(template(*args, **kwargs))
    return wrapper_aux
