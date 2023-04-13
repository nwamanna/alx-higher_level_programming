#!/usr/bin/python3
""" contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object: """


def class_to_json(obj):
    """ returns dictionary description for JSON serialization """
    serial_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serial_dict[key] = value
    return serial_dict
