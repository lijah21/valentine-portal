print("--- Advanced Tip Calculator ---")

bill = float(input("What was the total bill? $"))
tax_rate = 0.08  # 8% Sales Tax
bill_with_tax = bill * (1 + tax_rate)

tip_percentage = int(input("Tip percentage (10, 12, 15)? "))
people = int(input("How many people? "))

# LOGIC CHALLENGE: Check if people is 0
if people <= 0:
    print("Error: You need at least 1 person to pay the bill!")
else:
    total_bill = bill_with_tax * (1 + (tip_percentage / 100))
    final_amount = round(total_bill / people, 2)
    print(f"Including 8% tax, each person owes: ${final_amount:.2f}")