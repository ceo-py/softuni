from project_to_do.task import Task
from project_to_do.section import Section

import unittest


class Test(unittest.TestCase):

    def test_task_init(self):
        task = Task("Tst", "27.04.2020")
        message = f"{task.name} - {task.due_date}"
        expected = "Tst - 27.04.2020"
        self.assertEqual(message, expected)

    def test_change_name_working(self):
        task = Task("Tst", "27.04.2020")
        task.change_name("New name")
        message = task.name
        expected = "New name"
        self.assertEqual(message, expected)

    def test_change_name_same_name(self):
        task = Task("Tst", "27.04.2020")
        message = task.change_name("Tst")
        expected = "Name cannot be the same."
        self.assertEqual(message, expected)

    def test_change_due_date_working(self):
        task = Task("Tst", "27.04.2020")
        task.change_due_date("21.05.2020")
        message = task.due_date
        expected = "21.05.2020"
        self.assertEqual(message, expected)

    def test_edit_comment_working(self):
        task = Task("Tst", "27.04.2020")
        task.add_comment("pay the bills")
        message = task.edit_comment(0, "finish my homework")
        expected = "finish my homework"
        self.assertEqual(message, expected)

    def test_edit_comment_not_found(self):
        task = Task("Tst", "27.04.2020")
        task.add_comment("pay the bills")
        message = task.edit_comment(1, "finish my homework")
        expected = "Cannot find comment."
        self.assertEqual(message, expected)

    def test_section_init(self):
        section = Section("New section")
        message = f"{section.name} - {len(section.tasks)}"
        expected = "New section - 0"
        self.assertEqual(message, expected)

    def test_add_task(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        message = section.add_task(task)
        expected = "Task Name: Tst - Due Date: 27.04.2020 is added to the section"
        self.assertEqual(message, expected)

    def test_add_task_already_added(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        message = section.add_task(task)
        expected = "Task is already in the section New section"
        self.assertEqual(message, expected)

    def test_complete_task(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        section.complete_task("Tst")
        message = task.completed
        self.assertTrue(message)

    def test_complete_task_message(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        message = section.complete_task("Tst")
        expected = "Completed task Tst"
        self.assertEqual(message, expected)

    def test_complete_not_found(self):
        section = Section("New section")
        message = section.complete_task("Tst")
        expected = "Could not find task with the name Tst"
        self.assertEqual(message, expected)

    def test_clean_section(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        section.complete_task("Tst")
        message = section.clean_section()
        expected = "Cleared 1 tasks."
        self.assertEqual(message, expected)

    def test_view_section(self):
        section = Section("New section")
        message = section.view_section().strip()
        expected = "Section New section:"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()