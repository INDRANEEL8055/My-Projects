# strip() strip is used to strip the trailing blank spaces
# capitalize() is used to capitalise the first letter of the input
# use of fstring and enumerate function.



while True:
    user_action = (input('Type add, show, edit , complete or exit :- ')).strip()

    match user_action:
        case 'add':
            todo = (input("enter a todo:- ").capitalize()).strip() + "\n"

            # reading existing file
            file = open('todos.txt','r')  # adding the previous entries
            todos = file.readlines()   # writing them in a list so that old entries dont disappear everytime we run
            # the code
            file.close()

            # taking user entry and adding it to list
            todos.append(todo)

            # writing the appended list in text file
            file = open('todos.txt','w')  # first argument is the address , then second argument is 'w' write the file
            file.writelines(todos)  # argument will be list itself

        case 'show':
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            # to remove the breaking lines "extra space between todos
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # or instead use the list comprehension
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')  # for stripping the spaces between todos
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
            number = int(input("enter the Number of todo which is completed:- "))
            todos.pop(number-1)

        case 'exit':
            break

print("bye bye !")
