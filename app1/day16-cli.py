#  optimising the code with default arguments

# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo+ '\n')

        functions.write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:  #  to tell user to enter index number not the todo directly
            number = int(user_action[5:])  # as it's a string we need to convert it into int

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("enter a todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, "todos.txt")
        except ValueError:
            print("Your command is not valid")
            continue  # will ignore everything below and goes to the top of to enter the option again

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, "todos.txt")

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that index number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("This command is invalid. Enter the valid command !")

print('BYE!')
print("added github")




