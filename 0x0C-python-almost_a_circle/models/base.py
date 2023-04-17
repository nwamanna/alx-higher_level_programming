#!/usr/bin/python3
""" This module contains a class Base """
import json
import os


class Base:
    """ Parent class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def BaseInstance():
        return Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(str(cls.__name__) + ".json", "w", encoding="utf-8") as f:
                f.write("[]")
        else:
            list_dic = []
            for ins in list_objs:
                new_dict = ins.to_dictionary()
                list_dic.append(new_dict)
            with open(str(cls.__name__) + ".json", "w", encoding="utf-8") as f:
                word = Base.to_json_string(list_dic)
                f.write(word)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_ins = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_ins = cls(1)
        else:
            raise TypeError("not a class")
        dummy_ins.update(**dictionary)
        return dummy_ins

    @classmethod
    def load_from_file(cls):
        obj_list = []
        if not os.path.exists(str(cls.__name__) + ".json"):
            return []
        with open(str(cls.__name__) + ".json", encoding="utf-8") as f:
            json_dict = f.read()
            list_dict = cls.from_json_string(json_dict)
            for ins_dict in list_dict:
                instance = cls.create(**ins_dict)
                obj_list.append(instance)
            return obj_list
