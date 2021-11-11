from django.test import TestCase # imports djangos test functionality
from .forms import ItemForm # imports our form


class TestItemForm(TestCase): # new class that inherits the test case functionality
    
    def test_item_name_is_required(self): # defines the test
        form = ItemForm({'name': ''}) # instantiates a form where the name has not been filled out
        self.assertFalse(form.is_valid()) # should show form is not valid
        # asserts if there is a 'name' key in the dictionary of errors that will be returned
        self.assertIn('name', form.errors.keys())
        # checks if the error message shown to the user matches what we expect
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_done_field_is_not_required(self):
        # creates a form with only a name 
        form = ItemForm({'name': 'Test Todo Item'})
        # should be valid as done not required
        self.assertTrue(form.is_valid())


        # Tests that only the field we specified in the forms.py metaclass will appear on the form
    def test_fields_are_explicit_in_form_metaclass(self):
        # this instantiates an empty form
        form = ItemForm()
        # fom meta fieldds == 'name' and 'done'
        self.assertEqual(form.Meta.fields, ['name', 'done'])


# python3 manage.py test todo.test_forms - would just run the tests on this page
# python3 manage.py test todo.test_forms.TestItemForm - would just run the specific class of tests
# python3 manage.py test todo.test_forms.TestItemForm.test_item_name_is_required - runs specifically the first test