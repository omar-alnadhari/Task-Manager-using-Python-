import os
os.system('cls') #مسح المسارات التي تظهر في الكونسول

def add_task(): # add task to the list
    # get task from user
    task = input("Enter task: ")
    # define task status
    task_info = {"task":task,"completed":False}
    # add task to the list of tasks
    tasks.append(task_info)
    print("Task added to the lsit successfuly")
    
def mark_task_complete():
    pass
def view_tasks():
    ...

message = """1- add tasks to a list
2- mark task as complete
3- view tasks
4- Quit"""
# 
tasks = []

while(True):
    print(message)
    choice = input("Enter your choice: ")
    if choice == "1":
        # add task to tasks list
        add_task()
    elif choice == "2":
        # علم على المهمة ان المهمة تم اكمالها
        mark_task_complete()
    elif choice == "3":
        # عرض جميع المهام الموجودة
        view_tasks()
    elif choice == "4":
        # الخروج من البرنامج
        break
    else:
        print("Invalid choice, please enter a number between 1 and 4")
