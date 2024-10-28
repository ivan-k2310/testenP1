import unittest
from unittest.mock import patch
from App import (
    calcTotaalInkomen,
    calcMaxcHypotheek,
    calcMaxHypotheekMetTermijnen,
)

class TestIntegrationHypotheekCalculator(unittest.TestCase):
    #mocking the functions
    @patch('App.calcTotaalInkomen')
    @patch('App.calcMaxcHypotheek')
    @patch('App.calcMaxHypotheekMetTermijnen')
    def test_integration_hypotheek_calculation_with_studieschuld(self, mock_calcMaxHypotheekMetTermijnen, mock_calcMaxcHypotheek, mock_calcTotaalInkomen):
        #inputs
        jaarInkomen = 50000
        jaarInkomenPartner = 40000
        studieSchuld = True
        termijnen = 5

        #mocking the return values
        mock_calcTotaalInkomen.return_value = jaarInkomen + jaarInkomenPartner
        mock_calcMaxcHypotheek.return_value = (jaarInkomen + jaarInkomenPartner) * 4.25 * 0.75
        mock_calcMaxHypotheekMetTermijnen.return_value = mock_calcMaxcHypotheek.return_value * 1.03

        #call the function
        totaalInkomen = calcTotaalInkomen(jaarInkomen, jaarInkomenPartner)
        maxHypotheek = calcMaxcHypotheek(totaalInkomen, studieSchuld)
        maxHypotheekMetTermijnen = calcMaxHypotheekMetTermijnen(termijnen, maxHypotheek)

        #expected results
        expected_max_hypotheek = (jaarInkomen + jaarInkomenPartner) * 4.25 * 0.75
        expected_max_hypotheek_met_termijnen = expected_max_hypotheek * 1.03

        #expected outcomes
        self.assertEqual(totaalInkomen, jaarInkomen + jaarInkomenPartner)
        self.assertAlmostEqual(maxHypotheek, expected_max_hypotheek)
        self.assertAlmostEqual(maxHypotheekMetTermijnen, expected_max_hypotheek_met_termijnen)

    #mocking the functions
    @patch('App.calcTotaalInkomen')
    @patch('App.calcMaxcHypotheek')
    @patch('App.calcMaxHypotheekMetTermijnen')
    def test_integration_hypotheek_calculation_without_studieschuld(self, mock_calcMaxHypotheekMetTermijnen, mock_calcMaxcHypotheek, mock_calcTotaalInkomen):
        # inputs
        jaarInkomen = 50000
        jaarInkomenPartner = 40000
        studieSchuld = False
        termijnen = 10

        #Mocking the return values
        mock_calcTotaalInkomen.return_value = jaarInkomen + jaarInkomenPartner
        mock_calcMaxcHypotheek.return_value = (jaarInkomen + jaarInkomenPartner) * 4.25
        mock_calcMaxHypotheekMetTermijnen.return_value = mock_calcMaxcHypotheek.return_value * 1.035  # 10 years term adjustment

        #call the function
        totaalInkomen = calcTotaalInkomen(jaarInkomen, jaarInkomenPartner)
        maxHypotheek = calcMaxcHypotheek(totaalInkomen, studieSchuld)
        maxHypotheekMetTermijnen = calcMaxHypotheekMetTermijnen(termijnen, maxHypotheek)

        #expected results
        expected_max_hypotheek = (jaarInkomen + jaarInkomenPartner) * 4.25
        expected_max_hypotheek_met_termijnen = expected_max_hypotheek * 1.035

        #expected outcomes
        self.assertEqual(totaalInkomen, jaarInkomen + jaarInkomenPartner)
        self.assertAlmostEqual(maxHypotheek, expected_max_hypotheek)
        self.assertAlmostEqual(maxHypotheekMetTermijnen, expected_max_hypotheek_met_termijnen)

if __name__ == '__main__':
    unittest.main()