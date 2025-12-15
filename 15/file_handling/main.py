# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


#                   Different ways to use the default Read Method
#---------------------------------------------------------------------------------------
#f = open('C:/Users/Meer2/Documents/GitHub/PythonJourney/15/file_handling/ran.txt')
#print(f)
#txt = f.read().splitlines()    turns the txt into a list
#txt = f.readlines()            also turns txt into a list
#print(type(txt))               prints the type of txt
#print(txt)
#f.close()

#                  Using the with method auto closes the file automatically
#with open('C:/Users/Meer2/Documents/GitHub/PythonJourney/15/file_handling/ran.txt') as f:
#    lines = f.read().splitlines()
#    print(type(lines))
#    print(lines)
#------------------------------------------------------------------------------------------


#                  Writing and Updating
# with open('C:/Users/Meer2/Documents/GitHub/PythonJourney/15/file_handling/ran.txt', 'a') as f:
#    f.write('This text has to be appended at the end')


#                  Deleting Files using os import
ran_path = "C:/Users/Meer2/Documents/GitHub/PythonJourney/15/file_handling/ran.txt"

import os
if os.path.exists(ran_path):
    os.remove(ran_path)
else:
    print('The file does no longer exists')