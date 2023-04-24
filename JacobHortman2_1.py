def get_input():
    taken_scores = []
    number_of_students = int(input('Total number of students: '))  # Takes an input as an int to determine the number of students
    input_scores = input(f'Enter {number_of_students} score(s): ').split()  # Takes the scores as a string and splits them based on whitespace

    while len(input_scores) < number_of_students:  # While there is not enough scores to match each student, asks for the scores again
        input_scores = input(f'Enter {number_of_students} score(s): ').split()

    for x in range(0, len(input_scores)):  # Converts each score in the list to an int
        input_scores[x] = int(input_scores[x])

    for i in range(0, number_of_students):  # Adds scores to take from the input scores for the number of students, chopping off any extra scores
        taken_scores.append(input_scores[i])

    return number_of_students, taken_scores  # Returns the number of students and the scores for each


def get_grades(number_students, student_scores):
    final_grades = []
    best_score = max(student_scores)  # Calculates the best score among the students

    for x in range(0, number_students):  # Calculates the letter grade based on the student's score compared to the best score
        if student_scores[x] >= (best_score - 10):
            final_grades.append('A')
        elif student_scores[x] >= (best_score - 20):
            final_grades.append('B')
        elif student_scores[x] >= (best_score - 30):
            final_grades.append('C')
        elif student_scores[x] >= (best_score - 40):
            final_grades.append('D')
        else:
            final_grades.append('F')

    return final_grades  # Returns the list of letter grades for each student


def main():
    student_count, scores = get_input()  # Gets the necessary input from the user (number of students and their scores)
    letter_grades = get_grades(student_count, scores)  # Calculates the letter grade for each student

    for i in range(0, student_count):  # Prints each student's score and letter grade
        print(f'Student {i + 1} score is {scores[i]} and grade is {letter_grades[i]}')


if __name__ == '__main__':
    main()
