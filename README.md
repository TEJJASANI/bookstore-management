# Bookstore Management

A simple Python-based bookstore management system that lets you manage inventory, record sales, and visualize revenue using charts.

## Features

- Add new books with title, author, genre, price, and quantity.
- Update stock quantities for existing books.
- Record sales with date, title, and quantity sold.
- View sales summary with total revenue and top-selling books.
- Visualize:
  - Sales by genre (bar chart).
  - Revenue share by genre (pie chart).
  - Monthly revenue trend (line chart).
- Data persistence using CSV files:
  - `inventory.csv`
  - `sales.csv`

## Requirements

- Python 3.12 (or compatible)
- `pandas`
- `matplotlib`
- `seaborn`

Install dependencies:


## How to Run

1. Clone the repository:

2. Run the main script:

3. Use the menu in the terminal:
- `1` Add book  
- `2` Update inventory quantity  
- `3` Record sale  
- `4` Show sales summary  
- `5` Show charts  
- `6` Save & Exit  

## File Structure

- `bookstore_system.py` – main application file with the `Bookstore` class and menu system.
- `inventory.csv` – inventory data (auto-created if missing).
- `sales.csv` – sales data (auto-created if missing).

## License

This project is for learning and personal use.  
You may adapt or extend it as needed.
