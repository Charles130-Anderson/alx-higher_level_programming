import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Square class for testing
        self.square = Square(5, 2, 3, 1)

    def test_attributes(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_update_method_with_args(self):
        self.square.update(10, 8, 7, 6)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.x, 7)
        self.assertEqual(self.square.y, 6)

    def test_update_method_with_kwargs(self):
        self.square.update(size=10, x=8, y=7, id=6)
        self.assertEqual(self.square.id, 6)
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 8)
        self.assertEqual(self.square.y, 7)

    def test_to_dictionary_method(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square_dict, expected_dict)

    def test_string_representation(self):
        string_representation = str(self.square)
        expected_string = "[Square] (1) 2/3 - 5"
        self.assertEqual(string_representation, expected_string)

if __name__ == '__main__':
    unittest.main()
