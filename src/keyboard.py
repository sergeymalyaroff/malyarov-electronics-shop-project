from src.item import Item


class LanguageMixin:
    """
    Миксин для предоставления функционала изменения раскладки клавиатуры.
    """
    def __init__(self, language: str = 'EN') -> None:
        self.__language = language  # language стал приватным

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self):
        """
        Метод для изменения раскладки клавиатуры.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, LanguageMixin):
    """
    Класс для представления товара "клавиатура" в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN') -> None:
        Item.__init__(self, name, price, quantity)
        LanguageMixin.__init__(self, language)

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Keyboard.
        """
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, language='{self.language}')"

    def __str__(self):
        return self.name
