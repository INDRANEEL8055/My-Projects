while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if 'add' in user_action or 'new' in user_action:  # the option 'new' is added
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])  # as its a string we need to convert it into int

        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("enter a todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt','r') as file:
            todos = file.readlines()

        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt','w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("This command is invalid. Enter the valid command !")

print('BYE!')





