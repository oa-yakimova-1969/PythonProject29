import pytest
from src.masks import get_mask_card_number



@pytest.fixture
def card_number():
    return 9999888877776666

def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '9999 88** **** 6666'
def test_get_mask_card_number_incorrect_length():
    assert get_mask_card_number(888877776666) == "Некорректный ввод"
def test_get_mask_card_number_incorrect_format():
    assert get_mask_card_number("Abcd@#$%;:[}") == "Некорректный ввод"
def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == "Некорректный ввод"