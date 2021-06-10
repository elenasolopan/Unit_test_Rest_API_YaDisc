import unittest
from Ya_Disc import *


class TestUnittest(unittest.TestCase):
    def setUp(self):
        print("Method setup")

    def test_create_folder(self):
        self.assertEqual(YaDiscUser.create_folder(YaDiscUser('YOUR TOKEN YANDEX_DISC'),
                                                  "Your folder's name"), 201)

    def test_create_folder_exist(self):
        self.assertEqual(YaDiscUser.create_folder(YaDiscUser('YOUR TOKEN YANDEX_DISC'),
                                                  "Your folder's name"), 409)

    def test_create_folder_wrong_token(self):
        self.assertEqual(YaDiscUser.create_folder(YaDiscUser('WRONG TOKEN'),
                                                  "Your folder's name"), 401)

    def tearDown(self):
        print(f"Method tearDown\n")


if __name__ == '__main__':
    unittest.main()
