import unittest
from netmiko import ConnectHandler

class JenkinsUnitTests(unittest.TestCase):
    
    def setUp(self):
        with open('output.txt', 'r') as file:
            self.output = file.read()
    
    def test_R3_Lo99IP(self):
        for line in self.output:
            if "Router3" in line:
                self.assertIn("10.1.3.1/24", line)
                
    def test_R1_single_area(self):
        for line in self.output:
            if "Router1" in line:
                self.assertIn(" 0 ", line)
                
    def test_ping_from_R2_to_R5(self):
        r2 = {
            'device_type': 'cisco_ios',
            'host': '198.51.100.12',
            'username': 'lab',
            'password': 'lab123'
        }
        
        con = ConnectHandler(**r2)
        
        out = con.send_command('ping 10.1.5.1 source lo99')
        self.assertIn("(5/5)", out)


if __name__ == '__main__':
    unittest.main()