from django.test import TestCase
from .models import Item

class TestModels(TestCase):
 
    def test_done_defaults_to_false(self):
        # creates an item
        item = Item.objects.create(name='Test Todo Item')
        # confirms that its status = done by default is false
        self.assertFalse(item.done)


    def test_item_string_method_returns_name(self):
        # creates a test item
        item = Item.objects.create(name='Test Todo Item')
        # tests that the name is returned when it is rendered as a string
        self.assertEqual(str(item), 'Test Todo Item')

