
# learning Collections - 2D Collections (Tuples inside a Tuple)
numpad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))

for row in numpad:
    for num in row:
        print(num, end=" ")
    print() 



# trying something out, not sure what it does.
"""
 for i in range(len(numpad)):
    print(numpad[i], end=" ")
    print()

"""




