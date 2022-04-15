import unittest
import uuid
from abc import ABC
from dataclasses import is_dataclass, FrozenInstanceError, dataclass
from unittest.mock import patch

from src.__seedwork.domain.exceptions import InvalidUuidException
from src.__seedwork.domain.value_objects import UniqueEntityId, ValueObject


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop_1: str
    prop_2: str


class TestValueObjectUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        vo_1 = StubOneProp(prop='value')
        self.assertEqual(vo_1.prop, 'value')

        vo_2 = StubTwoProp(prop_1='value_1', prop_2='value_2')
        self.assertEqual(vo_2.prop_1, 'value_1')
        self.assertEqual(vo_2.prop_2, 'value_2')

    def test_convert_to_string(self):
        vo_1 = StubOneProp(prop='value')
        self.assertEqual(vo_1.prop, str(vo_1))

        vo_2 = StubTwoProp(prop_1='value_1', prop_2='value_2')
        self.assertEqual(
            '{"prop_1": "value_1", "prop_2": "value_2"}', str(vo_2))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = StubOneProp(prop='value')
            value_object.prop = 'fake'


class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
                UniqueEntityId,
                '_UniqueEntityId__validate',
                autospec=True,
                side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId(id='fake id')
            mock_validate.assert_called_once()
            self.assertEqual(
                assert_error.exception.args[0], 'ID must be a valid UUID')

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
                UniqueEntityId,
                '_UniqueEntityId__validate',
                autospec=True,
                side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            value_object = UniqueEntityId(
                id='ac12a9c5-e73a-4751-a5dc-49e3679b3614')
            mock_validate.assert_called_once()
            self.assertEqual(
                value_object.id, 'ac12a9c5-e73a-4751-a5dc-49e3679b3614')

            uuid_value = uuid.uuid4()
            value_object = UniqueEntityId(id=uuid_value)
            self.assertEqual(value_object.id, str(uuid_value))

    def test_generate_id_when_no_passed_id_in_constructor(self):
        with patch.object(
                UniqueEntityId,
                '_UniqueEntityId__validate',
                autospec=True,
                side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            value_object = UniqueEntityId()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = 'fake id'

    def test_convert_to_str(self):
        value_object = UniqueEntityId(
            id='ac12a9c5-e73a-4751-a5dc-49e3679b3614')
        self.assertEqual(str(value_object),
                         'ac12a9c5-e73a-4751-a5dc-49e3679b3614')
