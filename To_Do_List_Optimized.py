from datetime import date
import random

Tasks_List = [ ]
quotes_List=[]
RB_Task_List = ["Call to Subbu"]

def quotesPopUp():
    with open("quotes_List.txt","r") as quotes:
        quotes_List=[eachline.strip() for eachline in quotes if eachline.strip()]
        if quotes_List:
            print(random.choice(quotes_List))


with open("ToDo_List.txt","r") as f_read:
    for eachLine in f_read:
        if eachLine.strip():
            Tasks_List.append(eachLine.strip().capitalize())


def wellcome():
    print("\nSelect an option below:")
    print("----------------------")
    print("\t1. Add Task\n\t2. Delete Task\n\t3. View Task\n\t4. View Recycle Bin\n\t5. Quit\nToday Quote : ")
    quotesPopUp()

def show_list(title, items):
    print(f"\n{title}\n{'-' * len(title)}")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    if not items:
        print("No items available.")

def recycleB():
    print("Welcome To Recycle Bin")
    while RB_Task_List:
        show_list("Recycle Bin Tasks", RB_Task_List)
        user_input = input("Enter task number to delete or 'No' to exit: ").strip().lower()
        if user_input == "no":
            break
        if user_input.isdigit():
            idx = int(user_input)
            if 1 <= idx <= len(RB_Task_List):
                RB_Task_List.pop(idx - 1)
                print("Task Deleted.\n")
            else:
                print("Invalid Task Number.\n")
        else:
            print("Invalid input.\n")
    else:
        print("Recycle Bin Is Empty")
    input("Press Enter to return to Main Menu...\n")

def addtask():
    print('Type tasks or "No" to exit')
    count = 1
    while True:
        task = input(f"{count} - ").strip()
        if task.lower() == "no":
            break
        Tasks_List.append(task)
        print(f'Task "{task}" saved.')
        count += 1

def up_toFile():
    with open("ToDo_List.txt","w") as task_append:
        for task in Tasks_List:
            task_append.writelines(task+"\n")

  
def del_task():
    while Tasks_List:
        show_list("Task List", Tasks_List)
        user_input = input("Enter task number to delete or 'No' to exit: ").strip().lower()
        if user_input == "no":
            break
        if user_input.isdigit():
            idx = int(user_input)
            if 1 <= idx <= len(Tasks_List):
                confirm = input("Confirm deletion? Type 'Yes' to delete: ").strip().lower()
                if confirm == "yes":
                    RB_Task_List.append(Tasks_List.pop(idx - 1))
                    print("Task deleted.\n")
                else:
                    print("Cancelled.\n")
                    break
            else:
                print("Invalid task number.\n")
        else:
            print("Invalid input.\n")
            break
    else:
        print("No Active Tasks Available.")

def view_task():
    show_list("Task List", Tasks_List)
    input("Press Enter to return to Main Menu...\n")

if __name__ == "__main__":
    print(f"\n\tWelcome to Daily Tasks of {date.today()}")
    print("\t-------------------------------------")
    while True:
        wellcome()
        try:
            choice = int(input("\nEnter an option number: "))
            match choice:
                case 1:
                    addtask()
                    up_toFile()
                case 2:
                    del_task()
                case 3:
                    view_task()
                case 4:
                    recycleB()
                case 5:
                    print("Thank You and Good Bye")
                    up_toFile()
                    break
                case _:
                    print("Invalid option. Try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")
            up_toFile()