from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("Joro", 12)

    def test_successful_initialization(self):
        self.assertEqual("Joro", self.student_report_card.student_name)
        self.assertEqual(12, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_unsuccessful_student_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))


    def test_unsuccessful_school_year_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_successful_add_grade_to_dict(self):
        self.student_report_card.add_grade("Python", 6)
        self.student_report_card.add_grade("R", 6)

        self.assertEqual({"Python": [6], "R": [6]}, self.student_report_card.grades_by_subject)
        self.student_report_card.add_grade("Python", 5.50)

        self.assertEqual({"Python": [6, 5.50], "R": [6]}, self.student_report_card.grades_by_subject)

    def test_successful_average_grade_by_subject_return_string(self):
        self.student_report_card.add_grade("Python", 6)
        self.student_report_card.add_grade("R", 6)
        self.student_report_card.add_grade("Python", 5.50)
        result = self.student_report_card.average_grade_by_subject()

        self.assertEqual("Python: 5.75\n"
                         "R: 6.00", result)

    def test_successful_average_grade_for_all_subjects_return_string(self):
        self.student_report_card.add_grade("Python", 6)
        self.student_report_card.add_grade("R", 6)
        self.student_report_card.add_grade("Python", 5.50)

        result = self.student_report_card.average_grade_for_all_subjects()

        self.assertEqual("Average Grade: 5.83", result)

    def test__repr__(self):
        self.student_report_card.add_grade("Python", 6)
        self.student_report_card.add_grade("R", 6)

        self.assertEqual("Name: Joro\n"
                         "Year: 12\n"
                         "----------\n"
                         "Python: 6.00\n"
                         "R: 6.00\n"
                         "----------\n"
                         "Average Grade: 6.00", self.student_report_card.__repr__())


if __name__ == "__main__":
    main()
