import re
from datetime import datetime

data_file = "tasks.txt"

class Task:
    def __init__(self):
        self.task_data = self.reading()

    def reading(self):
        try:
            with open(data_file, "r") as rf:
                task = []
                for row in rf:
                    title, description, date = row.strip().split(",", 2)
                    task.append({"title": title, "description": description, "date": date })
                return task
        except FileNotFoundError:
            return []

    def saving(self):
        with open(data_file, "w") as wf:
            for row in self.task_data:
                wf.write(f"{row['title']},{row['description']},{row['date']}\n")

    def add_task(self):
        while True:
            self.title = input("Type name of the task: ")
            if self.title != "":
                try:
                    break
                except ValueError:
                    print("There has been Value Error, please, check your input!")
            else:
                print("Please type title of the task!")
        while True:
            self.description = input("Type description of the task: ")
            if self.description != "":
                try:
                    break
                except ValueError:
                    print("There has been Value Error, please check your input")
            else:
                print("Please type description of the task!")
        while True:
            self.date = input("What is the deadline (mm/dd/yyyy): ")
            if re.match(r"^(0?[1-9]|[1][0-2])\/(0[1-9]|[12][0-9]|3[01])\/(20)\d{2}$", self.date):
                try:
                    datetime.strptime(self.date, "%m/%d/%Y")
                    break
                except ValueError:
                    print("Please write correct format of the date! (mm/dd/yyyy)")
            else:
                print("Deadline is mandatory, correct format is (mm/dd/yyyy)! ")
        self.task_data.append({"title": self.title, "description": self.description, "date": self.date })
        print("Task added succesfully!")
        self.saving()

    def view_task(self):
        if self.task_data:
            print("Tasks:")
            for idx, tasks in enumerate(self.task_data, start=1):
                print(f"{idx}. Title: {tasks['title']}, Description: {tasks['description']}, Date: {tasks['date']}")
        else:
            print("There are no tasks")

    def modify_task(self):
        self.view_task()
        if self.task_data:
            index_of_task = int(input("Which task do you like to modify? ")) - 1
            if 0 <= index_of_task < len(self.task_data):
                new_title = input("Please, type new name of the task or press enter to skip: ")
                new_desc = input("Please, type new name of the description or press enter to skip: ")
                while True:
                    new_date = input("Please, type new date of the task or press enter to skip (mm/dd/yyyy): ")
                    if new_date == "":
                        break
                    if re.match(r"^(0?[1-9]|[1][0-2])\/(0[1-9]|[12][0-9]|3[01])\/(20)\d{2}$", new_date):
                        try:
                            datetime.strptime(new_date, "%m/%d/%Y")
                            break
                        except ValueError:
                            print("Please write correct format of the date! (mm/dd/yyyy)")
                    else:
                        print("Please, input date in correct format (mm/dd/yyyy)! ")
                if new_title:
                    self.task_data[index_of_task]['title'] = new_title
                if new_desc:
                    self.task_data[index_of_task]['description'] = new_desc
                if new_date:
                    self.task_data[index_of_task]['date'] = new_date
                print("Task updated!")
                self.saving()
            else:
                print("Invalid number of index!")
        else:
            print("Task box is empty!")

    def delete_task(self):
        self.view_task()
        if self.task_data:
            index_of_task = int(input("Which task do you like to delete? ")) - 1
            if 0 <= index_of_task < len(self.task_data):
                deleted_task = self.task_data.pop(index_of_task)
                print(f"Task '{deleted_task['title']}' deleted!")
                self.saving()
            else:
                print("Invalid number of index!")
        else:
            print("Task file is empty!")

    def main(self):

        while True:
            print("\nInteractive Task Manager")
            print("1. Add Task")
            print("2. View Task")
            print("3. Modify Task")
            print("4. Delete Task")
            print("5. Exit")

            option = input("Please choose your action?(1 to 5): ")

            if option == "1":
                self.add_task()
            elif option == "2":
                self.view_task()
            elif option == "3":
                self.modify_task()
            elif option == "4":
                self.delete_task()
            elif option == "5":
                print("Till we meet again!")
                break
            else:
                print("Wrong number of the option. Please choose from 1 to 5: ")
if __name__ == "__main__":
    task_manager = Task()
    task_manager.main()
