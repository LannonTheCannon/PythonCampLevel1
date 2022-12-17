import tkinter as tk
from tkinter import *

def getApp1():
    # contain the information based on appetizer #001
    appItem1 = 'Galaxy Fries'
    appItem1Price = 5.99
    appItem1Data = [appItem1, appItem1Price]

    message = appItem1Data[0] + ('.' * 12) + '$' + str(appItem1Data[1])
    #print(appItem1, appItem1Price)
    lbCart.insert(END, message)

def deleteItem():
    selected_item = lbCart.curselection()
    lbCart.delete(selected_item)

def createReceipt():
    # We need to grab everything from our list box
    items = lbCart.get(0, END)

    # for loop
    for item in items:
        # Examine each item in the list
        # Find its price point
        price_point = item.find('$')
        item_price = item[price_point:]
        item_price = item_price.strip('$')
        item_price = float(item_price)

# main window
root = tk.Tk()
root.geometry('1000x700')
root.title('Restaurant At the Edge of the Universe')

# Title bar
titleFrame = Frame(root, bg = '#132A13', bd = 5, relief = RAISED, width = 1000,
                   height = 50)
titleFrame.propagate(0)
titleFrame.pack(side = TOP)

# Title Label
lblTitle = Label(titleFrame, bg = '#132A13', fg = 'cornsilk', width = 40,
                 height = 2, text = 'Restaurant at The Edge of the Universe',
                 font = 'arial 16 bold')
lblTitle.pack()

# mainframe
mainFrame = Frame(root, bg = '#588157', bd = 5, relief = RAISED, width = 1000,
                  height = 450)
mainFrame.pack(side = TOP)

receiptFrame = Frame(root, bg = 'grey30', bd = 5, relief = SUNKEN, width = 1000,
                     height = 200)
receiptFrame.pack(side = TOP)

#############################################################################

itemCart = Frame(receiptFrame, bg = 'grey40', bd = 5, relief = SUNKEN, width = 500,
                 height = 200)
itemCart.propagate(0)
itemCart.pack(side = LEFT)

lbCart = Listbox(itemCart, width = 80, height = 10, font = 'arial 16')
lbCart.pack()

finalOrder = Frame(receiptFrame, bg = 'grey40', bd = 5, relief = SUNKEN, width = 500,
                 height = 200)
finalOrder.pack(side = RIGHT)

# Add Two buttons to the program
# Delete the item that we no longer want
btnDelete = Button(itemCart, bg = 'red', fg = 'cornsilk', width = 8, height = 1,
                   text = 'Delete', font = 'consolas 15 bold', command = deleteItem)
btnDelete.place(x = 389, y = 0)

btnPurchase = Button(itemCart, bg = 'red', fg = 'cornsilk', width = 8, height = 1,
                   text = 'Purchase', font = 'consolas 15 bold', justify = LEFT,
                     command = createReceipt)
btnPurchase.place(x = 389, y = 127)

##############################################################################

appFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
appFrame.propagate(0)
appFrame.pack(side = LEFT)

appTitle = Label(appFrame, bg = 'grey', font = 'consolas 16 bold', text = 'Appetizers',
                 width = 20, height = 2)
appTitle.pack(side = TOP)

appItem1 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold', command = getApp1)
appItem1.pack(side = TOP)

appItem2 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem2.pack(side = TOP)

appItem3 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem3.pack(side = TOP)

appItem4 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem4.pack(side = TOP)

appItem5 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem5.pack(side = TOP)

##############################################################################

entFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
entFrame.pack(side = LEFT)

##############################################################################

desFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
desFrame.pack(side = LEFT)

##############################################################################

drinkFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
drinkFrame.pack(side = LEFT)

##############################################################################

root.mainloop()
