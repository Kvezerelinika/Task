# Task Manager
    #### Description: This is my task manager project. It can create tasks with providing title, description and deadline date of the task, which are all mandatory. The tasks are saved in the tasks.txt file, so they are accessible later too. It is possbile to edit or delete tasks as well as it is possbile to edit specific component of the task e.g. only title and skip description and date.

    #### The idea was to make something that would work with data, save it and would have some logics or at least some functions from the lessons. So, at first, I made task manager, which would save task's title and description. However, it only could save data as long as it was active and would delete everything after it was closed, so I wanted to make it more permanent and implemented file save/read function, which makes every created task available as long as it is not deleted. Later on, I decided to also add date to the tasks, after adding it, I made it possible to filter the dates with mm/dd/yyyy format, because before that, it was possible to type anything in date. On the way, I encountered some bugs or issues I already fixed and we have final product.

## Main
    #### Main function provides menu with the list of the actions available. The user should type number from 1 to 5, which is appointed to each option.
    #### 1. Adding a task
    #### 2. Viewing of the task
    #### 3. Modifing the task
    #### 4. Deelting the task
    #### 5. Exiting

    #### After Exiting it prints Goodbye message.

    #### If user types number not from 1 to 5, they are prompted to type again, until they will type number from 1 to 5.

## Adding a task
    #### This function consists of 3 loops, for title, description and date. It prompts the users to provide information, otherwise it is not going to create and save the task.

    #### When the function is triggered, it checks if the input is empty. In th case, when input was empty, request of the input is repeated. If the input is not empty, then title and descripton is accepted.
    #### There is condition on the date, if input isn't empty and something has been inputed, function checks if it is in the format of mm/dd/yyyy, if it is task is created and saved. If there is no input or the format isn't mm/dd/yyyy, user is prompted to type something in correct format.

    #### In the end, the data is saved in the tasks.txt file and user sees the message "Task added succesfully!"

## Viewing of the tasks
    #### This function checks if there is saved tasks. It has two outcomes:

    #### 1. If there is saved data. The tasks are listed with numbers. After the taks list menu is printed for user's next move.
    #### 2. If there is no saved data, user gets the message about empty list and after the tasks list menu is printed for user's next move.

## Modifing the task

    #### This functions modifies the title, description and date of the task. It is also possible to skip one or more parts of the task from modifying.

    #### Triggering the functions calls the view_task function and shows the list of tasks. Where users can choose one they want to modify. If wrong number of index is typed, then user gets the message that they should have typed correct number of index.
    #### After the task is chosen, user is prompted to modify or skip modifying of the title. Same goes for the description as well.

    #### The date modifying has a condition and it should be in format of mm/dd/yyyy, otherwise users are prompted to input something in correct format and if nothing is entered then change of the date is skipped.

    #### If changes are made, they are saved in the task file.

## Deleting the task

    #### This function deletes the task from the saved file.

    #### Triggering the functions calls the view_task function, same way as in modify_task funqciton and shows the list of tasks. User chooses the index of the task they want to delete. After they will choose the index, task is deleted and there will be message that task was deleted, after this change is saved in the file too.

    #### If user will type wrong index of the task or if the task file is empty, they will get appropriate message.

# File I/O

    #### There is two functions for the file input and output:

    #### 1. reading() to open and see contents of the file.
    #### 2. saving() to save changes into the file, it can be from adding new task, edit or delete previously existent tasks.
