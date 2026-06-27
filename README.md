# skin-care-Administration-till-operation-purchasing-
Kasir Skincare is a Python desktop cashier/POS (Point of Sale) app for a skincare store, built with tkinter. It covers product selection, cart management, payment processing, receipt printing, discount logic, and sales history.



**Kasir Skincare** is a Python desktop cashier/POS (Point of Sale) app for a skincare store, built with `tkinter`. It covers product selection, cart management, payment processing, receipt printing, discount logic, and sales history.Here's everything you need for the GitHub description:

---

## What is this project?

A desktop POS (Point of Sale) cashier application for a skincare store, built with Python and `tkinter`. It lets a cashier process sales transactions, apply automatic discounts, print receipts, and review historical sales — all through a simple GUI.

---

## Features implemented

**Product catalog** — 5 brands (Wardah, Emina, Azarine, Somethinc, Hada Labo) with 5 products each (sunscreen, moisturizer, toner, facial wash, serum), all hardcoded in a dictionary with prices in IDR.

**Transaction flow** — the cashier selects a brand from a dropdown, which dynamically populates a product dropdown; they pick a quantity with a spinner and add items to a cart. Multiple products can be added before checkout.

**Shopping cart** — a `ttk.Treeview` table shows all cart items (brand, product name, quantity, subtotal) and updates in real time. A running total is displayed below the table.

**Discount logic** — if the cart total exceeds Rp 150,000, a 10% discount is automatically applied at checkout.

**Payment processing** — the cashier enters the amount tendered; the app validates it's sufficient, calculates change, and blocks underpayment with a warning.

**Receipt (struk)** — a popup window shows a formatted receipt with all items, the total, discount, amount paid, and change.

**CSV persistence** — every completed transaction is appended to `history_penjualan.csv`, with columns for date/time, brand, product, quantity, unit price, subtotal, total, discount, and final amount paid.

**Sales history viewer** — opens a separate window showing all past transactions read from the CSV in a scrollable table.

---

## Functions

| Function | Purpose |
|---|---|
| `init_csv()` | Creates the CSV file with headers if it doesn't exist yet |
| `tampilan_menu_utama()` | Renders the main menu with three buttons |
| `transaksi_baru()` | Resets the cart and loads the transaction screen |
| `tampilan_transaksi()` | Builds the two-panel transaction UI (product picker + cart) |
| `update_produk()` | Populates the product dropdown when a brand is selected |
| `tambah_keranjang()` | Validates inputs and adds the selected item to the cart |
| `update_keranjang()` | Refreshes the cart table and recalculates the running total |
| `proses_bayar()` | Validates payment, applies discount, triggers receipt and CSV save |
| `cetak_struk()` | Formats and displays the receipt in a messagebox popup |
| `simpan_ke_csv()` | Appends each cart item as a row in the CSV with transaction metadata |
| `lihat_riwayat()` | Opens a new window and reads/displays all rows from the CSV |

---

## Tech stack

- **Python 3** — standard library only, no external packages needed
- **tkinter + ttk** — GUI framework (built into Python)
- **csv** — for reading/writing the sales log
- **datetime** — for timestamping transactions
- **os** — for checking whether the CSV already existsYou can paste the description section directly into your GitHub repo's `README.md`. Let me know if you'd like me to generate a full formatted `README.md` file for download instead.
