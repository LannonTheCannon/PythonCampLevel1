import tkinter as tk
from tkinter import *
from tkmacosx import Button

class RestaurantMenu:

    def __init__(self):
        self.frames = []
        self.labels = []
        self.buttons = []

        self.apps = ['galaxy 1','galaxy 2','apple 3', 'orange 4', 'marigold 5']
        self.prices = ['$3.99','$5.99','$6.00','$14.50','$7.80','$12.50']

        self.root = Tk()
        self.root.title("Restaurant Menu Program")
        self.drawArea()

    def drawArea(self):
        titleFrame = tools.createFrame(self.root, 1000, 100, 'raised',15)
        titleFrame.propagate(0)
        titleFrame.pack()
        self.frames.append(titleFrame)

        lblTitle = tools.createLabel(titleFrame, 50, 20, 'Restaurant At the Edge of the Universe', 'flat',
                                    'arial 22 bold')
        lblTitle.pack()
        self.labels.append(lblTitle)

        mainFrame = tools.createFrame(self.root, 1000, 400, 'raised', 5)
        mainFrame.propagate(0)
        mainFrame.pack()
        self.frames.append(mainFrame)

        ###############################################################################
        appFrame = tools.createFrame(mainFrame, 248, 400, 'raised', 5)
        appFrame.propagate(0)
        appFrame.pack(side = LEFT)
        self.frames.append(appFrame)

        lblApp1 = tools.createLabel(appFrame, 20, 3, 'Appetizers', 'flat', 'arial 17 bold')
        lblApp1.pack(side = TOP)
        self.labels.append(lblApp1)

        for x in range(0,5):
            btnItem = tools.createButton(appFrame, 100, 20, 'raised', 5, self.apps[x],
                                         lambda x = x:  self.onClick(x))
            btnItem.pack(side = TOP, pady = 5)
            self.buttons.append(btnItem)

        #########################################
        entFrame = tools.createFrame(mainFrame, 248, 400, 'raised', 5)
        entFrame.propagate(0)
        entFrame.pack(side = LEFT)
        self.frames.append(entFrame)

        #########################################
        desFrame = tools.createFrame(mainFrame, 248, 400, 'raised', 5)
        desFrame.propagate(0)
        desFrame.pack(side = LEFT)
        self.frames.append(desFrame)

        #########################################
        drinkFrame = tools.createFrame(mainFrame, 248, 400, 'raised', 5)
        drinkFrame.propagate(0)
        drinkFrame.pack(side = LEFT)
        self.frames.append(drinkFrame)
        ###############################################################################

        botFrame = tools.createFrame(self.root, 1000, 150, 'raised', 5)
        botFrame.propagate(0)
        botFrame.pack()
        self.frames.append(botFrame)

        self.lbBox = tools.createListBox(botFrame, 60, 15, 'raised', 5, 'arial 12')
        self.lbBox.pack(side = LEFT)

        #########################################
        midFrame = tools.createFrame(botFrame, 100, 150, 'raised', 5)
        midFrame.propagate(0)
        midFrame.pack(side = LEFT)
        self.frames.append(midFrame)

        btnDelete = tools.createButton(midFrame, 70, 30, 'raised', 2, 'delete', self.deleteItem)
        btnDelete.propagate(0)
        btnDelete.pack(side = TOP)
        self.buttons.append(btnDelete)

        btnPurch = tools.createButton(midFrame, 70, 30, 'raised', 2, 'Purchase', self.purchaseAll)
        btnPurch.propagate(0)
        btnPurch.pack(side=TOP)
        self.buttons.append(btnPurch)

        #########################################
        receiptFrame = tools.createFrame(botFrame, 400, 150, 'raised', 5)
        receiptFrame.propagate(0)
        receiptFrame.pack(side=LEFT)
        self.frames.append(receiptFrame)

        self.lblReceipt = tools.createLabel(receiptFrame, 100, 20, '', 'raised', 'arial 15 bold')
        self.lblReceipt.propagate(0)
        self.lblReceipt.pack(side = LEFT)
        self.labels.append(self.lblReceipt)

    def onClick(self, i):
        # Add each item information into the listbox
        message = self.apps[i] + '.'*30 + self.prices[i]
        self.lbBox.insert(END, message)
        return

    def deleteItem(self):
        selected_item = self.lbBox.curselection()
        self.lbBox.delete(selected_item)

    def purchaseAll(self):
        # First get all the items in the list box
        all_items = self.lbBox.get(0, END)

        # Create an empty subtotal to hold the incrementing costs
        subtotal = 0
        for item in all_items:
            price_point = item.find('$')
            price = item[price_point:]

            # Drop the dollar sign from each string
            price = float(price.lstrip('$'))

            # Accumulate the grand total
            subtotal += price

        print(subtotal)
        TAX_RATE = 0.0725
        sales_tax = TAX_RATE * subtotal
        grand_total = sales_tax + subtotal

        message = f'''
Subtotal: $ {subtotal}
Sales Tax: $ {sales_tax}
Grand Total: $ {grand_total}
'''

        self.lblReceipt.configure(text = message)

class TKools:
    def createLabel(self, parent, width, height, text, relief, font):
        newLabel = Label(parent, width = width, height =height, text = text, relief = relief, font = font)
        return newLabel

    def createFrame(self, parent, width, height, style, border):
        newFrame = Frame(parent, width = width, height = height, relief = style, bd = border)
        return newFrame

    def createButton(self, parent, width, height, style, border, text, action):
        newButton = Button(parent, width = width, height = height, relief = style, bd = border,
                            text = text, command = action)
        return newButton

    def createListBox(self, parent, width, height, style, border, font):
        newLB = Listbox(parent, width = width, height = height, relief = style, bd = border,
                     font = font)
        return newLB

tools = TKools()
window = RestaurantMenu()
window.root.mainloop()