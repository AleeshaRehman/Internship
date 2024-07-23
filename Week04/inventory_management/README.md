# Inventory Management System

## Overview

The Inventory Management System (IMS) is a Python-based application designed to manage and organize information about food items in a stock inventory. It provides functionalities for CRUD operations, searching, filtering, and reporting.

## Features

- **Real-Time Data Handling**: Manage inventory data with CRUD operations and handle items nearing expiry.
- **Efficient Data Storage**: Store food items with attributes such as name, category, quantity, barcode, and expiry date.
- **User Interaction**: User-friendly, menu-driven interface for managing inventory.
- **Sorting & Filtering**: Prioritize and filter items based on expiry dates and categories.
- **Search & Reporting**: Search items by barcode, name, or category and generate various reports.

## File Structure

The project consists of the following files:

- `food_item.py`: Defines the `FoodItem` class, representing individual food items.
- `inventory.py`: Defines the `Inventory` class, managing the overall inventory with CRUD operations and other functionalities.
- `__init__.py`: Initializes the package and contains example usage of the `Inventory` and `FoodItem` classes.
- `main.py`: The main script to demonstrate the usage of the package. Run this script to interact with the Inventory Management System.

## Requirements

- Python 3.12 or higher
- No additional libraries are required beyond the Python standard library.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd <project_directory>
   ```

3. **Run the Main Script:**

   ```bash
   python main.py
   ```

   This will create an `inventory.csv` file if it does not exist and allow you to interact with the inventory system.

## Usage

1. **Adding Items:**
   - Create instances of `FoodItem` and add them to the inventory using the `add_item` method.

2. **Editing Items:**
   - Edit existing items in the inventory by specifying the barcode and the fields to be updated using the `edit_item` method.

3. **Deleting Items:**
   - Remove items from the inventory by specifying their barcode using the `delete_item` method.

4. **Searching Items:**
   - Search for items by barcode or name using the `search_item_by_barcode` and `search_item_by_name` methods.

5. **Viewing Near Expiry Items:**
   - List items nearing their expiry within a specified number of days using the `near_expiry_generator` method.

6. **Generating Reports:**
   - Generate reports on near expiry items, low stock items, and category summaries using the `generate_report` method.
```
