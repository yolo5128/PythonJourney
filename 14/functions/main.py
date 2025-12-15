
def happy_bday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You're {age} years old!")

happy_bday("Bob", 19)


def display_invoice(username, amount, due_date):
    print(f"Hello  {username}, Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Yolo", 12.50, "12/16/2025")


def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z= x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + "" + last_name

full_name = create_name("Yolo", "MrPandora")

print(full_name)



