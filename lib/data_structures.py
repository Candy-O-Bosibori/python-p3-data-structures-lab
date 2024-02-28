spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]





def get_names(spicy_foods):
    
    spicy_list=[i["name"] for i in spicy_foods]
    return spicy_list







def get_spiciest_foods(spicy_foods):
    # new list
    spiciest_foods = []
    # iterayte through every dict 
    for food in spicy_foods:
        # see if the spice level i greater than 5
        if food["heat_level"] > 5:
        #    append to the new list fomed
           spiciest_foods.append(food)
        #    return the list in the function
    return spiciest_foods   





        

def print_spicy_foods(spicy_foods):
    # iterate
    for food in spicy_foods:
        # moltiply the chillis by the heatlevel
        heat_level_emoji = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")



    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
#  it the cuisine is not avilable
    return None  






def print_spiciest_foods(spicy_foods):
    #   pass the spiciest food to the get_spiciest_foods func
      spiciest_foods = get_spiciest_foods(spicy_foods)
    #   then whatever out pust is given , print it it this way...
      print_spicy_foods(spiciest_foods)






def get_average_heat_level(spicy_foods):
    # get total
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    # get ttl items
    num_foods = len(spicy_foods)
    #  average
    return total_heat_level // num_foods






def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
