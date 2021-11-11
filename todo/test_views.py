from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    def test_get_todo_list(self):
        # sets the page we want to test (home)
        response = self.client.get('/')
        # tests if the response code on the home page is equal to 200 (successful http response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # sets the page we want to test 
        response = self.client.get('/add')
        # tests if the response code on the home page is equal to 200 (successful http response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')



    def test_get_edit_item_page(self):
        # Creates an item object to use in our test
        item = Item.objects.create(name='Test Todo Item')
        # sets the page we want to test, uses a python f string so that {item.id} is interpreted and added as part of the string
        response = self.client.get(f'/edit/{item.id}')
        # tests if the response code on the home page is equal to 200 (successful http response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        # response set to replicate that a new item has just been added
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # if it is added successfully it should redirect to the homepage
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        # Creates an item object to use in our test
        item = Item.objects.create(name='Test Todo Item')
        # sets the page we want to test, uses a python f string so that {item.id} is interpreted and added as part of the string
        response = self.client.get(f'/delete/{item.id}')
         # if it is added successfully it should redirect to the homepage
        self.assertRedirects(response, '/')
        # To test this further set existig_items = what is left in the db
        existing_items = Item.objects.filter(id=item.id)
        # Tests if it is equal to 0
        self.assertEqual(len(existing_items), 0)



    def test_can_toggle_item(self):
        # Creates an item object to use in our test
        item = Item.objects.create(name='Test Todo Item', done=True)
        # sets the page we want to test, uses a python f string so that {item.id} is interpreted and added as part of the string
        response = self.client.get(f'/toggle/{item.id}')
         # if it is added successfully it should redirect to the homepage
        self.assertRedirects(response, '/')
        # sets the updated item
        updated_item = Item.objects.get(id=item.id)
        # check the status of the upadated item, should be false as we have updated it above
        self.assertFalse(updated_item.done)


    def test_can_edit_item(self):
        # Creates an item object to use in our test
        item = Item.objects.create(name='Test Todo Item')
        # sets the page we want to test, uses a python f string so that {item.id} is interpreted and added as part of the string
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # if it is added successfully it should redirect to the homepage
        self.assertRedirects(response, '/')
        # sets the updated item
        updated_item = Item.objects.get(id=item.id)
        # Tests that the updated names are equal
        self.assertEqual(updated_item.name, 'Updated Name')
