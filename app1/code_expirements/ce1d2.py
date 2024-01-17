user_prompt = 'enter a todo:- '

todos = []

while True:

    todo = input(user_prompt).title()

    todos.append(todo)
    print(todos)
