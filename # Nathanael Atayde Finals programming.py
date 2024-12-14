# Nathanael Atayde Finals

import random
import time

# Naming and stuff
classes = ["Mage", "Thief", "Knight", "Martial Artist"]
statNames = ["Attack", "Speed", "Defense", "SPower", "Health"]
cStats = [
    [50, 15, 20, 70, 100],  # Mage
    [40, 20, 30, 50, 80],   # Thief
    [60, 10, 50, 30, 120],  # Knight
    [70, 10, 40, 20, 100]   # Martial Artist
]

pTravel = {
    "Dungeon": 225,
    "Forest": 150,
    "Town": 75,
    "Tavern": 0
}

item_names = ["Potion", "Stat Boost", "Cheap Vase", "Expensive Vase"]


monsters = [
    {"name": "Lava Slime", "attack": 10, "speed": 8, "defense": 5, "spower": 10, "health": 120},
    {"name": "Ice Bandit", "attack": 8, "speed": 10, "defense": 7, "spower": 5, "health": 100},
    {"name": "Sand Golem", "attack": 20, "speed": 3, "defense": 10, "spower": 5, "health": 175},
    {"name": "Illusion", "attack": 3, "speed": 3, "defense": 1, "spower": 1, "health": 50},
    {"name": "Wyvern", "attack": 30, "speed": 15, "defense": 15, "spower": 20, "health": 300},
    {"name": "Carlos Bulo", "attack": 10, "speed": 20, "defense": 5, "spower": 0, "health": 100}
]

shopItemsSell = {
    "Potion": 100,
    "Stat Boost": 500,
    "Cheap Vase": 200,
    "Expensive Vase": 500
}

shopItems = {
    "Potion": 100,
    "Stat Boost": 500,
}


# Player stuff
player = {
    "name": "",
    "class": "",
    "stats": [],
    "money": 500,
    "status": "Fine",
    "level": 1,
    "exp": 0,
    "inventory": {},
    "location": "Tavern",
    "distance_from_home": 0
}

# Loops and ifs

def player_name():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            player["name"] = name
            print(f"Welcome, {player["name"]}!")
            break
        else:
            print("You can't be nameless!")

def wait_line(rows):
    sLine = "-" * 20
    for i in range(rows):
        print(sLine)
        time.sleep(0.5)

def menu(line, options):
    print(line)
    
    for i, option in enumerate(options, start = 1):
        print(f"{i}.) {option}")
    
    while True:
        wait_line(1)
        choice = input("Choose an option: ").strip().lower()
        wait_line(1)
        
        if choice == "exit":
            return choice
        
        try:
            choice = int(choice) -1 
            if choice in range(len(options)):
                return choice
            print("Choose from the numbers instead of the letters.")
        except ValueError:
            print("Enter a number instead of letters")

def show_stats():
    print(f"{player['name']}'s Stats:")
    
    for i in range(len(statNames)):
        print(f"{statNames[i]}: {player['stats'][i]:.2f}")
    
    print(f"Level: {player['level']}, EXP: {player['exp']}")
    wait_line(1)

# Future: the further the locaiton is the longer it takes to load
def travel():
    while True:
        print("Travel Options:")
        destinations = list(pTravel.keys())
        
        for index in range(len(destinations)):
            print(f"{index +1}.) {destinations[index]}")
        
        print("0.) Back to menu")
        
        choice = input("Where Would You like to Go Adventurer?: ").strip()
        
        if choice.isdigit():
            choice = int(choice)
            
            if choice ==0:
                print("Returning to the main menu.")
                break
            
            elif choice in range(1,len(destinations)+1):
                destination = destinations[choice -1]
                print(f">>>> Heading to {destination} ({pTravel[destination]} miles away)...")
                player["location"] = destination
                
                event_chance = random.randint(0 ,100)
                
                if event_chance <60: #70% chance of encountering a monster 
                    encounter_monster()

                elif event_chance <40: #30% chance of finding a random item 
                    found_item = random.choice(item_names)
                    add_to_inventory(found_item) 
                    print(f"You found a {found_item} while traveling!")
                    
                else:
                    print("Nothing Happened on your Journey.")
                break
            
            else:
                print("Invalid choice. Please select a valid destination or '0' to return.")
        else:
            print("Invalid input. Please enter a number.")

def add_to_inventory(item_name):
    if item_name in player['inventory']:
        player['inventory'][item_name] += 1
    else:
        player['inventory'][item_name] = 1
    print(f"You found a {item_name}! You now have {player['inventory'][item_name]} of them.")

def show_inventory():
    if not player['inventory']:
        print("Your inventory is empty!")
        return
    print("Your Inventory:")
    for item, quantity in player['inventory'].items():
        print(f"{item}: {quantity}")

def shop():
    print("Welcome to the Shop Adventurer!\nAnything that fancies your Eye?")
    wait_line(1)
    while True:
        wait_line(1)
        print(f"You have {player['money']} gold.")
        wait_line(1)
        
        print("Shop Options:")
        print("1.) Buy items")
        print("2.) Sell items")
        print("3.) Exit shop")
        
        choice = input("Enter your choice: ").strip()
