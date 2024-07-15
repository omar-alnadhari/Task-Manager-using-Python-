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
    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task[ "completed"] == False ]
    # print(incomplete_tasks)

    # للخروج من الدالة اذا لم يوجد مهام للتعليم عليها انها مكتملة
    if len(incomplete_tasks) == 0: #another way => if not incomplete_tasks:
        print("No tasks to mark as complete")
        print("-"*25)
        return
    
    #show incomplete tasks to the user
    for i,task in enumerate(incomplete_tasks):
        print(f"{i+1}- {task['task']}")
    print("-"*25)
    
    # get the task number from the user
    task_number = int(input("Choose the task to complete"))

    # mark the task as completed
    incomplete_tasks [task_number - 1]["completed"] = True
    # aliasing

    # print a message to the user
    print("Task marked successfuly")

    #  pass

###--- Function to view the tasks ---###
def view_tasks():
    # if there are no tasks, print a message and write return
    if not tasks:
        print("No tasks to view")
        print("-"*25)
        return
    
    for i,task in enumerate(tasks):

        # if task["completed"]:
        #     status = "✔️"
        # else:
        #     status = "❌"
        status = "✔️" if task["completed"] else "❌"  # same work as above

        print(f"{i+1}. {task['task']} {status}")
    
    print("-"*25)
    # ❌
    # ✔️  #         شعار الويندوز   +   .

    #...  # ... هي نفسها  pass


message = """1- add tasks to a list
2- mark task as complete
3- view tasks
4- Quit"""
# 
tasks = []

while(True):
    print(message)
    choice = input("Enter your choice: ")
    print("-"*25)
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
