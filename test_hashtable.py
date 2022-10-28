# test_hashtable.py
import pytest
from hashtable import HashTable, BLANK


@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass


# Define a Custom HashTable Class
def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100


def test_should_create_empty_value_slots():
    # Given
    expected_values = [BLANK] * 3
    hash_table = HashTable(capacity=3)

    # When
    actual_values = hash_table.values

    # Then
    assert actual_values == expected_values


# Find a Value by Key
def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values


def test_should_not_grow_when_adding_elements():
    hash_table = HashTable(capacity=3)

    hash_table[1] = 1
    hash_table[2] = 4
    hash_table[3] = 9

    assert len(hash_table) == 3


def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values


def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert None in hash_table.values


# Find a Value by Key
