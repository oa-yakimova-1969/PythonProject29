import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


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


@pytest.fixture
def account():
    return 99998888777766665555

def test_get_mask_account(account):
    assert get_mask_account(account) == '**5555'
def test_get_mask_account_incorrect_length():
    assert get_mask_account(8888777766665555) == "Некорректный ввод"
def test_get_mask_account_incorrect_format():
    assert get_mask_account("Abcd@#$%;:[}<>?!") == "Некорректный ввод"
def test_get_mask_account_empty():
    assert get_mask_account("") == "Некорректный ввод"
