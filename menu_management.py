def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} does not exist in the menu.")

def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(initial_menu, "Tacos")
remove_item(initial_menu, "Salad")
availability = check_item(initial_menu, "Pizza")
print(f"Updated menu: {initial_menu}")
print(f"Availability: {availability}")