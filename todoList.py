from item import Item

class ToDoList:
    def __init__(self):
        self.items = []

    
    def get_items(self):
        return self.items


    def add_item(self, item):
        self.items.append(item)
        return True


    def del_item(self, item):
        try:
            self.items.pop(item)
            return True
        
        except:
            return False
    

    def print_items(self):
        for item in self.items:
            print(item.get_text())