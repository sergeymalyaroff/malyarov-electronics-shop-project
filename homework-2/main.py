from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    try:
        item.name = 'СуперСмартфон'
    except Exception as e:
        print(e)

    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]

    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5
