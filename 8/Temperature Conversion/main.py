
unit = input("Is this temperature in Celcius or Fahrenheight (C/F): ")
temp = float(input("Enter the temperature: )"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} degrees F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp} degrees C")
else:
    print(f"{unit} is an invalid unit of measurement.")
