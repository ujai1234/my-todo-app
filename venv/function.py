FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_file = file_local.readlines()
    return todos_file

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# cara menguji code tanpa menampilkan di main

if __name__ == "__main__":
    print("hello")
    print(get_todos())
