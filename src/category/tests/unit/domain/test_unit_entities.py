import unittest
from dataclasses import is_dataclass
from datetime import datetime

from src.category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        created_at = datetime.now()
        category = Category(
            name='Movie',
            description='some description',
            is_active=False,
            created_at=created_at
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, False)
        self.assertEqual(category.created_at, created_at)

        category = Category(name='Movie')
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_if_created_at_is_generated_in_constructor(self):
        category_1 = Category(name='Movie 1')
        category_2 = Category(name='Movie 2')
        self.assertNotEqual(category_1.created_at.timestamp(), category_2.created_at.timestamp())

