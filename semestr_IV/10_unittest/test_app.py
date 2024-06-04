import unittest
from app import categoty_by_age

class TestCategotyByAge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("SetUpClass")
        print("="*30)

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass")
        print("=" * 30)

    def test_child(self):
        """Test fot 'Child'"""
        self.assertEqual(categoty_by_age(5),"Child")

    def test_teenager(self):
        """Test fot 'Teenager'"""
        self.assertEqual(categoty_by_age(14),"Teenager")

    def test_adult(self):
        self.assertEqual(categoty_by_age(28), "Adult")

    def test_golden_age(self):
        self.assertEqual(categoty_by_age(70), "Golden age")

    def test_negative_age(self):
        self.assertEqual(categoty_by_age(-1), "Invalid age: -1")

    def test_too_old(self):
        self.assertEqual(categoty_by_age(151),"Invalid age: 151")

    def test_child_teenager(self):
        self.assertEqual(categoty_by_age(9),"Child")
        self.assertEqual(categoty_by_age(10),"Teenager")

    def test_teenager_adult(self):
        self.assertEqual(categoty_by_age(18),"Teenager")
        self.assertEqual(categoty_by_age(19),"Adult")

    def test_adult_golden_age(self):
        self.assertEqual(categoty_by_age(65),"Adult")
        self.assertEqual(categoty_by_age(66),"Golden age")

if __name__=="__main__":
    unittest.main(verbosity=2)
