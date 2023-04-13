#!/usr/bin/python3
""" This module contains a class Students """


class Student:
    """ Student class contains a method that
    retuns a dictionary JSON serializable """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        serial_dict = {}
        for key, value in self.__dict__.items():
            test = isinstance(value, (list, dict, str, int, bool))
            if attrs is not None:
                if key in attrs and test:
                    serial_dict[key] = value
            else:
                if isinstance(value, (list, dict, str, int, bool)):
                    serial_dict[key] = value
        return serial_dict
