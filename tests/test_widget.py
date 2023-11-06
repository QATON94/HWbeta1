import pytest

from src.widget import get_data, get_mask_cards_and_accounts


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_get_mask_cards_and_accounts(info, expected):
    assert get_mask_cards_and_accounts(info) == expected


def test_get_data():
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"
