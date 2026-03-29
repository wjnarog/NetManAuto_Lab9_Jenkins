import unittest

class JenkinsUnitTests(unittest.TestCase):
    
    def setUp(self):
        with open('output.txt', 'r') as file:
            self.output = file.read()
    
    def Test_R3_Lo99IP(self):
        pass


if __name__ == '__main__':
    unittest.main()