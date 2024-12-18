from item import Item
from todoList import ToDoList

new_todo = Item(text="Mow the lawn")
print(new_todo.get_text())

todo_list = ToDoList()

todo_list.add_item(new_todo)

todo_list.print_items()