import unittest
from src.sample.app import Food

class test_for_app(unittest.TestCase):
    def setUp(self):
        self.tmp = Food()

    def test_getByName(self):
        self.assertEqual(self.tmp.getByName('Arrabiata').strMeal, 'Spicy Arrabiata Penne')

    def tearDown(self):
        self.tmp = None