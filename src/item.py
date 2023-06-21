import csv
from typing import List


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # уровень цен с учетом скидки
    all = []  # список для хранения всех созданных экземпляров

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name  # name стал приватным
        self.price = price
        self.quantity = quantity

        # добавление нового экземпляра в список
        self.__class__.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value[:10]  # оставляем только первые 10 символов

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.__class__.pay_rate

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Item.
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls, filename: str = '/Users/sergejmalarov/PycharmProjects/malyarov-electronics-shop-project/src/items.csv') -> List['Item']:
        cls.all = []  # Сброс списка all к пустому состоянию
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('name')
                price = cls.string_to_number(row.get('price'))
                quantity = cls.string_to_number(row.get('quantity'))
                cls(name, price, quantity)  # Инициализация нового экземпляра Item

    @staticmethod
    def string_to_number(s: str) -> float:
        try:
            return float(s)
        except ValueError:
            print("Invalid string for conversion to number.")
