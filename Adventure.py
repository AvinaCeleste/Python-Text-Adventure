from random import randint

help_text = """
Commands:
Help - Opens the command list.
Inventory - Opens your inventory.
Fish - Allows you to fish. Your odds of catching a fish increase with better equipment.
Craft - Opens crafting menu.
Scavenge - Searches the island for useful material.
Consume - Consumes the item selected
"""

#Inventory class, holds single name, plural name, and quantity of item
class inventory():
    def __init__(self,single,plural,quantity):
        self.single = single
        self.plural = plural
        self.quantity = quantity
#Food class, inherits inventory class attributes and holds item food, health, and hydration value
class food(inventory):
    def __init__(self,single,plural,quantity,food_val,heal_val,hyd_val):
        inventory.__init__(self,single,plural,quantity)
        self.food_val = food_val
        self.heal_val = heal_val
        self.hyd_val = hyd_val
#Plural var
same = "="
s = "s"        
#Inventory objects
fishing_rod = inventory("fishing rod",s,0)
stone=inventory("stone",s,0)
wood=inventory("wood",same,0)
rope=inventory("rope",s,0)
#Food objects
raw_fish = food("raw fish",same,0,0,0,0)
coconut = food("coconut",s,0,0,0,0)
cooked_fish = food("cooked fish",same,0,0,0,0)
#List w/ inventory objects
items = {raw_fish,coconut,cooked_fish,fishing_rod,stone,wood,rope}


timer = {"fish" : 0, "search" : 0, "boat" : 0, "tree" : 0}
health = {"Hunger" : 0, "Hydration" : 0, "Health" : 0}
trees = {"t1" : 0, "t2" : 0, "t3" : 0, "t4" : 0,"t5" : 0, "t6" : 0,"t7" : 0, "t8" : 0,"t9" : 0, "t10" : 0}
game_torf = False

#Resets inventory and island. Restarts game.
def reset_game():
    print("""▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▀█▀ ▒█▀▀▀█ ▒█░░░ ░█▀▀█ ▒█▄░▒█ ▒█▀▀▄ 
░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█░ ░▀▀▀▄▄ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▒█ 
░▒█░░ ▒█░▒█ ▒█▄▄▄ 　 ▄█▄ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█▄▄▀""")
    print("The objective of the game is to survive and thrive for as long as possible. Type \"Help\" for a list of commands. ")
    for x in items:
        x.quantity = 0
    for y in timer:
        timer[y] = 0
    for x in trees:
        trees[x] = randint(0,4)
    for x in health:
        health[x] = randint(50, 100)
    game_torf = False
    choices()
    
def game_over():
    print("""▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀ ▒█▀▀█ 
▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀ 　 ▒█░░▒█ ░▒█▒█░ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄ 　 ▒█▄▄▄█ ░░▀▄▀░ ▒█▄▄▄ ▒█░▒█ """)
    choice_go = input("Ready to play again? Type yes to continue. ").lower()
    if choice_go == "yes" or choice_go == "y":
        reset_game()
    else:
        print("Thanks for playing!")

def fishing():
    fish_caught = randint(1,3)
    if fish_caught == 1:
        print("Congratulations, you caught a fish!")
        raw_fish.quantity += 1
    else:
        print("The fish don't seem to be biting.")
    events()
    choices()
    
def consume():
    food_list = "You have "
    food_text = "{} {}{}, "
    for i in items:
        if isinstance(i,food):
            if i.quantity > 0:
                if i.quantity == 1:
                    food_list += food_text.format(str(i.quantity),i.single,"")
                else:
                    if i.plural == same:
                        food_list += food_text.format(str(i.quantity),i.single,"")
                    elif i.plural == s:
                        food_list += food_text.format(str(i.quantity),i.single,"s")
                    else:
                        food_list += food_text.format(str(i.quantity),i.plural,"")
    if food_list == "You have ":
            food_list += "nothing."
    else:
            food_list += "and nothing else."
    print(food_list)
    consume_input = input("What would you like to consume? ")
    item_to_consume = 0
    for x in items:
        if isinstance(x,food):
            if consume_input == x.single:
                item_to_consume = x
    if item_to_consume == 0:
        print("You can't eat that!")
    else:
        if item_to_consume.quantity == 0:
            print("You don't have any {}.".format(item_to_consume.single))
        else:
            item_to_consume.quantity -= 1
            print("You have eaten a {}.".format(item_to_consume.single))
    choices()
         
def inventory_fun():
    inventory_list = "You have "
    inv_text = "{} {}{}, "
    for x in items:
        if x.quantity > 0:
            if x.quantity == 1:
                inventory_list += inv_text.format(str(x.quantity),x.single,"")
            else:
                if x.plural == same:
                    inventory_list += inv_text.format(str(x.quantity),x.single,"")
                elif x.plural == s:
                    inventory_list += inv_text.format(str(x.quantity),x.single,"s")
                else:
                    inventory_list += inv_text.format(str(x.quantity),x.plural,"")
    if inventory_list == "You have ":
            inventory_list += "nothing."
    else:
            inventory_list += "and nothing else."
    print(inventory_list)
    choices()
    
def boat():
    if timer["boat"] >= 1:
        boat_int = randint(1,100)
        if boat_int == 1:
            print("In the distance, you see a boat heading towards you. With a frantic scream and a flailing of limbs, you beckon the ship over. You have been rescued.")
            game_torf = True
            game_over()
            
def events():
    for x in timer:
        timer[x] += 1
    if timer["tree"] >= 5:
        for x in trees:
            if trees[x] != 0 and trees[x] != 5:
                trees[x] += 1
        timer["tree"] = 0
    for x in health:
        health[x] -= 5
    

def scavenge():
    stone = randint(1,30)
    bottle = randint(1,100)
    bugs = randint(1,30)
    driftwood = randint(1,30)
          
def health_bars():
    def bars(bar_x):
        bar_val = int(round(health[bar_x]/10, 0))
        bar = ""
        for x in range(0,10):
            if bar_val > 0:
                bar += "⬛"
                bar_val -= 1
            else:
                bar += "⬜"
        final_string = bar_x+" "+ bar +" "+str(health[bar_x])+"%"
        return final_string
    print(bars("Health")+"\n"+bars("Hunger")+"\n"+bars("Hydration"))
    choices()
            
        
def choices():
    boat()
    if game_torf == False:
        choice = input("What would you like to do? ").lower()
        if choice == "fish":
            fishing()
        elif choice == "inventory":
            inventory_fun()
        elif choice == "help":
            print(help_text)
            choices()
        elif choice == "health":
            health_bars()
        elif choice == "quit":
            game_over()
        elif choice == "consume":
            consume()
        else:
            print("Invalid command. Try again.")
            choices()
        
reset_game()