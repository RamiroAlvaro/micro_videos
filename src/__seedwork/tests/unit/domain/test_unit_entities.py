import unittest
from abc import ABC
from dataclasses import is_dataclass, dataclass

from src.__seedwork.domain.entities import Entity
from src.__seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, kw_only=True)
class StubEntity(Entity):
    prop_1: str
    prop_2: str


class TestEntityUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_unique_entity_id_and_props(self):
        entity = StubEntity(prop_1='value_1', prop_2='value_2')
        self.assertEqual(entity.prop_1, 'value_1')
        self.assertEqual(entity.prop_2, 'value_2')
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(entity.unique_entity_id.id, entity.id)

    def test_accept_a_valid_uuid(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                id='8635ef94-1a9b-486b-a7cc-d1d0ab416fb5'),
            prop_1='value_1',
            prop_2='value_2'
        )
        self.assertEqual(entity.id, '8635ef94-1a9b-486b-a7cc-d1d0ab416fb5')

    def test_to_dict_method(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                id='8635ef94-1a9b-486b-a7cc-d1d0ab416fb5'),
            prop_1='value_1',
            prop_2='value_2'
        )
        self.assertDictEqual(entity.to_dict(), {
            'id': '8635ef94-1a9b-486b-a7cc-d1d0ab416fb5',
            'prop_1': 'value_1',
            'prop_2': 'value_2'
        })
