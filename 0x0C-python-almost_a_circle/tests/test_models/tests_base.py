import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_init_without_id(self):
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_list(self):
        dictionaries = [{"id": 1, "name": "example"}]
        json_string = Base.to_json_string(dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "name": "example"}]')

    def test_save_to_file(self):
        base_instance1 = Base(1)
        base_instance2 = Base(2)
        Base.save_to_file([base_instance1, base_instance2])

        with open('Base.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_with_string(self):
        json_string = '[{"id": 1, "name": "example"}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 1, "name": "example"}])

    def test_create_method(self):
        dictionary = {"id": 1, "name": "example"}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, "example")

    def test_load_from_file_existing_file(self):
        base_instance1 = Base(1)
        base_instance2 = Base(2)
        Base.save_to_file([base_instance1, base_instance2])

        loaded_instances = Base.load_from_file()
        self.assertEqual(len(loaded_instances), 2)
        self.assertEqual(loaded_instances[0].id, 1)
        self.assertEqual(loaded_instances[1].id, 2)

    def test_load_from_file_nonexistent_file(self):
        loaded_instances = Base.load_from_file()
        self.assertEqual(loaded_instances, [])

if __name__ == '__main__':
    unittest.main()
