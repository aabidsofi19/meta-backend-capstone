from django.test import TestCase
from rest_framework.response import Response 
from restaurant.views import MenuItemsView 
from restaurant.models import Menu 
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIRequestFactory 

factory = APIRequestFactory()

class MenuViewTest(TestCase) :
    
    def setUp(self) -> None:
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Salad", price=80, inventory=100)
        return super().setUp()

    def test_get_all(self) :
        request = factory.get("/restaurant/menu/items" , )
        response : Response   = MenuItemsView.as_view()(request,format="json")
        items = Menu.objects.all() 

        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data ,
                         MenuSerializer(items,many=True).data )

