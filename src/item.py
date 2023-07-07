import csv
from typing import List
from pathlib import Path

class InstantiateCSVError(Exception):
    """
    Исключение, возникающее при попытке инстанцировать объекты Item из поврежденного CSV-файла.
    """
    pass

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

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Операция сложения доступна только для экземпляров класса Item.")

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Item.
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, filename: str = 'items.csv') -> List['Item']:

        cls.all = []  # Сброс списка all к пустому состоянию
        base_path = Path(__file__).parent  # определение пути к файлу, где находится данный скрипт
        file_path = (base_path / filename).resolve()  # объединение пути к скрипту и имени файла

        try:
            with file_path.open('r', encoding='windows-1251') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл items.csv поврежден")

                    name = row.get('name')
                    price = cls.string_to_number(row.get('price'))
                    quantity = cls.string_to_number(row.get('quantity'))
                    cls(name, price, quantity)  # Инициализация нового экземпляра Item

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(s: str) -> float:
        try:
            return float(s)
        except ValueError:
            print("Invalid string for conversion to number.")
