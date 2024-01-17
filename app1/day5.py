# strip() strip is used to strip the trailing blank spaces
# capitalize() is used to capitalise the first letter of the input
# use of fstring and enumerate function.

todos = []

while True:
    user_action = (input('Type add, show, edit , complete or exit :- ')).strip()
    match user_action:
        case 'add':
            todo = (input("enter a todo:- ").capitalize()).strip()
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo which you'd like to edit:- "))
            print(number)
            number = number - 1
            existing_todo = todos[number]
            print(existing_todo)
            new_todo = input("enter the new todo:- ")
            todos[number] = new_todo
            print(new_todo)
        case 'complete':
            number = int(input("Number of todo to complete:- "))
            todos.pop(number-1)

        case 'exit':
            break

print("bye bye !")