# Exit the shop 
        if choice == '3':
            print("Thank you for visiting the shop!") 
            break 

 # Buying items 
        elif choice == '1':
            wait_line(1)
            print("Items available for purchase:")
            wait_line(1)
            items = list(shopItems.keys())
            
            for index,item in enumerate(items, start = 1):
                print(f"{index}.) {item}: {shopItems[item]} gold")
                
            buy_choice=input("Enter the number of the item to buy or 'back' to return: ").strip()
            
            if buy_choice.lower() == 'back':
                continue
            
            try:
                buy_choice=int(buy_choice) 
            except ValueError:
                print("Invalid input. Please enter a number or 'back'.") 
                continue
            
            if buy_choice >= 1 and buy_choice <= len(items): 
                item_name=items[buy_choice-1]
                item_cost=shopItems[item_name]
                
                if player["money"] >= item_cost:
                    add_to_inventory(item_name) 
                    player["money"] -= item_cost 
                    print(f"You bought {item_name} for {item_cost} gold.") 
                else:
                    print("You don't have enough gold to buy that item.") 
            else: 
                print("Invalid item number. Please try again.")
        
# Selling items
        elif choice == '2':
            if not player["inventory"]:
                wait_line(1)
                print("You have no items to sell.")
                continue
            
            wait_line(1)
            print("Items in your inventory:")
            wait_line(1)
            items = list(player["inventory"].keys())
            
            for i, item in enumerate(items, start=1):
                print(f"{i}: {item} (x{player['inventory'][item]})")
            
            sell_choice = input("Enter the number of the item to sell or 'back' to return: ").strip()
            
            if sell_choice.lower() == "back":
                continue
            
            try:
                sell_choice = int(sell_choice)
                
                if 1 <= sell_choice <= len(items):
                    selected_item = items[sell_choice - 1] 
                    item_value = shopItemsSell.get(selected_item, 0) * 0.75
                    
                    quantity_to_sell = int(input(f"How many {selected_item}(s) would you like to sell? "))
                    
                    if quantity_to_sell <= 0 or quantity_to_sell > player['inventory'][selected_item]:
                        print("Invalid quantity.")
                        continue
                    
                    player['inventory'][selected_item] -= quantity_to_sell
                    
                    if player['inventory'][selected_item] == 0:
                        del player['inventory'][selected_item]
                    
                    player["money"] += item_value * quantity_to_sell
                    print(f"You sold {quantity_to_sell} {selected_item}(s) for {item_value * quantity_to_sell} gold.")
                
                else:
                    print("Invalid number. Input a positive number.")
            
            except ValueError:
                print("Invalid input. Please enter a number.")


# Future: make it so that monsters have different chance of encounters and certain drops that you can sell also diff exp
def encounter_monster():
    monster = random.choice(monsters)
    
    print(f"A wild {monster['name']} appeared during your expedition!")
    
    battle(monster)

def battle(monster):
    print(f"Battle with {monster['name']}!")
    
    monster_health = monster['health']
    
    # Basically means that as long as player's hp is not 0 or monster hp isn't 0 the game continues
    while player['stats'][4] >0 and monster_health >0:
        print(f"Your Health: {player['stats'][4]:.2f}, Monster Health: {monster_health:.2f}")
        
        action = menu("Choose an action:", ["Attack", "Use Item", "Run"])
        
        # Attack
        if action ==0:
            damage = max(0.1, player['stats'][0] - monster['defense'])
            monster_health -= damage
            
            if monster_health <=0:
                print(f"You defeated the {monster['name']}!")
                
                # Upgrade so that monster doesn't give same amount of exp
                player['exp'] +=10
                level_up()
                return
            
            # Monster Attacking
            damage_taken = max(0.1 ,monster['attack'] - player['stats'][2])
            player['stats'][4] -= damage_taken
            
            # Death
            if player['stats'][4] <=0:
                print(f"{player['name']} has been defeated. Game Over.")

        # Using Item
        elif action ==1:
            use_item()
        
        # Escape
        elif action ==2:
            if random.randint(0, 100) < 50:
                print("You escaped successfully!")
                return
            
            print("You failed to escape!")

def use_item():
    if not player['inventory']:
        print("Your inventory is empty!")
        return
    
    print("\nYour Inventory:")
    
    items = list(player['inventory'].keys())
    
    for i,item in enumerate(items):
        print(f"{i}: {item} (x{player['inventory'][item]})")
    
    choice=input("Choose an item to use (or 'exit' to cancel): ")
    
    if choice.lower() == 'exit':
        return
    
    try:
        choice=int(choice)
        
        if choice in range(len(items)):
            selected_item=items[choice]
            
            player['inventory'][selected_item] -=1
            
            if player['inventory'][selected_item] ==0:
                del player['inventory'][selected_item]
            # Heal
            if selected_item == "Potion":
                player['stats'][4] = min(100 ,player['stats'][4] +20)
                print("You used a Potion and healed 20 health!")
                
        else:
            print("Please enter a number from the choices and make it positive")
            
    except ValueError:
        print("Please enter a number.")

def level_up():
    # Exp requirement increments
    while player['exp'] >= player['level'] * 10:
        # Reset the exp requirements back to 0 and increase it by 10
        player['exp'] -= player['level'] * 10
        player['level'] +=1
        
        print(f"You leveled up to Level {player['level']}!")
        
        stat_increase=menu("Choose a stat to increase:", statNames)
        
        player['stats'][stat_increase] += 5

def game():
    global player
    
    while True:
        wait_line(1)
        action=menu("What would you like to do?", ["View Stats", "Travel", "Inventory", "Visit Shop"])
        
        if action==0:
            show_stats()
            
        elif action==1:
            travel()
            
        elif action==2:
            show_inventory()
            
        elif action==3:
            shop()

# Main game loop starts here.
wait_line(1)
print("\nWelcome to the Text Adventure Game!\nThis is a game about adventuring forever\nIf you want to Choose answers you must enter the assigned numbers\n")

player_name()
wait_line(1)

choice = menu("Choose your class:", classes)

wait_line(1)

player["class"]=classes[choice]
player["stats"]=cStats[choice][:]

print(f"\nWelcome,{player['name']} the {player['class']}!\n")
wait_line(2)

game()