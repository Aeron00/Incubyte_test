import unittest
from Chandrayaan_3_TDD_Assessment import control_lunar_space_craft

class TestCase(unittest.TestCase):
    def test1_final_pos_and_direction(self):
        result = control_lunar_space_craft((0,0,0),"N",['f','r','u','b','l'])
        self.assertEqual(result,((0,1,-1),"W"))

    def test2_final_pos_and_direction(self):
        result = control_lunar_space_craft((1,1,1),"S",['r','f','u','l','b','r'])
        self.assertEqual(result,((1,1,1),"N"))

if __name__ == "__main__":
    unittest.main()