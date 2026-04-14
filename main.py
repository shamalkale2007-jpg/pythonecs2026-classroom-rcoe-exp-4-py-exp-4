# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:
# Date:

# Write your code here
print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# Write your code here
# TODO: Add & Print new Task from user
new_task = input("Enter a new task to add: ")
tasks.append(new_task)
print(f"Tasks after Adding: {tasks}")
# TODO: Edit & Print task selected by User
edit_index = int(input("Enter the index of the task to edit: "))
edited_task = input("Enter the new task: ")
tasks[edit_index] = edited_task
print(f"Tasks after Editing: {tasks}")
# TODO: Remove & Print a Task selected by User
remove_index = int(input("Enter the index of the task to remove: "))
tasks.pop(remove_index)
print(f"Tasks after Removing: {tasks}")
# TODO: Sort & Print the Tasks
tasks.sort()
print(f"Tasks after Sorting: {tasks}")
