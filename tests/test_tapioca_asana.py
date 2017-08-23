# coding: utf-8

import unittest

from tapioca_asana import Asana


class TestTapiocaAsana(unittest.TestCase):

    def setUp(self):
        self.wrapper = Asana()


if __name__ == '__main__':
    unittest.main()
