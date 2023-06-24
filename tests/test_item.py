"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

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


def test_instantiate_from_csv():
    """
    Тестирование метода instantiate_from_csv
    """
    Item.instantiate_from_csv()

    # Проверка, что было создано правильное количество экземпляров
    assert len(Item.all) == 5  # Измените на количество строк в вашем файле CSV

    # Проверка, что первый экземпляр был правильно инициализирован
    assert Item.all[0].name == 'Смартфон'  # Измените на значения из вашего файла CSV
    # Добавьте дополнительные проверки для других атрибутов и экземпляров, если нужно


def test_string_to_number():
    """
    Тестирование метода string_to_number
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5
    assert Item.string_to_number('0') == 0


def test_item_repr():
    item = Item('Смартфон', 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000.0, 20)"

def test_item_str():
    item = Item('Смартфон', 10000, 20)
    assert str(item) == 'Смартфон'