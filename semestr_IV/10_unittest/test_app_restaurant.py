import unittest
from unittest.mock import patch
from app_restaurant import Restaurant,IceCreamStand
from io import StringIO

class TestRastaurant(unittest.TestCase):
    """Тетстування класу Reastaurant"""

    @classmethod
    def setUp(self):
        self.restaurant=Restaurant("Липа", "українська")

    def capture_ouput(self,func,*args,**kwargs):
        with patch('sys.stdout',new_callable=StringIO) as mock_stdout:
            func(*args,**kwargs)
            return  mock_stdout.getvalue()

    def test_reastaurant_creation(self):
        self.assertEqual(self.restaurant.restaurant_name,"Липа")
        self.assertEqual(self.restaurant.cuisine_type,"українська")
        self.assertEqual(self.restaurant.number_served,0)

    def  test_describe_restaurant(self):
        output_text=("Ресторан 'Липа' пропонує кухню типу 'українська'.\n")
        output=self.capture_ouput(self.restaurant.describe_restaurant)
        self.assertEqual(output,output_text)

    # def test_open_restaurant(self):
    #     pass
    def test_open_restaurant(self):
        output_text = ("Ресторан 'Липа' відкритий!\n")
        output = self.capture_ouput(self.restaurant.open_restaurant)
        self.assertEqual(output, output_text)

    def test_set_number_served(self):
        self.restaurant.set_number_served(4)
        self.assertEqual(self.restaurant.number_served,4)

    def test_increment_number_served(self):
        self.restaurant.increment_number_served(4)
        self.assertEqual(self.restaurant.number_served, 4) # 4==4


if __name__=="__main__":
    unittest.main(verbosity=2)