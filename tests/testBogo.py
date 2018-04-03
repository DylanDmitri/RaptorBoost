import unittest
from bogo.BogoBoost import RandomTree

class MyTestCase(unittest.TestCase):
    def test_something(self):
        t = RandomTree(3)
        print(t.head.serialize)

if __name__ == '__main__':
    unittest.main()
