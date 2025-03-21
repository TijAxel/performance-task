from Prices import stores#imports the list of items and the amounts

shop_list = []  # Empty list for user-selected items


def shopping():#Function with no parameter
    begin = input("Do you wish to begin making your grocery list? (Yes/No): ").strip().lower()#begins the code if user says yes and puts it ino lowercase so it is easier.

    if begin == "no":#if the user does say no it will end the code
        print("Have a nice day!")
        return

    while begin != "no":#if user said anything other than no, it will begin the code
        question = input("Great! What store would you like to buy from? Cermark, Walmart, or Sams Club?: ").strip().lower()#ask the user what store they would like to go and then stores it in a variable named questions 

        if question in stores:#if the store they chose was one of the options it will execute the following code
            store_choice = stores[question][0]
            
            category = input(f"What category would you like to buy from {question.capitalize()}? (Meat, Dairy, or Fruits): ").strip().lower() #ask the user what category of fruits meat or dairy they want to choose from
            category_map = {"meat": "meats", "dairy": "dairy", "fruits": "fruits"}# a dictionary that can help he computer read the input better so if the user writes meat itll read it as meats
            category = category_map.get(category, category)# another part of the dictionary that converts what the user writes so meat will be turn to meats

            if category in store_choice:
                available_items = {item[0].lower(): item for item in store_choice[category]}  #this shows the available items in the store chouces as this format (item, price)
                print(f"Available items in {category.capitalize()}: {', '.join(available_items.keys())}")

                items_to_buy = input("Enter the items you want to buy: ").strip().lower().split(", ") ## User enters multiple items separated by commas, converts them to lowercase, and stores them in a list.
                quantities = {}#the empty list that the items_to_buy stuff would be stored intox``

                for item in items_to_buy:# loop through the selected items
                    if item in available_items: #this checks the item they chose is within this store
                        while True:
                            try:
                                qty = int(input(f"How many of {item.capitalize()} would you like to buy?: ")) #ask the user for the amount of items they want
                                if qty > 0: #ensures that the quantity is positive
                                    quantities[item] = qty #stores the amount
                                    break #exits the loop
                                else:
                                    print("Please enter a quantity greater than 0.") #in case the user enters a number that is negative
                            except ValueError:
                                print("Invalid input. Please enter a number.") #asks the user to enter a positive number

                for item, qty in quantities.items():  # Loop through selected items and amounts
                    name, price = available_items[item]  # Extract name and price from dictionary which is in prices
                    total_price = price * qty  # Calculate total price for item
                    shop_list.append((name, price, qty, total_price))  # Add to shopping list
                    print(f"Added {qty}x {name} - ${total_price:.2f} to your shopping list.")  # Confirm the amount added to the shopping lit
            
            else:
                print("Invalid category selection. Please choose from Meat, Dairy, or Fruits.")  # Error message for the product input
        
        else:
            print("Store not found. Please choose from Cermark, Walmart, or Sams Club.")  # Error message for the store input
        
        # Ask if user wants to continue shopping
        begin = input("Would you like to continue shopping? (Yes/No): ").strip().lower()
    
    # **Final Receipt**
    print("\n=== Final Receipt ===")
    total_cost = sum(total for _, _, _, total in shop_list)  # Calculate total cost
    for item, price, qty, total in shop_list:  # Loop through shopping list
        print(f"{qty}x {item} - ${price:.2f} each - Total: ${total:.2f}")  # Print item details
    print(f"Total Cost: ${total_cost:.2f}")  # Display total cost
    print("Thank you for shopping!")  # Thanks user once they are done
    
    rate_list("Shopping list builder")  # Call rating function

# **Rate the Game System**
def rate_list(simulator):  # Function to rate the program
    while True:
        rate = input(f"Please rate the '{simulator}' on a scale of 1-10: ").strip()  # Ask for rating
        
        if rate.isdigit() and 1 <= int(rate) <= 10:  # Makes sure that the rating is a number between 1-10
            rate = int(rate)  # Convert rating to integer
            final_score = rate * 10  # Convert rating to percentage
            print(f"{final_score}% satisfaction rate")  #Prints the satifaction rate
            break  # Exit loop
        else:
            print("Invalid input. Please enter a number between 1 and 10.")  # Error message
    
    # Recommendation check
    friend = input("Would you recommend this game to a friend? (yes/no): ").strip().lower()
    if friend == "yes":
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")

# Start the shopping function
shopping()
