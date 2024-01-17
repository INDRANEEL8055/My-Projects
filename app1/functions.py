FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ It is the function to read the text file
    and return the list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)