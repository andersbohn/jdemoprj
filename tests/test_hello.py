import unittest
from ppkg import hello

print("test_hello")

class TestHello(unittest.TestCase):

    def test_nothing_really(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
