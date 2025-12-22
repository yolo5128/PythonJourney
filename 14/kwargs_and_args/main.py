#-------------------------------------------------------------!
# *args =  allows u to pass multiple nonkey arguments
# **kwargs = allows you to pass multiple keyword arguments
#           * unpacking operator
#           1. positional 2. default 3. keyword 4. ARBITRARY
#-------------------------------------------------------------!

#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total

#print(add(1, 2, 3))


#def display(*args):
#    for arg in args:
#        print(arg, end=" ")

#display("First", "LASSSS", "Last")

## KWARGS

#def address(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

# address(street="123 FAKE",
#         city="Detroit",
#            state="Michigan",
#             zip="53234")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('State')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "squarepants",
               street="123 fake", apartment="100", 
               city="Detroit",
               State="MI,",
               zip="54321")