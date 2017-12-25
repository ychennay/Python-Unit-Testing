from models.item import ItemModel
from tests.unit.unit_base_test import UnitBaseTest


class ItemTest(UnitBaseTest):
    def setUp(self):
        self.item = ItemModel('car', 4.99, 1)

    def test_create_item(self):
        self.assertIsInstance(self.item, ItemModel)
        self.assertEqual(self.item.name, 'car')
        self.assertEqual(self.item.price, 4.99)
        self.assertEqual(self.item.store_id, 1)
        self.assertIsNone(self.item.store)

    def test_item_json(self):
        self.assertDictEqual(self.item.json(), {'name':
                                                    'car',
                                                'price':
                                                    4.99})
