from django.test import TestCase

class SetUpDatabase(TestCase):
    def setUp(self):
        print('setup')
    
    def test_call_console(self):
        print('console')

