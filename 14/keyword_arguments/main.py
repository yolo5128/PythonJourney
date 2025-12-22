
# Keyword arguments = an argument preceded by an indentifier
#                     helps with readability, order of arguments dont matter



def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello,", title="Mr.", first="Yolo", last="MrPandora")

for x in range(1, 11):
    print(x, end=" ")

print()
print("1", "2", "3", "4", "5", sep="-")

def getPhone(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}-{last}"

phone_num = getPhone(country_code=1, area_code=440, first=456, last=6798,)

print(phone_num)

