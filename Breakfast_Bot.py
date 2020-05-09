import time

def print_pause(message):
    print(message)
    time.sleep(2)

def valid_input(prompt, opt1, opt2):
    while True:
        response = input(prompt).lower()
        if opt1 in response:
            break
        elif opt2 in response:
            break
        else:
            print_pause("Sorry, I do not understand.")
    return response

def get_order():
    response = valid_input("Please place your order.  Would you like waffles or pancakes?\n", "waffles", "pancakes").lower()
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    reorder()
    
def reorder():
    response = valid_input("Would you like to order again? Yes or No?\n", "no", "yes").lower()
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I am happy to take your order.")
        get_order()
       
def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.") 
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def order_breakfast():
    intro()
    while True:
        get_order()
        break  

order_breakfast()    