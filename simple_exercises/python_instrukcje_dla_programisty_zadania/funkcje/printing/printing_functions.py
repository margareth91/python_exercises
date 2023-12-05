def print_models(unprinted_designs1, completed_models1):
    while unprinted_designs1:
        current_design = unprinted_designs1.pop()

        print(f"Wydruk modelu: {current_design}")
        completed_models1.append(current_design)


def show_completed_models(completed_models2):
    for completed_model in completed_models2:
        print(f"Wydrukowano model: {completed_model}")
