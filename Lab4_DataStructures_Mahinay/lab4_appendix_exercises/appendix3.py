# ==========================================
# STUDENT-SPECIFIC INPUTS
# ==========================================
LAST_NAME = "Mahinay"
STUDENT_ID = "TUPM-26-4014"
SEED_NUM = int(STUDENT_ID [-1])
FAVORITE_ARTIST = "AVRIL LAVIGNE"

# ==========================================================
# EXERCISE 3: TRANSACTION HISTORY ANALYZER
# ==========================================================
print("\n------------------------------------------------------------")
print("EXERCISE 3: TRANSACTION HISTORY ANALYZER")
print("------------------------------------------------------------")

customers = [f"{LAST_NAME}_C1", f"{LAST_NAME}_C2", f"{LAST_NAME}_C3", f"{LAST_NAME}_C4", f"{LAST_NAME}_C5"]
products_prices = {"NOTEBOOK": 50.00, "PEN": 20.00, "USB": 350.00, "HEADPHONES": 750.00, "CALCULATOR": 1200.00}

raw_transactions = [
    {"customer": customers[0], "product": "NOTEBOOK", "quantity": 3},
    {"customer": customers[1], "product": "PEN", "quantity": 10},
    {"customer": customers[2], "product": "USB", "quantity": 2},
    {"customer": customers[3], "product": "HEADPHONES", "quantity": 1},
    {"customer": customers[4], "product": "CALCULATOR", "quantity": 1},
    {"customer": customers[0], "product": "NOTEBOOK", "quantity": 3} # Repeated Purchase
]

print("\n--- Exercise 3 Assessment Data ---")

# 1. Generated Transaction Records
print("\n1. Generated Transaction Records:")
for i, tx in enumerate(raw_transactions, 1):
    print(f"   Transaction {i}: {tx}")

# 2. Organized Transaction Data
organized_transactions = [{**tx, "unit_price": products_prices[tx["product"]], "total_value": products_prices[tx["product"]] * tx["quantity"]} for tx in raw_transactions]
print("\n2. Organized Transaction Data:")
for i, tx in enumerate(organized_transactions, 1):
    print(f"   Organized {i}: {tx}")

# 3. Repeated/Distinct Transactions
seen_tx = set()
distinct_transactions = []
repeated_transactions = []
for tx in raw_transactions:
    key = (tx["customer"], tx["product"], tx["quantity"])
    if key in seen_tx:
        repeated_transactions.append(tx)
    else:
        seen_tx.add(key)
        distinct_transactions.append(tx)

print("\n3. Repeated/Distinct Transactions:")
print(f"   Distinct Count: {len(distinct_transactions)}")
print(f"   Repeated: {repeated_transactions}")

# 4. Transaction Values
print("\n4. Transaction Values:")
for i, tx in enumerate(organized_transactions, 1):
    print(f"   Transaction {i} Total Value: PHP {tx['total_value']:,.2f}")

# 5. Customer Summaries
customer_summaries = {}
for tx in organized_transactions:
    customer_summaries[tx["customer"]] = customer_summaries.get(tx["customer"], 0) + tx["total_value"]
print("\n5. Customer Summaries:")
print(f"   Total Spending per Customer: {customer_summaries}")

# 6. Product Summaries
product_summaries = {}
for tx in organized_transactions:
    p = tx["product"]
    if p not in product_summaries:
        product_summaries[p] = {"total_qty": 0, "total_revenue": 0}
    product_summaries[p]["total_qty"] += tx["quantity"]
    product_summaries[p]["total_revenue"] += tx["total_value"]
print("\n6. Product Summaries:")
for p, stats in product_summaries.items():
    print(f"   Product {p}: {stats}")

# 7. Ordered Results
ordered_transactions = sorted(organized_transactions, key=lambda x: x["total_value"], reverse=True)
print("\n7. Ordered Results (Sorted by Value Descending):")
for i, tx in enumerate(ordered_transactions, 1):
    print(f"   Rank {i}: {tx['customer']} - {tx['product']} (PHP {tx['total_value']})")

# 8. Overall Transaction Summary
grand_total = sum(customer_summaries.values())
print("\n8. Overall Transaction Summary:")
print(f"   Grand Total Revenue: PHP {grand_total:,.2f}")

# Final Output (Exercise 3)
print("\nFinal Output: Final Consolidated Transaction Report")
print("=" * 65)
print(f"{'Customer':<15} | {'Product':<12} | {'Qty':<5} | {'Total Value'}")
print("-" * 65)
for tx in organized_transactions:
    print(f"{tx['customer']:<15} | {tx['product']:<12} | {tx['quantity']:<5} | PHP {tx['total_value']:,.2f}")
print("=" * 65)
print(f"GRAND TOTAL REVENUE: PHP {grand_total:,.2f}")
print("=" * 65)