import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Testy dla klasy AnonymousSurvey"""

    def setUp(self):
        """Utworzenie ankiety i zestawu odpowiedzi do uzycia we wszystkich metodach testowych"""
        question = "Jaki jest Twoj ojczysty jezyk?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["angielski", "polski", "niemiecki"]

    def test_store_single_response(self):
        """Sprawdzenie, czy pojedyncza odpowiedz jest prawidlowo przechowywana"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Sprawdzenie, czy trzy pojedyncze odpowiedzi sa prawidlowo przechowywane"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
