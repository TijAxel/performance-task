from Prices import stores#imports the list of items and the amounts

shop_list= []#empty list which would change based on how many items the user wants.

def shopping():#A function named shopping with no parameter
    begin = input("Do you wish to begin making your grocery list?(Yes/No): ").lower()#begins the code

    if begin == "no":
        print("Have a nice day!")
        return #finishes code

    while begin !="no":

        question= input("Great! What store would you like to buy from? Cermark, Walmart, or Sams Club?: ").lower()

        if question in stores:
            item_counter= int(input(f"How many items would you like to buy?: "))
            
            
            if item_counter.isdigit() and (item_counter) > 0:#if the amount they chose is a digit and is over than 0 then it would execute the following coe
                
                category= input(f"What would you like to buy from {question.capitalize()}? (Meat, Dairy, or Fruits): ").lower()
                category_map= {"meat": "meats", "dairy": "dairy", "fruits": "fruits", "toys": "toys", "electronics": "electronics", } #The category map helps the code correct what user says so if user says meat it would go to the list of meats

                category = category_map.get(category, category)

                store_choice= stores[question][0]

                if category in store_choice:
                    available_items = ", ".join([item[0] for item in store_choice[category]])#This part of the code shows the availble items in the store they chose which would be either in the category meat, dairy, or fruits
                    print(f"Available items in {category.capitalize()}: {available_items}")

                    for _ in range(item_counter):#the underscore represents the item and the amount of times they want of that item
                        food_choice = input(f"What would you like to buy? {available_items}: ")

                        for item, price in store_choice[category]:
                            if food_choice.lower() == item.lower():  # Case-insensitive match
                                shop_list.append((item, price))
                                print(f"Added {item} - ${price:.2f} to your shopping list.")
                                break
                        else:
                            print("Invalid selection. Please choose from the available items.")

                else:
                    print("Invalid category selection. Please choose from Meat, Dairy, or Fruits.")

            else:
                print("Invalid number of items. Please enter a positive integer.")

        else:
            print("Store not found. Please choose from Cermark, Walmart, or Sams Club.")

        begin = input("Would you like to continue shopping? (Yes/No): ").lower()

    # **Final Receipt**
    print("\n=== Final Receipt ===")
    total_cost = 0#starting the total cost at zero then adding it up
    for item, price in shop_list:# for every item and price that is in the shopping list run the following code
        print(f"{item}: ${price:.2f}")
        total_cost += price# adds the prices together and replaces the variable in total cost
    print(f"Total Cost: ${total_cost:.2f}")
    print("Thank you for shopping!")

    ####THE RATE THE GAME SYSTEM#######
    def rate_list(simulator):
        rate = input(f"Please rate the '{simulator}' on a scale of 1-10: ")

    if rate.isdigit() and 1 <= int(rate) <= 10:  # Validate the rating input
        rate = int(rate)
        final_score = rate * 10  # Convert the rating to a percentage
        print(f"{final_score}% satisfaction rate")
    else:
        print("Invalid input. Please enter a number between 1 and 10.")
        return  # Exit the function early if input is invalid
    # Ask if the user would recommend it to a friend  
    friend = input("Would you recommend this game to a friend? (yes/no): ").lower()
    # Handle the user's recommendation response
    if friend == "yes":
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")

# rate_list("Shopping list builder")  # Passing the game name and genre as arguments 






shopping()#We call the function here

                

