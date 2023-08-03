import unittest
from Chandrayaan_3_TDD_Assessment import control_lunar_space_craft

class TestCase(unittest.TestCase):
    def test_final_pos_and_direction(self):
        result = control_lunar_space_craft((0,0,0),"N",['f','r','u','b','l'])
        self.assertEqual(result,((1,1,1),"S"))

unittest.main()