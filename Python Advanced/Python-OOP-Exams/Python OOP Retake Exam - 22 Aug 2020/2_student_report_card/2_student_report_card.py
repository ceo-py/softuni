from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("Joro", 12)

    def test_successful_initialization(self):
        self.assertEqual("Joro", self.student_report_card.student_name)
        self.assertEqual(12, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_unsuccessful_student_name_setter_raise_value_error_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_successful_year(self):
        self.student_report_card.school_year = 1

        self.assertEqual(1, self.student_report_card.school_year)

    def test_unsuccessful_school_year_setter_raise_value_error_less_than_1_and_more_than_12(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_successful_add_grade(self):
        self.student_report_card.add_grade("Python", 6.00)

        self.assertEqual({"Python": [6.00]}, self.student_report_card.grades_by_subject)
        self.student_report_card.add_grade("Python", 6.00)
        self.assertEqual({"Python": [6.00, 6.00]}, self.student_report_card.grades_by_subject)

    def test_successful_average_grade_by_subject(self):
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Fund", 6.00)
        result = self.student_report_card.average_grade_by_subject()

        self.assertEqual([6.0, 6.0], self.student_report_card.grades_by_subject["P - Basic"])
        self.assertEqual([6.0], self.student_report_card.grades_by_subject["P - Fund"])
        self.assertEqual(1, len(self.student_report_card.grades_by_subject["P - Fund"]))
        self.assertEqual("P - Basic: 6.00\n"
                         "P - Fund: 6.00", result)

    def test_successful_average_grade_for_all_subjects(self):
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Fund", 6.00)

        result = self.student_report_card.average_grade_for_all_subjects()

        self.assertEqual("Average Grade: 6.00", result)
        self.assertEqual([6.0], self.student_report_card.grades_by_subject["P - Fund"])
        self.assertEqual([6.0, 6.0], self.student_report_card.grades_by_subject["P - Basic"])

    def test__repr__(self):
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Basic", 6.00)
        self.student_report_card.add_grade("P - Fund", 6.00)

        result = self.student_report_card.__repr__()

        self.assertEqual("Name: Joro\n"
                         "Year: 12\n"
                         "----------\n"
                         f"{self.student_report_card.average_grade_by_subject()}\n"
                         "----------\n"
                         f"{self.student_report_card.average_grade_for_all_subjects()}", result)


if __name__ == "__main__":
    main()
