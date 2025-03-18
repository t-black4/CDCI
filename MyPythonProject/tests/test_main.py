import unittest
from task_manager import Task, TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Create a TaskManager instance and some tasks for testing."""
        self.task_manager = TaskManager()
        self.task1 = Task("Buy groceries", "Buy milk, eggs, and bread.")
        self.task2 = Task("Complete homework", "Finish the math assignment.")
        self.task3 = Task("Clean the house", "Vacuum and mop the floors.")

    def test_add_task(self):
        """Test if a task is added correctly."""
        self.task_manager.add_task(self.task1)
        self.assertIn(self.task1, self.task_manager.list_tasks())

    def test_remove_task(self):
        """Test if a task is removed correctly."""
        self.task_manager.add_task(self.task1)
        self.task_manager.remove_task(self.task1)
        self.assertNotIn(self.task1, self.task_manager.list_tasks())

    def test_find_task_by_title(self):
        """Test finding a task by its title."""
        self.task_manager.add_task(self.task2)
        found_task = self.task_manager.find_task_by_title("Complete homework")
        self.assertEqual(found_task, self.task2)

    def test_task_mark_completed(self):
        """Test if a task can be marked as completed."""
        self.task_manager.add_task(self.task3)
        self.task3.mark_completed()
        self.assertEqual(self.task3.status, "completed")

    def test_singleton_property(self):
        """Test if TaskManager is a singleton."""
        manager1 = TaskManager()
        manager2 = TaskManager()
        self.assertIs(manager1, manager2)  # Ensure both references point to the same object


if __name__ == "__main__":
    unittest.main()
