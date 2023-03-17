import unittest
from ut1 import get_name
class NamesTestCase(unittest.TestCase):
    def test_1(self):
        get = get_name('nick', 'sheva')
        self.assertEqual(get, "Nick Sheva")
if __name__ == '__main__':
    unittest.main()