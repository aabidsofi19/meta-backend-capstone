from django.test import TestCase
from restaurant.models import Menu , Booking 


class MenuItemTest(TestCase) :
    def test_string_representation(self) :
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
