from datetime import datetime, date 
import json
def add_task(task_list, title, due_date=None):
    """ 
    Creates a new Task and adds it to the list.
    Parses due_date string (YYYY-MM-DD) into a datetime.date object.
    """
    parsed_date = None

    if due_date:
        try:
             # Parse string and extract the date component
             parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Error: Invalid date format for '{title}'. Please use 'YYYY-MM-DD'.")
            return False

        # Create the task dictionary
        new_task = {
            "title": title,
            "due_date": parsed_date,
            "completed": False
        }

        task_list.append(new_task)
        print(f"Task '{title}' added successfully.")
        return True

    
def complete_task(task_list, index):
    """
    Marks the task at the given index as completed.
    """
    actual_index = index - 1
    try:
        task_list[actual_index] ["completed"] = True
        print(f"Task at index {index} marked as completed.")
    except IndexError:
        print(f"Error: Index {index} is invalid. No task found.")


def delete_task(task_list, index):
    """
    Removes the task at the given index.
    """
    try:
        if 0 <= index < len(task_list):
            removed_task = task_list.pop(index)
            print(f"Task '{removed_task['title']}' removed successfully.")
        else:
            print(f"Error: Index {index} is invalid. Cannot delete.")
    except Exception as e:
        print(f"Error deleting task at index {index}: {e}")


def list_tasks(task_list):
     """ 
     Prints a formatted list of tasks with index, status, title, and due date.
     Flags overdue tasks by comparing with today's date.
     """
     if not task_list:
          print("No tasks found in the list.")
          return

     today = date.today()
     print("\n--- Current To-Do List " + "-" * 3)

     for index, task in enumerate(task_list):
          status = "🟢 Done" if task["completed"] else "❌ Pending"
          due_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "No due date"

          # Check if overdue (pending and past today's date)
          overdue_flag = ""
          if not task["completed"] and task["due_date"] and task["due_date"] < today:
               overdue_flag = "⚠️  OVERDUE!"

          print(f"[{index}] Status: {status} | Title: {task['title']} | Due: {due_str} {overdue_flag}")
          print(f" {"-" * 82} \n")


def save_tasks(task_list):
    # Convert any date  objects to strings so JSON can save them safely
    serializable_tasks = []
    for task in task_list:
        task_copy = task.copy()
        if task_copy["due_date"] and not isinstance(task_copy["due_date"], str):
            task_copy["due_date"] =  task_copy["due_date"].strftime("%Y-%m-%d")
        serializable_tasks.append(task_copy)

    # Write everything to a file called tasks.json
    with open("tasks.json", "w") as f:
        json.dump(serializable_tasks, f, indent=4)
        print("Tasks successfully saved to tasks.json!")


if __name__ == "__main__":
 my_task = []
 add_task(my_task, "Finished assignment", "2026-07-24")
 add_task(my_task, "PCEP training ongoing", "2026-07-21")
 complete_task(my_task, 0)
 list_tasks(my_task)
 