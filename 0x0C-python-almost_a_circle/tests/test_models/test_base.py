#!/usr/bin/python3
""" Test for Base Class """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ unit test for all methods in Base """
    @classmethod
    def setUpClass(cls):
        cls.base1 = Base()
        cls.base2 = Base(6)
        cls.r1 = Rectangle(10, 7, 2, 8)
        cls.r2 = Rectangle(2, 4)

    @classmethod
    def tearDownClass(cls):
        _Base__nb_objects = 0
        cls.base1 = None
        cls.base2 = None
        cls.r1 = None
        cls.r2 = None
        print("Tearing down")

    def test_init(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 6)
	
    def test_to_json_string(self):
        dictionary = self.r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        assert type(json_dictionary) == str

    def test_save_to_file(self):
        Rectangle.save_to_file([self.r1, self.r2])
        self.assertTrue(os.path.exists('Rectangle.json'))

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        assert type(list_output) == list

    def test_create(self):
        r1_dictionary = self.r1.to_dictionary()
        new_r = Rectangle.create(**r1_dictionary)
        assert self.r1 != new_r

    def load_from_file(self):
        list_rectangles_input = [self.r1, self.r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output), list)
        self.assertTrue(type(list_rectangles_output[0]), Rectangle)
