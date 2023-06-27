# tests/test_phone.py

import pytest
from src.phone import Phone
from src.item import Item

def test_create_phone():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.sim_cards == 2

def test_add_phone_and_item():
    phone = Phone("iPhone 14", 120000, 5, 2)
    item = Item("Смартфон", 10000, 20)
    assert phone + item == 25

def test_add_two_phones():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    phone2 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1 + phone2 == 10

def test_invalid_sim_cards():
    with pytest.raises(ValueError) as e_info:
        phone = Phone("iPhone 14", 120000, 5, 0)
    assert str(e_info.value) == "Количество физических SIM-карт должно быть целым числом больше нуля."
