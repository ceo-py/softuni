from unittest import TestCase, main

from project.student import Student


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.student = Student("Not Joro")
        self.student_with_courses = Student("Joro", {"Python": ["too weak"]})

    def test_successful_initialization(self):
        self.assertEqual("Not Joro", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Joro", self.student_with_courses.name)
        self.assertEqual({"Python": ["too weak"]}, self.student_with_courses.courses)

    def test_successful_enroll_course_exist_added_only_notes(self):
        result = self.student_with_courses.enroll("Python", ["can't argue with that"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["too weak", "can't argue with that"], self.student_with_courses.courses["Python"])

    def test_successful_enroll_course_and_notes_not_existing_with_Y(self):
        result = self.student.enroll("JS", ["too much {}"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"JS": ["too much {}"]}, self.student.courses)

    def test_successful_enroll_course_and_notes_not_existing_with_empty_string(self):
        result = self.student.enroll("JS", ["too much {}"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"JS": ["too much {}"]}, self.student.courses)

    def test_successful_enroll_course(self):
        result = self.student.enroll("JS", ["too much {}"], "N")

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["JS"])

    def test_unsuccessful_add_notes_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("C--", ["too good, to be true"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_successful_add_notes_to_existing_course_in_list(self):
        result = self.student_with_courses.add_notes("Python", "learn to test")

        self.assertEqual("Notes have been updated", result)
        self.assertTrue("learn to test" in self.student_with_courses.courses["Python"])

    def test_unsuccessful_leave_course_raise_exception_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_successful_leave_course_pop_from_list(self):
        self.student_with_courses.courses = {"Python": ["too weak"], "R": ["Damn its fast"]}
        result = self.student_with_courses.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({"R": ["Damn its fast"]}, self.student_with_courses.courses)


if __name__ == "__main__":
    main()
