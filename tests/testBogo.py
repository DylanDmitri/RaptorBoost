import unittest
from bogo.RandomTree import RandomTree, bag

class MyTestCase(unittest.TestCase):

    def test_something(self):
        t = RandomTree(1)
        print(t.head.serialize())


if __name__ == '__main__':
    unittest.main()
