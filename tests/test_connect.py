import unittest
from connect import connect_agents


# Test zu TP-1
class TestConnectAgents(unittest.TestCase):

    # zur Funktion connect-agents
    def test_case_1(self):
        self.assertTrue(connect_agents(11002, "platform"))

    def test_case_2(self):
        self.assertTrue(connect_agents(11002, "grid"))

    def test_case_3(self):
        self.assertFalse(connect_agents(11002, "Test"))

    def test_case_4(self):
        self.assertFalse(connect_agents(11000, "platform"))

    def test_case_5(self):
        self.assertFalse(connect_agents(11000, "grid"))

    def test_case_6(self):
        self.assertFalse(connect_agents(11000, "Test"))

    def test_case_7(self):
        self.assertFalse(connect_agents(11001, "platform"))

    def test_case_8(self):
        self.assertFalse(connect_agents(11001, "grid"))

    def test_case_9(self):
        self.assertFalse(connect_agents(11001, "Test"))

    def test_case_10(self):
        self.assertFalse(connect_agents(12000, "platform"))

    def test_case_11(self):
        self.assertFalse(connect_agents(12000, "grid"))

    def test_case_12(self):
        self.assertFalse(connect_agents(12000, "Test"))

    def test_case_13(self):
        self.assertFalse(connect_agents(10999, "platform"))

    def test_case_14(self):
        self.assertFalse(connect_agents(10999, "grid"))

    def test_case_15(self):
        self.assertFalse(connect_agents(10999, "Test"))
