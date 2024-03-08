def get_todos(filepath='todos.txt'):
    """ Read the text file and return
    the to-do items."""
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local
def write_todos(todos_arg,filepath='todos.txt'):
    """ Write the to-do items to the text file."""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

def showTodos():
    todos = get_todos()
    # new_todos = [item.strip('\n') for item in todos] #list comprehension
    print("\n")
    for index, item in enumerate(todos):
        item = item.strip('\n')  # to remove the extra break line in console
        print(index + 1, "-->", item, )
    print("\n")