import unittest

import moves


class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):  #tests have to start with test
        assert 5 + 5 == 10 #Assert is a function that checks if the statement is true
        
    def test_one_plus_one(self): #tests have to start with test
        assert not 1 + 1 == 3 #Assert is a function that checks if the statement is true
        
if __name__ == '__main__':
    unittest.main()