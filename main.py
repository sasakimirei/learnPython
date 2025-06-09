while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open("files/subfiles/todos.txt", 'r')
            # todos = file.readlines()
            # file.close()

            with open("files/subfiles/todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open("files/subfiles/todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            with open("files/subfiles/todos.txt", "w") as file:
                file.writelines(todos)

        case 'show':
            with open("files/subfiles/todos.txt", 'r') as file:
                todos = file.readlines()

            # new_todos = []
            #
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # print(new_todos)

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open("files/subfiles/todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open("files/subfiles/todos.txt", "w") as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open("files/subfiles/todos.txt", 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("files/subfiles/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break