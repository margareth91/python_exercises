class AnonymousSurvey:
    """Przecowuje anonimowe odpowiedzi na pytania w ankiecie"""

    def __init__(self, question):
        """Przechowuje pytanie i przygotowuje do przechowywania odpowiedzi"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Wyswietla pytanie z ankiety"""
        print(self.question)

    def store_response(self, new_response):
        """Przechowuje pojedyncza odpowiedz na pytanie z ankiety"""
        self.responses.append(new_response)

    def show_results(self):
        """Wyswietla wszystkie udzielone odpowiedzi"""
        print("Oto wyniki ankiety:")
        for response in self.responses:
            print(f" - {response}")
