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
        self.name = name
        self.price = price
        self.quantity = quantity

        # добавление нового экземпляра в список
        self.__class__.all.append(self)

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
        return f"Item('{self.name}', {self.price}, {self.quantity})"
