import unittest
import hash_functions as hf

class TestHashFunctions(unittest.TestCase):
    def test_ascii_no_key(self):
        self.assertEqual(hf.h_ascii([],10),'need to specify key')

    def test_ascii_zero_table_size(self):
        key = range(0,10)
        self.assertEqual(hf.h_ascii(key,0),'size of hash table has to be at least 1')

    def test_ascii_ellen_key(self):
        key = 20
        sum = 101*2 + 108*2 + 110 #ascii sum of 'ellen'
        loc = sum % key
        self.assertEqual(hf.h_ascii('ellen',20), loc)

    def test_rolling_no_key(self):
        self.assertEqual(hf.h_rolling([],10),'need to specify key')

    def test_rolling_zero_table_size(self):
        key = range(0,10)
        self.assertEqual(hf.h_rolling(key,0),'size of hash table has to be at least 1')

    def test_rolling_ellen_key(self):
        key = 20
        sum = 101*2 + 108*2 + 110 #ascii sum of 'ellen'
        loc = sum % key
        self.assertNotEqual(hf.h_ascii('ellen',20), None)


if __name__ == '__main__':
    unittest.main()
