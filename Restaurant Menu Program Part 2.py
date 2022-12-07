# Restuarant Menu Program Part 2 (If and Else Strategy)

def show_app_menu():
    # Show the user the menu for appetizer items
    print('-' * 60)
    print('\n') # Escape Character: make a new line
    print('\t\t\tAppetizers'.upper())
    print('\n')
    print('''
1. Galaxy Fries ................................. $ 5.99
2. White Drawf Milk Shake ....................... $ 6.50
3. Black Hole Nuggets ........................... $ 8.50
4. Dark Matter Salad ............................ $ 6.50
5. Cosmos Cut Fries ............................. $ 8.99 
''')
    print('-' * 60)

def show_entree_menu():
    # Show the user the menu for entree items
    print('-' * 60)
    print('\n') 
    print('\t\t\tEntree'.upper())
    print('\n')
    print('''
1. Galaxy Burger ................................. $ 12.99
2. Blue Giant Fish Steak ......................... $ 14.50
3. Red Drawf Sun Sprouts ......................... $ 11.50
4. Scorpio Sun Steak ............................. $ 10.50
5. Gemini Callimari  ............................. $ 15.99 
''')
    print('-' * 60)

def show_dessert_menu():
    # Show the user the menu for entree items
    print('-' * 60)
    print('\n') 
    print('\t\t\tDessert'.upper())
    print('\n')
    print('''
1. Mushroom Mochi Balls .......................... $ 4.99
2. White Forest Cheese Cake ...................... $ 6.50
3. Milkyway Milkshake ............................ $ 7.50
4. Orange Star Cake............................... $ 3.50
5. Super Nova Short Cake  ........................ $ 5.99 
''')
    print('-' * 60)

def show_drink_menu():
    # Show the user the menu for entree items
    print('-' * 60)
    print('\n') 
    print('\t\t\tDrinks'.upper())
    print('\n')
    print('''
1. Coca Cola ..................................... $ 4.99
2. Pepsi Cola .................................... $ 3.50
3. Sprite ........................................ $ 7.50
4. Orange Soda ................................... $ 3.50
5. Intergalactic Gargle Blaster ................ $ 304.99 
''')
    print('-' * 60)


orderList = []
subtotal = 0 

print('\tRestaurant at the Edge of the Universe')

print('\n')

isApp = input('Would you like to order an appetizer [yes] or [no]: ').lower()

if isApp == 'yes': 

    show_app_menu()
    # Ask the user to make a choice on the menu
    app_choice = int(input('Please enter the number of the appetizer you would like: '))
    # If the app_choice falls within the numebrs 1 - 5 , else: display that item is not on the menu
    if app_choice >= 1 and app_choice <= 5:
        # to check to see if the user ordered galaxy fries?
        if app_choice == 1:
            app_item = 'Galaxy Fries'
            app_price = 5.99
            
        elif app_choice == 2:
            app_item = 'White Drawf Milk Shake'
            app_price = 6.50

        elif app_choice == 3:
            app_item = 'Black Hole Nuggets'
            app_price = 8.50
            
        elif app_choice == 4:
            app_item = 'Dark Matter Salad'
            app_price = 6.50
            
        else:
            app_item = 'Cosmos Cut Fries'
            app_price = 8.99

        print(f'You chose the {app_item} for ${app_price}.')
        orderList.append(app_item)

        
        # Ask the user for how many of that particular item that they would like make
        app_quant = int(input(f"Please enter the number of {app_item} that you would like to order: "))
        # This value should store the price of the item the user chose * the quantity 
        app_subtotal = app_price * app_quant
        subtotal = subtotal + app_subtotal 

    else:
        print('That item is not on the list!')

isEntree = input('Would you like to order an entree [yes] or [no]: ').lower()

# If the answer to this question is yes, then show the entree menu
if isEntree == 'yes':

    show_entree_menu()

    entree_choice = int(input('Please enter the number of the item you would like to order: '))

    if entree_choice >= 1 and entree_choice <= 5:
        # to check to see if the user ordered galaxy fries?
        if entree_choice == 1:
            entree_item = 'Galaxy Burger'
            entree_price = 12.99
            
        elif entree_choice == 2:
            entree_item = 'Blue Giant Fish Steak'
            entree_price = 14.50

        elif entree_choice == 3:
            entree_item = 'Red Drawf Sun Sprouts'
            entree_price = 11.50
            
        elif entree_choice == 4:
            entree_item = 'Scorpio Sun Steak'
            entree_price = 10.50
            
        else:
            entree_item = 'Gemini Callimari'
            entree_price = 15.99

        print(f'You chose the {entree_item} for ${entree_price}.')

        # Ask the user for how many of that particular item that they would like make
        ent_quant = int(input(f"Please enter the number of {app_item} that you would like to order: "))
        # This value should store the price of the item the user chose * the quantity 
        ent_subtotal = entree_price * ent_quant
        subtotal = subtotal + ent_subtotal 
        
    else:
        print('This item is not on the list!')
#############################################################################################


isDrink = input('Would you like to order an drink [yes] or [no]: ').lower()

# If the answer to this question is yes, then show the entree menu
if isDrink == 'yes':

    show_drink_menu()

    drink_choice = int(input('Please enter the number of the item you would like to order: '))

    if drink_choice >= 1 and drink_choice <= 5:
        # to check to see if the user ordered galaxy fries?
        if drink_choice == 1:
            drink_item = 'Coca Cola'
            drink_price = 4.99
            
        elif drink_choice == 2:
            drink_item = 'Pepsi Cola'
            drink_price = 3.50

        elif drink_choice == 3:
            drink_item = 'Sprite'
            drink_price = 7.59
            
        elif drink_choice == 4:
            drink_item = 'Orange Soda'
            drink_price = 3.50
            
        else:
            drink_item = 'Intergalactic Gargle Blaster'
            drink_price = 304.99

        print(f'You chose the {drink_item} for ${drink_price}.')
        # Ask the user for how many of that particular item that they would like make
        drink_quant = int(input(f"Please enter the number of {app_item} that you would like to order: "))
        # This value should store the price of the item the user chose * the quantity 
        drink_subtotal = drink_price * drink_quant
        subtotal = subtotal + drink_subtotal 
        
    else:
        print('This item is not on the list!')

sales_tax = 0.07 * subtotal
grand_total = sales_tax + subtotal

print(f'Your subtotal comes out to ${round(subtotal,2)}')
print(f'Your Sales tax comes out to ${round(sales_tax,2)}')
print(f'Your Grand total comes out to ${round(grand_total,2)}')
