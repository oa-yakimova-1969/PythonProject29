import pytest
rom src.widget import mask_account_card


@pytest.mark.parametrize("input_string, expected_string", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Master Card 7158300734726758", "Master Card 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305")
])


def test_mask_account_card(input_string, expected_string):
    assert mask_account_card(input_string) == expected_string


def test_mask_account_card_incorrect():
    assert mask_account_card("9999888877776666") == "Ошибка: некорректный ввод."
    assert mask_account_card("Счет") == "Ошибка: некорректный ввод."


def test_mask_account_card_empty():
    assert mask_account_card("") == "Ошибка: некорректный ввод."

