"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item, InstantiateCSVError
from pathlib import Path
import os

def test_item_creation():
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20

def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000

def test_apply_discount():
    Item.pay_rate = 0.8  # устанавливаем новый уровень цен
    item = Item("Смартфон", 10000, 20)
    item.apply_discount()
    assert item.price == 8000.0

def test_all_items_list():
    Item.all = []  # очищаем список перед тестом
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1 in Item.all
    assert item2 in Item.all



def setup_module(module):
    """
    Функция выполняется перед началом тестирования всего модуля.
    Она будет очищать список 'all' перед началом тестов.
    """
    Item.all = []



def test_instantiate_from_csv_no_file():
    # Проверяем обработку ошибки при отсутствующем файле
    filename = 'non_existing_file.csv'
    with pytest.raises(FileNotFoundError, match=r"Отсутствует файл items.csv"):
        Item.instantiate_from_csv(filename)





