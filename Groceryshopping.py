from Prices import stores

def shopping():
    begin = input("Do you wish to begin making your grocery list?(Yes/No): ").lower()

    if begin == "no":
        print("Have a nice day!")
        return #finishes code

    while begin !="no":

        question= input("Great! What store would you like to buy from? Cermark, Walmart, or Sams Club?: ").lower()

        if question in stores:
            item_counter= int(input(f"How many items would you like to buy?: "))
            
            
            if item_counter.isdigit() > 0:
                
                category= input(f"What would you like to buy from {question.capitalize()}? {stuff}").lower()
                category_map= {"meat": "meats", "dairy": "dairy", "fruits": "fruits"}
                category = category_map.get(category, category)
                store_choice= stores[question][0]
                

                for item, price in store_choice[category]:
                    print(f"-{item}: ${price:.2f}")
                    available_items = ", ".join([i[0] for i in store_choice[category]])
                    stuff= ", ".join([i[0] for i in store_choice[category]])
                    food_choice= input(f"What would you like to buy? {stuff}: ")

                    if food_choice in ([i[0] for i in store_choice[category]]):
                        shop_list= []
                        shop_list.append(food_choice)

                        print (shop_list)
                        
        else:
            print("invalid category selection")
    else:
        print("Store not found. Please choose from the following, Cermark, Walmart, or Sams club.")
    begin= input("Would you like to continue shopping?(Yes/No): ").lower()


shopping()


# if begin == "no":# if youre done with the sim this will run

#     def rate_list(simulator):  
# # Ask for rating input
#     rate = input(f"Please rate the '{simulator}' on a scale of 1-10: ")

#     if rate.isdigit() and 1 <= int(rate) <= 10:  # Validate the rating input
#         rate = int(rate)
#         final_score = rate * 10  # Convert the rating to a percentage
#         print(f"{final_score}% satisfaction rate")
#     else:
#         print("Invalid input. Please enter a number between 1 and 10.")
#         return  # Exit the function early if input is invalid

# # Ask if the user would recommend it to a friend  
# friend = input("Would you recommend this game to a friend? (yes/no): ").lower()

# # Handle the user's recommendation response
# if friend == "yes":
#     print("Thanks, we appreciate it!")
# else:
#     print("Sorry you did not enjoy it.")
# rate_list("Shopping list builder")  # Passing the game name and genre as arguments 
