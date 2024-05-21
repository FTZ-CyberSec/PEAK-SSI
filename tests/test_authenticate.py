import unittest
from authenticate import new_prosumer

# tests zu TP-9
class TestNew_Prosumer(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(new_prosumer(11002))

    def test_case_2(self):
        self.assertFalse(new_prosumer(11000))

    def test_case_3(self):
        self.assertFalse(new_prosumer(11001))

    def test_case_4(self):
        self.assertFalse(new_prosumer(12000))

    def test_case_5(self):
        self.assertFalse(new_prosumer(10999))

        # Am ende (Zeile 80f) müsste ergänzt werden: return False und return True