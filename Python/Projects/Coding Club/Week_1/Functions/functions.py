# ----------  EXAMPLE 1  ---------- 
def display_invoice(username, amount, due_date):
   print(f"Hello {username}")
   print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 100.01, "01/02")

# ----------  EXAMPLE 2  ---------- 
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)