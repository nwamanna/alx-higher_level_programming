#!/usr/bin/python3
""" Test for Rectangle Class """
import sys
import io
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ unit test for all methods in Rectangle """
    @classmethod
    def setUpClass(cls):
        cls._Base__nb_objects = 90
        cls.r1 = Rectangle(10, 2)
        cls.num = Rectangle._Base__nb_objects
        cls.r2 = Rectangle(5, 6, 2, 3, 12)
        print(f'this is {cls.r1.id} instance')

    @classmethod
    def tearDownClass(cls):
        Base._Base__nb_objects = 0
        cls.r1 = None
        print(cls.r1)
        cls.r2 = None
        print("Tearing down")

    def test_init(self):
        self.assertEqual(self.r1.id, self.num)
        self.assertEqual(self.r2.id, 12)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 6)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 3)

    def test_width(self):
        with self.assertRaises(ValueError):
            self.r1.width = 0
            self.r1.x = -6
        with self.assertRaises(TypeError):
            self.r1.width = "width"
            self.r1.x = "x"

    def test_area(self):
        self.assertTrue(self.r1.area(), 20)
        self.assertTrue(self.r2.area(), 30)

    def test_display(self):
        with io.StringIO() as f:
            sys.stdout = f
            self.r1.display()
            sys.stdout = sys.__stdout__
            self.assertTrue(f.getvalue(), "####################")

    def test_str(self):
        str1 = "[Rectangle] (1) 0/0 - 10/2"
        with io.StringIO() as buf:
            sys.stdout = buf
            print(self.r1)
            sys.stdout = sys.__stdout__
            self.assertTrue(buf.getvalue(), str1)

    def test_update(self):
        self.r1.update(89)
        self.r2.update(67)
        self.assertTrue(self.r1.id, 89)
        self.assertTrue(self.r2.id, 67)
        
    def test_to_dictionary(self):
        instance_dict = self.r1.to_dictionary()
        self.assertTrue(type(instance_dict), dict)
