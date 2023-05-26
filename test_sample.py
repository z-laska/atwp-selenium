import unittest


class TestLogin(unittest.TestCase):
    def test_success_login(self):
        self.assertEqual(True, True)

    def test_fail_login(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
