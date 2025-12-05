# Dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(capitals.get("USA")) -- gets value for key USA

# if capitals.get("China"):
#    print("That capital exists")
# else:
#    print("No such capital exists")

# capitals.update({"Germany": "Berlin"}) -- adds new key value pair
# capitals.update({"USA": "Detroit"}) -- updates existing key 
# capitals.pop("China") -- removes item with key China
# capitals.popitem() -- removes last item
# capitals.clear()  # -- removes all items
# keys = capitals.keys() -- gets all keys
# values = capitals.values()  # -- gets all values
# print(values)

# for value in capitals.values():  # -- iterating through values
#    print(value)

# for key in capitals.keys(): -- iterating through keys
#    print(key) -- prints keys only

# items = capitals.items() 
# for key, value in capitals.items():
#    print(f"{key}: {value}")
