user_prompt = "Enter a todo:"

todos = []

while True:
    user_action = input("Type add os show: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for num, item in enumerate(todos):
                item = item.strip()
                print(num, item)
        case 'edit':
            number = int(input("Enter a number to edit: "))
            existing_todo = todos[number]
            print(existing_todo)
            new_todo = input("Enter a new replacement todo: ")
            todos[number] = new_todo
            print(todos[number])
        case 'exit':
            break
        case _:
            print("Unknown command, please try again!")

print("Bye!")

