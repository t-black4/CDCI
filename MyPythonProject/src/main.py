from task_manager import Task, TaskManager

def main():
    task_manager = TaskManager()

    # Add some tasks
    task1 = Task("Buy groceries", "Buy milk, eggs, and bread.")
    task2 = Task("Complete homework", "Finish the math assignment.")
    task3 = Task("Clean the house", "Vacuum and mop the floors.")
    
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)

    print("All tasks:")
    for task in task_manager.list_tasks():
        print(task)

    # Find a task by title
    task_to_find = "Complete homework"
    found_task = task_manager.find_task_by_title(task_to_find)
    if found_task:
        print(f"\nFound task: {found_task}")
    else:
        print(f"\nTask '{task_to_find}' not found.")

    # Mark a task as completed
    task_to_complete = task_manager.find_task_by_title("Clean the house")
    if task_to_complete:
        task_to_complete.mark_completed()
        print(f"\nTask '{task_to_complete.title}' marked as completed.")
    
    # Remove a task
    task_manager.remove_task(task1)
    print("\nTasks after removing 'Buy groceries':")
    for task in task_manager.list_tasks():
        print(task)

if __name__ == "__main__":
    main()
