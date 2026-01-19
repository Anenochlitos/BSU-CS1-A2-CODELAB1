chips = {
    "pringles":1,
    "lays":2,
    "doritos":3,
}   #Create a dictionary for chips with its item no.
drinks = {
    "cola":1,
    "sprite":2,
    "fanta":3
}   #Create a dictionary for drinks with its item no.

price = {
    chips["pringles"]:1.50,
    chips["lays"]:1.00,
    chips["doritos"]:1.25,
    drinks["cola"]:1.75,
    drinks["sprite"]:1.50,
    drinks["fanta"]:1.60
} #Create a dictionary for prices, from the chips and drinks dictionaries

def run():  #Define a function to display the menu
    print("Menu:")  #Display the menu
    print("\nChips:")   #Display chips section
    for i, n in chips.items():#For each item in chips dictionary -labeling both key-pair as "i" and "n" respectively -print the item, its code, and price
        print(f"{i} - C{n} - ${price[n]}") #I added C before the number to indicate chips and took the price from the price dictionary
    print("\nDrinks:")  #Same goes for the drinks section
    for i, n in drinks.items():
            print(f"{i} - D{n} - ${price[n]}")

    initial_balance = float(input(f"\nAdd your balance and press Enter to continue: $"))
    print(f"Your current balance is: ${initial_balance:.2f}")  #Displays the current balance

    print("\nTo select an item, enter the item code (e.g., C1 for pringles, D3 for fanta).") #Adds a user guideline for selecting an item
    selected = input("Enter item code: ").strip().lower()  #Stores user input in selection and removes any space and converts to lowercase
    if len(selected) < 2:  #Checks if input is less than 2 to immediately print "invalid selection"
        print("Invalid selection.") #prints "invalid selection"
    else:   #If not less than 2, continues with the code
        category = selected[0] #Stores the first character of the input to determine the category (chips or drinks)
        try:    #Try to pass the following selection as integer; if it fails, it goes to except and prints "invalid selection"
            item_number = int(selected[1:]) #Stores the second character of the input as item number
            if category == 'c' and item_number in chips.values():   #if category is chips and item number is in chips values, 
                item_name = [name for name, num in chips.items() if num == item_number][0] 
                #Create a list in chips labeled name and goes through each pair in chips and keeps only the pair that matches the item number, then takes the first item in that list
                item_price = price[item_number] #Gets the price from the price dictionary using the item number
                print(f"You selected {item_name} which costs ${item_price}.") #Prints the selected item and its price
            elif category == 'd' and item_number in drinks.values():
                item_name = [name for name, num in drinks.items() if num == item_number][0]
                item_price = price[item_number]
                print(f"You selected {item_name} which costs ${item_price}.")
            else:
                print("Invalid selection.") #If neither condition is met, prints "invalid selection"
        except ValueError:  #If the conversion to integer fails, it goes here and prints "invalid selection"
            print("Invalid selection.")
    purchase = input(f"\nDo you want to purchase this item ({item_name})? (yes/no): ").strip().lower()
    if purchase == "yes" and initial_balance >= item_price:  #Checks if the current balance is greater than or equal to the item price
        initial_balance -= item_price  #Deducts the item price from the current balance
        print(f"Purchase successful! Your new balance is: ${initial_balance:.2f}")  #Prints purchase successful message with new balance
    elif purchase == "no":  #If user inputs no for purchase
        print("Purchase cancelled.")  #Prints purchase cancelled message
    else:
        print("\nInsufficient balance. Please add more funds to complete the purchase.")  #Prints insufficient balance message
        while True:
            print(f"Your current balance is: ${initial_balance:.2f} and the item price is: ${item_price:.2f}")  #Prints current balance and item price
            print(f"You need an additional ${item_price - initial_balance:.2f} to complete the purchase.")  #Prints the additional amount needed
            additional_balance = float(input("\nEnter additional amount to add: "))  #Asks user to input additional balance
            initial_balance += additional_balance  #Adds the additional balance to the current balance
            purchase =input(f"Do you want to proceed with the purchase of {item_name}? (yes/no): ").strip().lower()
            if purchase == "yes" and initial_balance >= item_price:  #Checks again if the current balance is sufficient
                initial_balance -= item_price  #Deducts the item price from the current balance
                print(f"Purchase successful! Your new balance is: ${initial_balance:.2f}")  #Prints purchase successful message with new balance
                break  #Exits the loop
            elif purchase == "no":  #If user inputs no for purchase then exit
                print("Purchase cancelled.")  #Prints purchase cancelled message
                break  #Exits the loop
            else:
                print("Still insufficient balance. Transaction cancelled.")  #Prints transaction cancelled message

if __name__ == "__main__":  #If this file is run directly, it will execute the run function
    run()
