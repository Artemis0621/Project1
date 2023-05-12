def enter_scores(app):
    try:
        input_scores = []
        number_of_students = int(app.student_number_input)
        input_scores.append(float(app.student_score_input))

        # TODO: Display the scores in the table widget

        app.student_score_input.clear()
    except ValueError:
        app.error_label.setText("Please enter only numbers for the number of students and their scores.")


def clear_entries(app):
    app.student_number_input.clear()
    app.student_score_input.clear()
    app.score_table.clear()


def calculate_grades(app, scores):
    # TODO: Find a way to input the scores list from the enter_scores() method
    final_grades = []
    best_score = max(scores)

    for x in range(0, len(scores)):
        if scores[x] >= (best_score - 10):
            final_grades.append('A')
        elif scores[x] >= (best_score - 20):
            final_grades.append('B')
        elif scores[x] >= (best_score - 30):
            final_grades.append('C')
        elif scores[x] >= (best_score - 40):
            final_grades.append('D')
        else:
            final_grades.append('F')

    # TODO: Display the grades on the table widget
