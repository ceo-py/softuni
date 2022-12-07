from project.student_report_card import StudentReportCard
import unittest


class TestStudentReportCard(unittest.TestCase):
    def setUp(self):
        # Create a new student report card object before each test
        self.report_card = StudentReportCard("Jane Doe", 1)

    def test_init(self):
        # Test that the student_name property returns the correct value
        self.assertEqual(self.report_card.student_name, "Jane Doe")
        self.assertEqual(self.report_card.school_year, 1)
        self.assertEqual(self.report_card.grades_by_subject, {})

    def test_empty_student_name_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            report_card = StudentReportCard('', 5)

        self.assertEqual(str(ve.exception), "Student Name cannot be an empty string!")

    def test_school_year(self):
        # Test that the school_year property returns the correct value
        self.report_card.school_year = 12
        self.assertEqual(self.report_card.school_year, 12)

    def test_school_year_out_of_bounds_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            report_card = StudentReportCard('John Doe', 0)
        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

        with self.assertRaises(ValueError) as ve:
            report_card = StudentReportCard('John Doe', 13)
        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

    def test_add_grade(self):
        # Test that the add_grade method adds a grade to the correct subject
        self.report_card.add_grade("Math", 90)
        self.assertEqual(self.report_card.grades_by_subject["Math"], [90])

    def test_average_grade_by_subject(self):
        # Test that the average_grade_by_subject method returns the correct value
        self.report_card.add_grade("Math", 90)
        self.report_card.add_grade("Math", 95)
        self.assertEqual(self.report_card.average_grade_by_subject(), "Math: 92.50")

    def test_average_grade_for_all_subjects(self):
        # Test that the average_grade_for_all_subjects method returns the correct value
        self.report_card.add_grade("Math", 90)
        self.report_card.add_grade("English", 95)
        self.assertEqual(self.report_card.average_grade_for_all_subjects(), "Average Grade: 92.50")

    def test_repr(self):
        # Test that the __repr__ method returns the correct value
        self.report_card.add_grade("Math", 90)
        self.report_card.add_grade("English", 95)
        expected_output = "Name: Jane Doe\nYear: 1\n----------\nMath: 90.00\nEnglish: 95.00\n----------\nAverage Grade: 92.50"
        self.assertEqual(self.report_card.__repr__(), expected_output)


if __name__ == "__main__":
    unittest.main()