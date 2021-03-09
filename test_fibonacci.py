import unittest
import fibonacci

class TestCube(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci.fibFunc(10), "0112358132134")

if __name__ == '__main__':
    unittest.main()