from Prices import stores#imports the list of items and the amounts

shop_list = []  # Empty list for user-selected items




shop_list = []  # Empty list for user-selected items


def shopping():
    begin = input("Do you wish to begin making your grocery list? (Yes/No): ").strip().lower()

    if begin == "no":
        print("Have a nice day!")
        return

    while begin != "no":
        question = input("Great! What store would you like to buy from? Cermark, Walmart, or Sams Club?: ").strip().lower()

        if question in stores:
            store_choice = stores[question][0]
            
            category = input(f"What category would you like to buy from {question.capitalize()}? (Meat, Dairy, or Fruits): ").strip().lower()
            category_map = {"meat": "meats", "dairy": "dairy", "fruits": "fruits"}
            category = category_map.get(category, category)

            if category in store_choice:
                available_items = {item[0].lower(): item for item in store_choice[category]}  # Dictionary for quick lookup
                print(f"Available items in {category.capitalize()}: {', '.join(available_items.keys())}")

                items_to_buy = input("Enter the items you want to buy (comma-separated): ").strip().lower().split(", ")
                quantities = {}

                for item in items_to_buy:
                    if item in available_items:
                        while True:
                            try:
                                qty = int(input(f"How many of {item.capitalize()} would you like to buy?: "))
                                if qty > 0:
                                    quantities[item] = qty
                                    break
                                else:
                                    print("Please enter a quantity greater than 0.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")

                for item, qty in quantities.items():
                    name, price = available_items[item]
                    total_price = price * qty
                    shop_list.append((name, price, qty, total_price))
                    print(f"Added {qty}x {name} - ${total_price:.2f} to your shopping list.")

            else:
                print("Invalid category selection. Please choose from Meat, Dairy, or Fruits.")

        else:
            print("Store not found. Please choose from Cermark, Walmart, or Sams Club.")

        begin = input("Would you like to continue shopping? (Yes/No): ").strip().lower()

    # **Final Receipt**
    print("\n=== Final Receipt ===")
    total_cost = sum(total for _, _, _, total in shop_list)  # Sum prices
    for item, price, qty, total in shop_list:
        print(f"{qty}x {item} - ${price:.2f} each - Total: ${total:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("Thank you for shopping!")

    rate_list("Shopping list builder")  # Call rating function


# **Rate the Game System**
def rate_list(simulator):
    while True:
        rate = input(f"Please rate the '{simulator}' on a scale of 1-10: ").strip()

        if rate.isdigit() and 1 <= int(rate) <= 10:
            rate = int(rate)
            final_score = rate * 10
            print(f"{final_score}% satisfaction rate")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")

    # Recommendation check
    friend = input("Would you recommend this game to a friend? (yes/no): ").strip().lower()
    if friend == "yes":
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")


# Run the program only if executed directly
if __name__ == "__main__":
    shopping()