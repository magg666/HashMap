from unittest import TestCase
from MyHashMap import MyHashMap, Node


class TestMyHashMapPosition(TestCase):

    def setUp(self) -> None:
        self.test_hash_map = MyHashMap()
        for i in range(self.test_hash_map.bucket_size):
            self.test_hash_map.elements.append(Node(i, i))

    def test_get_position_by_hash_key_exists(self):
        self.assertEqual(self.test_hash_map.get_position_by_hash(0), 0)
        self.assertEqual(self.test_hash_map.get_position_by_hash(1), 1)
        self.assertEqual(self.test_hash_map.get_position_by_hash(15), 15)

    def test_get_position_by_hash_key_not_exists(self):
        self.assertIsNone(self.test_hash_map.get_position_by_hash(16))
        self.assertIsNone(self.test_hash_map.get_position_by_hash("wrong"))
        self.assertIsNone(self.test_hash_map.get_position_by_hash(-3))


class TestMyHashMapPut(TestCase):

    def setUp(self) -> None:
        self.test_hash_map = MyHashMap()
        for i in range(self.test_hash_map.bucket_size):
            self.test_hash_map.elements.append(Node(i, i))

    def test_put_key_exists(self):
        self.test_hash_map.put(1, "updated value")
        self.assertEqual(self.test_hash_map.bucket_size, 16)
        self.assertEqual(self.test_hash_map.get_position_by_hash(1), 1)
        self.assertEqual(self.test_hash_map.get(1), "updated value")

        # loop below is to verify get() method
        for node in self.test_hash_map.elements:
            if node.key == 1:
                self.assertEqual(node.value, "updated value")

    def test_put_key_not_exists(self):
        self.test_hash_map.put("non-existing key", "new value")
        self.assertEqual(self.test_hash_map.bucket_size, 17)

        self.test_hash_map.put("another non-existing key", "another new value")
        self.assertEqual(self.test_hash_map.bucket_size, 18)

        self.assertEqual(self.test_hash_map.get_position_by_hash("non-existing key"), 16)
        self.assertEqual(self.test_hash_map.get_position_by_hash("another non-existing key"), 17)

        self.assertEqual(self.test_hash_map.get("non-existing key"), "new value")
        self.assertEqual(self.test_hash_map.get("another non-existing key"), "another new value")

        # loop below is to verify get() method
        for node in self.test_hash_map.elements:
            if node.key == "non-existing key":
                self.assertEqual(node.value, "new value")
            elif node.key == "another non-existing key":
                self.assertEqual(node.value, "another new value")


class TestMyHashMapGet(TestCase):

    def setUp(self) -> None:
        self.test_hash_map = MyHashMap()
        for i in range(self.test_hash_map.bucket_size):
            self.test_hash_map.elements.append(Node(i, i))

    def test_get_key_exists(self):
        self.assertEqual(self.test_hash_map.get(1), 1)
        self.assertEqual(self.test_hash_map.get(6), 6)
        self.assertEqual(self.test_hash_map.get(15), 15)

    def test_get_key_not_exists(self):
        with self.assertRaises(KeyError):
            self.test_hash_map.get(-3)
            self.test_hash_map.get("key")
            self.test_hash_map.get(16)


class TestMyHashMapClear(TestCase):

    def setUp(self) -> None:
        self.test_hash_map = MyHashMap()
        for i in range(self.test_hash_map.bucket_size):
            self.test_hash_map.elements.append(Node(i, i))

    def test_clear(self):
        self.test_hash_map.clear()
        self.assertEqual(self.test_hash_map.bucket_size, 0)

        with self.assertRaises(KeyError):
            self.test_hash_map.get(0)
            self.test_hash_map.get(15)
            self.test_hash_map.get(16)

        # loop below checks if really there is no node
        counter = 0
        for node in self.test_hash_map.elements:
            if node:
                counter += 1
        self.assertEqual(counter, 0)


class TestMyHashMapRemove(TestCase):

    def setUp(self) -> None:
        self.test_hash_map = MyHashMap()
        for i in range(self.test_hash_map.bucket_size):
            self.test_hash_map.elements.append(Node(i, i))

    def test_remove_key_exists(self):
        self.assertEqual(self.test_hash_map.remove(0), 0)
        self.assertEqual(self.test_hash_map.bucket_size, 15)

        self.assertEqual(self.test_hash_map.remove(6), 6)
        self.assertEqual(self.test_hash_map.bucket_size, 14)

        self.assertEqual(self.test_hash_map.remove(15), 15)
        self.assertEqual(self.test_hash_map.bucket_size, 13)

    def test_remove_key_not_exist(self):
        with self.assertRaises(KeyError):
            self.test_hash_map.remove("wrong key")
            self.test_hash_map.remove(-3)
            self.test_hash_map.remove(16)
