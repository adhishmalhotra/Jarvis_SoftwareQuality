import unittest

import typing_test


class TestTimer(unittest.TestCase):


    def test_formattime(self):

        result = typing_test.format_time(180)
        self.assertEqual(result, '03:00')