"""
non-persistent todo list console app, written in base Python and intended for educational use! 
this file serves as an example solution, and aims to follow best practices and clean coding
principles.
"""
from multiprocessing.sharedctypes import Value


TODO_LIST: list[str] = ["first todo", "add yours!"]


def display_options() -> None:

    print(
        """
Pick an Option:
  1 - Add Todo
  2 - Edit Todo
  3 - Delete Todo
  Q - Quit App
>> """,
        end="",
    )


def display_todos() -> None:
    global TODO_LIST
    [print(f"{idx}. {todo}") for idx, todo in enumerate(TODO_LIST)]


def choose_option() -> str:

    choice = input().lower()
    valid_choices = ["1", "2", "3", "q"]

    # loop until the user provides a valid string from options
    while choice not in valid_choices:
        print("Not a valid choice, try again!")
        display_options()
        choice = input()

    # return valid choice
    return choice


def choose_todo() -> int:
    global TODO_LIST

    while True:
        choice = ""
        try:
            choice = int(input())
        except (ValueError, Exception) as err:
            print("You need to enter the number of your todo!")
            continue

        if choice not in range(len(TODO_LIST)):
            print(f"You don't have a number {choice} todo!")
            continue

        print(f"You chose: {TODO_LIST[choice]}")
        return choice


def add_new_todo():

    # access the global contant todo_list
    global TODO_LIST

    # read the value of their new todo
    print("What is your new todo? Enter anything!")
    new_todo = input()
    TODO_LIST.append(new_todo)


def edit_todo():
    global TODO_LIST
    display_todos()
    print("Which todo do you want to edit?")
    choice = choose_todo()

    print("What would you like to replace this with? Enter anything!")

    updated_todo = input()
    TODO_LIST[choice] = updated_todo


def delete_todo():
    global TODO_LIST

    display_todos()
    print("Which todo do you want to delete?")
    choice = choose_todo()
    print("Are you sure you want to delete this? (y/n)")

    if input().lower() != "y":
        print("Okay, delete mission aborted!")
        return
    TODO_LIST.pop(choice)
    print("Consider it done!")


def main():
    # welcome msg
    print("Welcome to TodoList App!")
    print("--" * 10)

    # start main loop
    while True:
        # accept one of the options
        display_todos()
        display_options()
        choice = choose_option()

        if choice == "1":
            add_new_todo()
        if choice == "2":
            edit_todo()
        if choice == "3":
            delete_todo()
        if choice == "q":
            print("Thanks for using the app; good luck with your Todo-ing!")
            break



if __name__ == "__main__":
    main()
