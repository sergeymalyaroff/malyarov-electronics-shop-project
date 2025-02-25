from src.item import Item

class Phone(Item):
    """
    Класс для представления телефона в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, sim_cards: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param sim_cards: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__sim_cards = None
        self.sim_cards = sim_cards

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Phone.
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.sim_cards})"

    @property
    def sim_cards(self):
        return self.__sim_cards

    @sim_cards.setter
    def sim_cards(self, sim_cards):
        if sim_cards <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__sim_cards = sim_cards
