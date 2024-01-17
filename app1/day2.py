user_prompt = 'enter a todo:- '

todos=[]

while True:
    todo = input(user_prompt).capitalize()
    todos.append(todo)
    print(todos)
