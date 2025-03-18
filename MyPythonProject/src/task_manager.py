class Task:
    def __init__(self, title, description, status="pending"):
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, status={self.status})"

    def mark_completed(self):
        self.status = "completed"


class TaskManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        return self.tasks

    def find_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
