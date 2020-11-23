import unittest
from src.sample.app import Food

class test_for_app(unittest.TestCase):
    def setUp(self):
        self.tmp = Food()

    def test_getByName(self):
        self.assertEqual(self.tmp.getByName('Arrabiata')[0]['strMeal'], 'Spicy Arrabiata Penne')

    def test_getById(self):
        self.assertEqual(self.tmp.getById(52772)[0]['strCategory'], "Chicken")

    def test_listByLetter(self):
        self.assertEqual(len(self.tmp.listByLetter('a')), 2)

    def test_getByNameNotFound(self):
        self.assertEqual(self.tmp.getByName('Dziuzeppe'), None)

    def test_getByIdNotFound(self):
        self.assertEqual(self.tmp.getById(22222222), None)

    def test_listByLetterNotFound(self):
        self.assertEqual(self.tmp.listByLetter('z'), None)

    def test_getByNameException(self):
        with self.assertRaises(Exception):
            self.tmp.getByName(123)

    def test_getByIdException(self):
        with self.assertRaises(Exception):
            self.tmp.getById(True)

    def test_listByLetterType(self):
        with self.assertRaises(Exception):
            self.tmp.listByLetter(True)

    def test_listByLetterMore(self):
        with self.assertRaises(Exception):
            self.tmp.listByLetter('asd')

    def tearDown(self):
        self.tmp = None