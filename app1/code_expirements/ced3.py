# strip() strip is used to strip the trailing blank spaces
# capitalize() is used to capitalise the first letter of the input


todos=[]

while True:
    user_action = (input('Type add or show or exit :- ')).strip()
    match user_action:
        case 'add':
            todo = (input("enter a todo:- ").capitalize()).strip()
            todos.append(todo)
        case 'show' | 'display' :
            for item in todos:
                print(item).title()
        case 'exit':
            break
        case _:
            print("Hey, you entered a unknown command!!!")

print("bye bye !")



