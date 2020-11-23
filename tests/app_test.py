import unittest
from src.sample.app import Food

class test_for_app(unittest.TestCase):
    def setUp(self):
        self.tmp = Food()

    def test_getByName(self):
        self.assertEqual(self.tmp.getByName('Arrabiata')[0]['strMeal'], 'Spicy Arrabiata Penne')

    def test_getById(self):
        self.assertEqual(self.tmp.getById('52772')[0]['strIngredient1'], "penne rigate")

    def tearDown(self):
        self.tmp = None