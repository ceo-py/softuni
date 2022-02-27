grades = float(input())

def check_grade(grade):
    if 2.00 <= grade <= 2.99:
        return print("Fail")
    elif 3.00 <= grade <= 3.49:
        return print("Poor")
    elif 3.50 <= grade <= 4.49:
        return print("Good")
    elif 4.50 <= grade <= 5.49:
        return print("Very Good")
    elif 5.50 <= grade <= 6:
        return print("Excellent")

check_grade(grades)