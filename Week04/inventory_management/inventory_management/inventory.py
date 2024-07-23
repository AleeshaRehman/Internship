from datetime import datetime, timedelta
from .food_item import FoodItem
import csv

class Inventory:
    def __init__(self, file_name="inventory.csv"):
        self.items = []
        self.file_name = file_name
        self.load_items()

    def load_items(self):
        try:
            with open(self.file_name, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item = FoodItem(
                        name=row['name'],
                        category=row['category'],
                        quantity=int(row['quantity']),
                        barcode=row['barcode'],
                        expiry_date=row['expiry_date']
                    )
                    self.items.append(item)
        except FileNotFoundError:
            print(f"{self.file_name} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading inventory: {e}")

    def save_items(self):
        try:
            with open(self.file_name, mode='w', newline='') as file:
                fieldnames = ['name', 'category', 'quantity', 'barcode', 'expiry_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for item in self.items:
                    writer.writerow({
                        'name': item.name,
                        'category': item.category,
                        'quantity': item.quantity,
                        'barcode': item.barcode,
                        'expiry_date': item.expiry_date.strftime('%Y-%m-%d')
                    })
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item):
        self.items.append(item)
        self.save_items()

    def edit_item(self, barcode, **kwargs):
        item = self.search_item_by_barcode(barcode)
        if item:
            for key, value in kwargs.items():
                if key in item.__dict__:
                    if key == 'expiry_date':
                        value = datetime.strptime(value, "%Y-%m-%d")
                    setattr(item, key, value)
            self.save_items()
            return True
        return False

    def delete_item(self, barcode):
        item = self.search_item_by_barcode(barcode)
        if item:
            self.items.remove(item)
            self.save_items()
            return True
        return False

    def search_item_by_barcode(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                return item
        return None

    def search_item_by_name(self, name):
        return [item for item in self.items if item.name == name]

    def search_item_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def get_near_expiry_items(self, days=7):
        near_expiry = []
        current_date = datetime.now()
        for item in self.items:
            if 0 <= (item.expiry_date - current_date).days <= days:
                near_expiry.append(item)
        return near_expiry

    def __iter__(self):
        return iter(self.items)

    def near_expiry_generator(self, days=7):
        current_date = datetime.now()
        for item in self.items:
            if 0 <= (item.expiry_date - current_date).days <= days:
                yield item
