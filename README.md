# BestBuy Store Management System

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Masterschool](https://img.shields.io/badge/Masterschool-Bootcamp-orange)
![Platform](https://img.shields.io/badge/Platform-Terminal%20%2B%20HTML-lightgrey)

A sleek, command-line interface (CLI) application developed in Python for managing a retail store's inventory and processing customer orders.

## 🚀 Features

- **Inventory Management**: Track product details including name, price, and stock levels.
- **Dynamic Product States**: Automatically deactivates products when they go out of stock.
- **Order Processing**: Efficiently handle multi-product orders with real-time stock updates.
- **Interactive CLI**: User-friendly menu system with colorful terminal output for better readability.
- **Robust Validation**: Built-in error handling for invalid inputs, negative prices, and over-purchasing.

## 📁 Project Tree

```text
.
├── main.py        # Entry point & CLI Menu
├── products.py    # Product class & logic
├── store.py       # Store class & ordering
└── README.md      # Documentation
```

## 📋 Requirements & Dependencies

- **Python 3.10+** (Recommended)
- **Standard Libraries**: This project uses only Python standard libraries, so no external `pip` installations are required:
  - `typing`: For type hinting.
  - `os/sys`: For system-level interactions.
- **Terminal**: A terminal that supports ANSI color codes (for GREEN/RED highlights).

## 🕹️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lcetin66/bestbuy.git
   cd BestBuy
   ```

2. **Execute the program**:
   ```bash
   python3 main.py
   ```

## 📖 Usage

Once the program is running, you will be presented with the following menu:

1. **List all products in store**: Displays all currently active products, their prices, and remaining stock.
2. **Show total amount in store**: Shows the cumulative count of all items available across all products.
3. **Make an order**: Allows you to select products by number and specify quantities to purchase.
4. **Quit**: Safely exits the application.

## 🧪 Example

```text
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

Please choose a number: 1

Products in store:
1. MacBook Air M2, Price: $1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500
3. Google Pixel 7, Price: $500, Quantity: 250
------
```

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
