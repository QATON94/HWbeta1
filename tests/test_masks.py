from src.masks import get_mask_card, returning_account_mask


def test_get_mask_card():
    assert get_mask_card('1234567890123456') == '1234 56** **** 3456'


def test_returning_account_mask():
    assert returning_account_mask('12345678901234567890') == '**7890'