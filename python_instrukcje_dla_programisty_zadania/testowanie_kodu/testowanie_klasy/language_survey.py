from survey import AnonymousSurvey

# Zdefiniowanie pytania i utworzenie ankiety
question = "Jaki jest Twoj ojczysty jezyk?"
my_survey = AnonymousSurvey(question)

# Wyswietlenie pytania i przechowywanie odpowiedzi na nie
my_survey.show_question()
print("Wpisz 'q', aby zakonczyc dzialanie programu.\n")
while True:
    response = input("Jezyk: ")
    if response == "q":
        break
    my_survey.store_response(response)

# Wyswietlenie wynikow ankiety
print("Dziekujemy kazdemu respodentowi za udzial w ankiecie!")
my_survey.show_results()
