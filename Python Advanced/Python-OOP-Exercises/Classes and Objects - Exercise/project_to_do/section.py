from project.task import Task


class Section:
    tasks = []

    def __init__(self, name):
        self.name = name

    def add_task(self, new_task):
        for show in Section.tasks:
            if new_task.name in show.name:
                return f"Task is already in the section {self.name}"
        Section.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for name_t in Section.tasks:
            if task_name == name_t.name:
                name_t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for pos, tasks in enumerate(Section.tasks):
            if tasks.completed:
                count += 1
                del Section.tasks[pos]
        return f"Cleared {count} tasks."

    def view_section(self):
        text = f"Section {self.name}:\n"
        for show in Section.tasks:
            text += f"{show.details()}\n"
        return text



