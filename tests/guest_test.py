import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):

        self.guest_rich = Guest(100)
        self.guest_poor = Guest(5)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest_rich.cash)

