import unittest
from classes.guest import Guest
from classes.bar import Bar

class TestGuest(unittest.TestCase):
    
    def setUp(self):

        self.guest_rich = Guest(100)
        self.guest_poor = Guest(5)

        self.drink = Bar("Tequila Sunrise", 7.50)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest_rich.cash)

    def test_rich_guest_can_buy_drink(self):
        self.guest_rich.buy_drink(self.drink)
        self.assertEqual(92.50, self.guest_rich.cash)

    def test_poor_guest_cant_buy_drink(self):
        self.guest_poor.buy_drink(self.drink)
        self.assertEqual(5, self.guest_poor.cash)


