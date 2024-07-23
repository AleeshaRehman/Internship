from inventory_management import FoodItem, Inventory

def main():
    inventory = Inventory()

    item1 = FoodItem(name="Milk", category="Dairy", quantity=10, barcode="12345", expiry_date="2024-07-25")
    item2 = FoodItem(name="Eggs", category="Poultry", quantity=30, barcode="12346", expiry_date="2024-07-24")
    item3 = FoodItem(name="Cheese", category="Dairy", quantity=5, barcode="12347", expiry_date="2024-07-30")
    
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    print("All Items:")
    print(inventory.items)

    print("\nSearching for item with barcode 12345:")
    print(inventory.search_item_by_barcode("12345"))

    print("\nSearching for items with name 'Eggs':")
    print(inventory.search_item_by_name("Eggs"))

    print("\nSearching for items in category 'Dairy':")
    print(inventory.search_item_by_category("Dairy"))

    print("\nEditing item with barcode 12345 (change quantity to 20):")
    inventory.edit_item("12345", quantity=20)
    print(inventory.search_item_by_barcode("12345"))

    print("\nItems nearing expiry within 7 days:")
    for item in inventory.near_expiry_generator(7):
        print(item)

    print("\nDeleting item with barcode 12345:")
    inventory.delete_item("12345")
    print(inventory.items)

if __name__ == "__main__":
    main()
