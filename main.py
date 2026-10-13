file_input = open("Input.txt")

aRows = []
aColumns = [] 

for rows in range (9):
    for columns in range (9):
        aRows.append(file_input.read())
    


print(aRows)
#print(aColumns)