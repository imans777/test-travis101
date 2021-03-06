from unittest import TestCase
import sqlite3
import os
from flask import Response
db = sqlite3.connect(
    os.path.join(
        os.path.dirname(__file__),
        '.'.join(['database', 'db'])
    ),
    check_same_thread=False,
    isolation_level=None
)
db.cursor().execute(''' CREATE TABLE IF NOT EXISTS TestTable(name TEXT) ''')
db.cursor().execute(''' INSERT INTO TestTable(name) VALUES ('iman') ''')
db.cursor().execute(''' SELECT name FROM TestTable ''')
print('->> this is the selected test table: ', db.cursor().fetchall())


class f1(TestCase):
    def setUp(self):
        print('init setup f1')

    def test_number_one(self):
        self.assertEqual(2, 2)
        print('this is a sample test')


from ddt import ddt, data, unpack


@ddt
class DDT_TEST(TestCase):
    def setUp(self):
        print('before everything')

    def normal_func(self):
        print('this is normal func')
        self.assertFalse(False)

    @data(1, 2, 3, 4)
    def test_ddt_1(self, value):
        print("HEELLOOOOOOOOOOOOOOOOOOOOOOOOOOO:")
        self.assertLess(value, 5)

    @data([1, 2], [3, 4])
    def test_ddt_2(self, value):
        print('THIS IS VALUE: ', value)
        self.assertIn(value, [[1, 2], [3, 4]])

    @data([2, 5], [1, 4])
    @unpack
    def test_ddt_3(self, first, second):
        print('first and second: ', first, second)
        self.assertLess(first, second)

    @data({'a': 'b'}, {'c': 'd'})
    def test_ddt_4(self, value):
        print('dict value: ', value)
