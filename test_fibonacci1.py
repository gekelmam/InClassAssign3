import unittest

def fibFunc(nterms):
    n1, n2 = 0, 1
    my_str = ""
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        my_str += str(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return my_str


class TestCube(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(fibFunc(10), "0112358132134")

if __name__ == '__main__':
    unittest.main()