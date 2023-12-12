import datetime

class Task:
    def __init__(self, task_name, deadline, assigned_to=None):
        self.task_name = task_name
        self.deadline = deadline
        self.assigned_to = assigned_to
        self.completed = False
        self.grade = None

    def mark_as_completed(self):
        self.completed = True

    def assign_grade(self, grade):
        if self.completed:
            self.grade = grade
        else:
            print("The task must be completed before assigning a grade.")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' has been removed.")
                break
        else:
            print(f"Task '{task_name}' not found.")

    def prioritize_tasks(self):
        self.tasks.sort(key=lambda x: x.deadline)

    def show_all_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("All Tasks:")
            for task in self.tasks:
                print(f"Task: {task.task_name}, Deadline: {task.deadline}, Assigned to: {task.assigned_to}, Completed: {task.completed}, Grade: {task.grade if task.completed else 'Not graded'}")

    def find_task_by_name(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                return task
        return None

# Helper function to validate date format
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Main program
task_manager = TaskManager()

while True:
    print("\n==== Task Manager ====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show All Tasks")
    print("4. Prioritize Tasks")
    print("5. Mark Task as Completed")
    print("6. Grade Task")
    print("7. Assign Task")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        if not validate_date(deadline):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        assigned_to = input("Enter assigned person (optional): ")
        task = Task(task_name, deadline, assigned_to)
        task_manager.add_task(task)
        print(f"Task '{task_name}' added.")

    elif choice == "2":
        task_name = input("Enter task name to remove: ")
        task_manager.remove_task(task_name)

    elif choice == "3":
        task_manager.show_all_tasks()

    elif choice == "4":
        task_manager.prioritize_tasks()
        print("Tasks prioritized based on deadlines.")

    elif choice == "5":
        task_name = input("Enter task name to mark as completed: ")
        task_to_complete = task_manager.find_task_by_name(task_name)
        if task_to_complete:
            task_to_complete.mark_as_completed()
            print(f"Task '{task_name}' marked as completed.")
        else:
            print(f"Task '{task_name}' not found.")

    elif choice == "6":
        task_name = input("Enter task name to assign grade: ")
        task_to_grade = task_manager.find_task_by_name(task_name)
        if task_to_grade:
            if task_to_grade.completed:
                grade = input("Enter the grade: ")
                task_to_grade.assign_grade(grade)
                print(f"Grade assigned to Task '{task_name}'")
            else:
                print("The task must be completed before assigning a grade.")
        else:
            print(f"Task '{task_name}' not found.")

    elif choice == "7":
        task_name = input("Enter task name to assign: ")
        assigned_to = input("Enter assigned person: ")
        task_to_assign = task_manager.find_task_by_name(task_name)
        if task_to_assign:
            task_to_assign.assigned_to = assigned_to
            print(f"Task '{task_name}' assigned to '{assigned_to}'")
        else:
            print(f"Task '{task_name}' not found.")

    elif choice == "8":
        print("Exiting the Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
