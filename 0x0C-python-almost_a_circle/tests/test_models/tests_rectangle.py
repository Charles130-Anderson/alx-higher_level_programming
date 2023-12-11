import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Rectangle class for testing
        self.rectangle = Rectangle(4, 5, 2, 3, 1)

    def test_attributes(self):
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_area_method(self):
        self.assertEqual(self.rectangle.area(), 4 * 5)

    def test_display_method(self):
        expected_output = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
            self.rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_method_with_args(self):
        self.rectangle.update(10, 8, 7, 6, 2)
        self.assertEqual(self.rectangle.id, 10)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 7)
        self.assertEqual(self.rectangle.x, 6)
        self.assertEqual(self.rectangle.y, 2)

    def test_update_method_with_kwargs(self):
        self.rectangle.update(width=10, height=8, x=7, y=6, id=2)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.height, 8)
        self.assertEqual(self.rectangle.x, 7)
        self.assertEqual(self.rectangle.y, 6)

    def test_to_dictionary_method(self):
        rectangle_dict = self.rectangle.to_dictionary()
        expected_dict = {
            "id": 1,
            "width": 4,
            "height": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(rectangle_dict, expected_dict)

    def test_string_representation(self):
        string_representation = str(self.rectangle)
        expected_string = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(string_representation, expected_string)

if __name__ == '__main__':
    unittest.main()
