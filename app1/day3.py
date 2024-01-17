# strip() strip is used to strip the trailing blank spaces
# capitalize() is used to capitalise the first letter of the input


todos = []

while True:
    user_action = (input('Type add, show, edit or exit OR COMEOUT :- ')).strip()
    match user_action:
        case 'add':
            todo = (input("enter a todo:- ").capitalize()).strip()
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the todo which you'd like to edit:- "))
            print(number)
            number = number - 1
            existing_todo = todos[number]
            print(existing_todo)
            new_todo = input("enter the new todo:- ")
            todos[number] = new_todo
            print(new_todo)

        case 'exit':
            break

print("bye bye !")
