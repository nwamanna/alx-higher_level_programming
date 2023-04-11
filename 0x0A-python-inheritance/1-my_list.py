#!/usr/bin/python3
""" Subclass of list """


class MyList(list):
    """ a subclass of list that can arrange in ascending order """
    def print_sorted(self):
        """ prints list in ascending order """
        sort = sorted(self)
        print(sort)
