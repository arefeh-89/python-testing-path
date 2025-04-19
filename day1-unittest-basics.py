import unittest

def multiply(a,b):
    return a*b

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def reverse_string(s):
    rev = s[::-1]
    return rev

class TestMathFunctions(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(5,8),40)
    def test_multiply_negative(self):
        self.assertEqual(multiply(-3,-6),18)
    def test_multiply_mix(self):
        self.assertEqual(multiply(-5,7),-35)
    def test_multiply_zero_pos(self):
        self.assertEqual(multiply(0,34),0)     
    def test_multiply_zero_neg(self):
        self.assertEqual(multiply(0,-64),0) 

class TestEvenOddFunctions(unittest.TestCase):
    def test_even(self):
        self.assertEqual(is_even(68),True)
    def test_odd(self):
        self.assertEqual(is_even(9),False)
    def test_even(self):
        self.assertEqual(is_even(-40),True)
    def test_even(self):
        self.assertEqual(is_even(-93),False)
    def test_even(self):
        self.assertEqual(is_even(0),True)

class TestReverseString(unittest.TestCase):
    def test_mix_reverse(self):
        self.assertEqual(reverse_string("Arefeh"),"heferA")
    def test_empty_string(self):
        self.assertEqual(reverse_string(""),"")
    def test_uper_string(self):
        self.assertEqual(reverse_string("AREFEH"),"HEFERA")
    def test_lower_string(self):
        self.assertEqual(reverse_string("arefeh"),"hefera")
    def test_space_string(self):
        self.assertEqual(reverse_string("Arefeh is a good girl."),".lrig doog a si heferA")

if __name__ == "__main__":
    unittest.main()





    