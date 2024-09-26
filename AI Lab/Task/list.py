tasks = []

def add_task():
  
  task = input("Enter a new task: ")
  tasks.append(task)
  print("Task added successfully!")

def view_tasks():
  
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("To-do list:")
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")

def complete_task():
  
  view_tasks()
  if tasks:
    task_index = int(input("Enter the number of the task to complete: ")) - 1
    if 0 <= task_index < len(tasks):
      completed_task = tasks.pop(task_index)
      print(f"Task '{completed_task}' marked as complete!")
    else:
      print("Invalid task number.")

def clear_list():
  
  tasks.clear()
  print("To-do list cleared!")

while True:
  print("\nTo-do List Menu:")
  print("1. Add task")
  print("2. View tasks")
  print("3. Complete task")
  print("4. Clear list")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    add_task()
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    complete_task()
  elif choice == '4':
    clear_list()
  elif choice == '5':
    print("Exiting...")
    break
  else:
    print("Invalid choice.")