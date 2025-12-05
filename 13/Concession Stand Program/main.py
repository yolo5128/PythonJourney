# concession stand program

# utilizing dictionsaries to store item prices

menu = {"hot dog": 2.50,
        "hamburger": 3.00,
        "fries": 1.50,
        "soda": 1.00,
        "candy": 0.75}

cart = []
total = 0


print("Welcome to the Concession Stand!")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

while True:
    food = input("Enter an item to add to your cart (or 'done' to finish): ").lower()
    if food == "done":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------------------------")
print("Items in your cart:")
print("------------------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")
