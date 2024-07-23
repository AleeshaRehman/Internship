from datetime import datetime

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

    def __repr__(self):
        return (f"FoodItem(name={self.name}, category={self.category}, quantity={self.quantity}, "
                f"barcode={self.barcode}, expiry_date={self.expiry_date.strftime('%Y-%m-%d')})")
