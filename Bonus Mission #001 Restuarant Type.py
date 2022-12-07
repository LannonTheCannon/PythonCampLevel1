# Bonus Mission #001 Restuarant Type

# Think about a specific food item that you would like to sell and welcome the user to your restuarant
restuarant = 'Restuarant at the Edge of the Universe'
print(f'Welcome to the {restuarant}!')

# Ask the user how many items that they would like to purchase.
dumplings = int(input('How many dumplings would you like to purchase: '))

# Create a variable that stores the price of the item 
dumpling_price = 13.99

# Identify how much their subtotal is
subtotal = dumplings * dumpling_price

# Create a variable that stores the tax rate
tax_rate = 0.0725

# Calculate the sales tax
sales_tax = subtotal * tax_rate

# Calculate the grandtotal
grand_total = subtotal + sales_tax

# Tell the user how much their subtotal is, tax_rate, and the sales tax. Also include the grandtotal
print(f'''

1) dumplings .............x{dumplings}

+++++++++++++++++++++++++++++++++

subtotal.................. ${subtotal}
tax_rate ................. {tax_rate}%
sales_tax ................ ${sales_tax}

++++++++++++++++++++++++++++++++++

grand_total............... ${grand_total}

''')












