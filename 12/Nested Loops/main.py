# Loop found within another loop (outer-inner)

rows = int(input("Enter the # of rows:"))
columns = int(input("Enter the # of columns:"))
symbol = input("Enter a symbol to use:")


for x in range(rows): # outer-loop
    for c in range(columns): # inner-loop
        print(symbol, end="") # printing the range of 1-9
    print() # prints a new line after the inner-loop ends.


