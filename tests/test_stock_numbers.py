import unittest

import stock_numbers


class Stock_numbersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = stock_numbers.app.test_client()
    
    def test_version(self):
        rv = self.app.get('/api/v1.0/version')
        self.assertIn('version', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
