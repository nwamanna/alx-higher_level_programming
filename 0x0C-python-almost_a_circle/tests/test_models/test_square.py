#!/usr/bin/python3
""" Test for Square Class """
import sys
import io
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ unit test for all methods in Square """
    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(5)
        cls.num = Square._Base__nb_objects
        cls.s2 = Square(3, 1, 3, 7)
        print(f'this is {cls.s1.id} instance')

    @classmethod
    def tearDownClass(cls):
        Base._Base__nb_objects = 0
        cls.s1 = None
        print(cls.s1)
        cls.s2 = None
        print("Tearing down")

    def test_init(self):
        self.assertEqual(self.s1.id, self.num)
        self.assertEqual(self.s2.id, 7)
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 3)
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 9)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 1)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 3)

    def size(self):
        with self.assertRaises(ValueError):
            self.s1.size = 0
            self.s1.x = -6
        with self.assertRaises(TypeError):
            self.s1.size = "width"
            self.s1.x = "x"

    def test_str(self):
        str1 = "[Square] (1) 0/0 - 5"
        with io.StringIO() as buf:
            sys.stdout = buf
            print(self.s1)
            sys.stdout = sys.__stdout__
            self.assertTrue(buf.getvalue(), str1)

    def test_update(self):
        self.s1.update(89)
        self.s2.update(67)
        self.assertTrue(self.s1.id, 89)
        self.assertTrue(self.s2.id, 67)

    def test_to_dictionary(self):
        instance_dict = self.s1.to_dictionary()
        self.assertTrue(type(instance_dict), dict)
