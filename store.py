import json

# Function to load items from JSON file
def load_items():
    try:
        with open('items.json', 'r') as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []
    return items

# Function to save items to JSON file
def save_items(items):
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)

# Function to create a new item
def create_item(name, price, inventory):
    items = load_items()
    item = {
        'name': name,
        'price': price,
        'inventory': inventory
    }
    items.append(item)
    save_items(items)

# Function to read all items
def read_items():
    items = load_items()
    for item in items:
        print(f"Name: {item['name']}, Price: {item['price']}, Inventory: {item['inventory']}")

# Function to update an item
def update_item(name, price, inventory):
    items = load_items()
    for item in items:
        if item['name'] == name:
            item['price'] = price
            item['inventory'] = inventory
            break
    save_items(items)

# Function to delete an item
def delete_item(name):
    items = load_items()
    items = [item for item in items if item['name'] != name]
    save_items(items)

def main():
    print("Welcome to the store!")
    while True:
        print("\nMenu:")
        print("1. Create item")
        print("2. Read items")
        print("3. Update item")
        print("4. Delete item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the item: ")
            price = float(input("Enter the price: "))
            inventory = int(input("Enter the inventory: "))
            create_item(name, price, inventory)
        elif choice == "2":
            read_items()
        elif choice == "3":
            name = input("Enter the name of the item: ")
            price = float(input("Enter the new price: "))
            inventory = int(input("Enter the new inventory: "))
            update_item(name, price, inventory)
        elif choice == "4":
            name = input("Enter the name of the item to delete: ")
            delete_item(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")  
    
    


if __name__ == '__main__':
    main()