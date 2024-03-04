import store

def add_to_cart(cart):
    inventory = store.load_items()
    print("Pleaase select an item from the inventory: \n")
    for products in inventory:
        print(f"Name: {products['name']}, Price: {products['price']}, Inventory: {products['inventory']}")
    name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity: "))
    for i in range(len(inventory)):
        if inventory[i]['name'] == name:
            if inventory[i]['inventory'] >= quantity:
                inventory[i]['inventory'] -= quantity
                for item in cart:
                    if item["name"] == name:
                        item["quantity"] += quantity
                        return True
                print(f"Item added to the cart. {quantity} {name} added to the cart.")
                print(cart)
                store.save_items(inventory)
                item = {"name": inventory[i]['name'], "quantity": quantity, "price": inventory[i]['price']}
                cart.append(item)
                return True
            else:
                print("Sorry, the item is out of stock.")
                return False
    print("Item not found in the inventory.")
    
def add_item(cart):
    name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    item = {"name": name, "quantity": quantity, "price": price}
    cart.append(item)
    print("Item added to the cart.")

def remove_item(cart):
    name = input("Enter the name of the item to remove: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            store.update_item(name, item["price"], item["quantity"])
            print("Item removed from the cart.")
            return
    print("Item not found in the cart.")

def display_cart(cart):
    total_cost = 0
    print("Shopping Cart:")
    for item in cart:
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
        total_cost += item['quantity'] * item['price']
    print(f"Total Cost: {total_cost}")

def main():
    cart = []
    while True:
        print("\nMenu:")
        print("0. Manage store inventory")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Display cart")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "0":
            store.main()
        elif choice == "1":
            add_to_cart(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            print("Thank you for using the shopping cart program!")
            display_cart(cart)
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()