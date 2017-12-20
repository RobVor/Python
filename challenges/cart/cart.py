import os, sys, logging

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
logging.disable(logging.DEBUG)

#Variables and Constants
logging.debug('Initializing Variables.')

CART = []
ITEMS = [1, 2, 3, 4]
DESC = ['Coke', 'Kit Kat', 'Bar One', 'Fanta']
QTY = 0
PRICES = [7.50, 9.50, 8.50, 7.50]
TOTAL = 0

#Classes (And exceptions)
logging.debug('Initializing custom Classes.')

class NoInput(Exception):
    pass

#Functions
logging.debug('Initializing custom Functions.')

def CLSC():
    os.system("cls" if os.name == "nt" else "clear")

def ItemGrid(GridItems):
    logging.debug('Generating print view of items.')
    print('Items', 'Description', 'Quantity', 'Price', sep = "        ")
    i = 0
    for n in GridItems:
        print('{:^5}'.format(n[i]),'{:<6}'.format(''),'{:<11}'.format(n[i + 1]),'{:<6}'.format(""),'{:^8}'.format(n[i + 2]),'{:<8}'.format(""),'{:<8}'.format(n[i + 3]))
    print()

def CartView():
    CLSC()
    TOTAL = 0
    logging.debug('Viewing cart content.')
    if len(CART) < 1:
        print('Your cart is currently empty.')
        print()
        print("""
        [1] - Add items to cart
        [2] - Return to main menu

        """)
        try:
            OPTION = int(input('What do you want to do? '))
            if OPTION == 1:
                logging.debug('Option 1 of CartView selected.')
                CartAdd()
            elif OPTION == 2:
                logging.debug('Option 2 of CartView selected.')
            else:
                logging.debug('Invalid selection of CartView.')
                x = input('Invalid selection made. Please try again.')
                CartView()
        except Exception as e:
            logging.exception(e)
            x = input('Invalid selection made. Please try again.')
            CartView()
    else:
        ItemGrid(CART)
        for n in CART:
            TOTAL = TOTAL + float(n[2] * n[3])
        print('Cart Total: ',TOTAL)
        TOTAL = 0
        print('Your cart has the above items.')
        print()
        print("""        
        [1] - Add items to cart
        [2] - Remove items from cart
        [3] - Return to main menu

        """)
        try:
            OPTION = int(input('What do you want to do? '))
            if OPTION == 1:
                logging.debug('Option 1 of CartView selected.')
                CartAdd()
            elif OPTION == 2:
                logging.debug('Option 2 of CartView selected.')
                CartRemove()
            elif OPTION == 3:
                logging.debug('Option 3 of CartView selected.')
            else:
                logging.debug('Invalid selection of CartView.')
                x = input('Invalid selection made. Please try again.')
                CartView()
        except Exception as e:
            logging.exception(e)
            x = input('Invalid selection made. Please try again.')
            CartView()
        
    
def CartAdd():
    CLSC()
    logging.debug('Adding items to cart.')
    print('The following items are available.')
    ItemGrid(ShopView())
    ID = int(input('Select the item number to add to your cart: '))
    QTY = int(input('How many of do you want? '))
    if len(CART) == 0:
        logging.debug('Adding item ' + str(ID) + ' to cart.')
        CART.append([ITEMS[ID - 1], DESC[ID - 1], QTY, PRICES[ID - 1]])
        return CART
    else:
        for n in CART:
            if ID in n:
                print('True')
                logging.debug('Item already exists, adding one to quantity')
                n[2] += QTY
                break
            else:
                print('False')
                logging.debug('Adding item ' + str(ID) + ' to cart.')
                CART.append([ITEMS[ID - 1], DESC[ID - 1], QTY, PRICES[ID - 1]])
                break
        return CART

def CartRemove():
    CLSC()
    TOTAL = 0
    logging.debug('Removing items from cart.')
    ItemGrid(CART)
    for n in CART:
        TOTAL = TOTAL + float(n[2] * n[3])
    print('Cart Total: ',TOTAL)
    TOTAL = 0
    print('Your cart has the above items.')
    print()
    OPTION = int(input('Select the item number that you wish to remove.'))
    for n in CART:
        if OPTION in n:
            try:
                while True:
                    QTY = int(input('How many items do you want to remove? '))
                    if QTY > n[2]:
                        logging.debug('Amount is to high.')
                        print('You do not have that many items, please try again.')
                    elif (QTY < n[2]) or (QTY == None):
                        logging.debug('No value or low value supplied.')
                        logging.debug('We can remove', QTY, 'items.')
                        n[2] -= QTY
                        break
                    elif QTY == n[2]:
                        logging.debug('Removing item from cart entirely.')
                        r = CART.index(n)
                        del CART[r]
                        break
            except Exception as e:
                logging.debug(str(e))
        else:
            logging.debug('No item given.')
            print('There is no item with that id.')
            CartRemove()

def ShopView():
    CLSC()
    SHOP = []
    logging.debug('Showing store items available.')
    for n in range(len(ITEMS)):
        SHOP.append([ITEMS[n], DESC[n], QTY, PRICES[n]])
    return SHOP

def main():
    try:
        while True:
            CLSC()
            logging.debug('Main function.')
            print("""
            Welcome to the Shop.

            [1] - View store items
            [2] - View cart items
            [3] - Add items to cart
            [4] - Remove items from cart
            [5] - Exit

            """)
            ACTION = int(input('What would you like to do? (Use number for selections) '))
            if ACTION == 1:
                logging.debug('Option 1 selected.')
                ItemGrid(ShopView())
                wait = input('Press <Return> to continue ')
            elif ACTION == 2:
                logging.debug('Option 2 selected.')
                CartView()
            elif ACTION == 3:
                logging.debug('Option 3 selected.')
                CartAdd()
            elif ACTION == 4:
                logging.debug('Option 4 selected.')
                CartRemove()
            elif ACTION == 5:
                logging.debug('Option 5 selected.')
                logging.debug('Goodbye.')
                sys.exit()
            
    except Exception as e:
        logging.exception(e)
        main()

#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

main()

#End
logging.debug('Program end and cleanup.')
