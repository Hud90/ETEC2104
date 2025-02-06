from unittest import TestCase

class T(TestCase):
    def test_dummy(self):
        self.assertEqual(1,1)
    def test_shouldFail(self):
        self.assertEqual(1,1)