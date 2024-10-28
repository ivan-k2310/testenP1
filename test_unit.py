
from queue import Full
import unittest
from unittest.mock import patch
from App import calcTotaalInkomen, calcMaxcHypotheek, calcMaxHypotheekMetTermijnen, MaxHypotheekPartner

class TestMaxHypotheekFunctions(unittest.TestCase):

    def test_calcTotaalInkomen(self):
        print("Running test_calcTotaalInkomen...")
        self.assertEqual(calcTotaalInkomen(50000, 30000), 80000)
        self.assertEqual(calcTotaalInkomen(0, 0), 0)
        self.assertEqual(calcTotaalInkomen(10000, 0), 10000)

    def test_calcMaxcHypotheek(self):
        print("Running test_calcMaxcHypotheek...")
        self.assertEqual(calcMaxcHypotheek(80000, True), 80000 * 4.25 * 0.75)
        self.assertEqual(calcMaxcHypotheek(80000, False), 80000 * 4.25)

    def test_calcMaxHypotheekMetTermijnen(self):
        print("Running test_calcMaxHypotheekMetTermijnen...")
        self.assertEqual(calcMaxHypotheekMetTermijnen(1, 100000), 100000 * 1.02)
        self.assertEqual(calcMaxHypotheekMetTermijnen(5, 100000), 100000 * 1.03)
        self.assertEqual(calcMaxHypotheekMetTermijnen(10, 100000), 100000 * 1.035)
        self.assertEqual(calcMaxHypotheekMetTermijnen(20, 100000), 100000 * 1.045)
        self.assertEqual(calcMaxHypotheekMetTermijnen(30, 100000), 100000 * 1.05)
        self.assertEqual(calcMaxHypotheekMetTermijnen(0, 100000), None)  # default case

if __name__ == "__main__":
    unittest.main()