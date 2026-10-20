file_input = open("Input.txt")

w, h = 9, 9
Matrix = [[0 for x in range(w)] for y in range(h)] 

vRow=0
vColumn=0
while vColumn != 9:
    while vRow != 9:
        Matrix[vColumn][vRow] = file_input.read(2) # Fills in the current value of the matrix
        vRow = vRow + 1 #iterates through the columns 
    vRow = 0 # resets the column so next row is able to be read
    vColumn = vColumn + 1 #slowly goes through it all


aFoundRow=[]
aFoundColumn =[]
for row in range(9):
    if Matrix[0][row] != 0:# Fills in the current value of the matrix
        aFoundRow.append(Matrix[0][row])
for column in range(9):
    if Matrix[column][0] != 0:# Fills in the current value of the matrix
        aFoundColumn.append(Matrix[column][0])

aPossible = []
    
for x in range(0, len(aFoundRow)):
    if aFoundRow[x] !=0 and aFoundColumn[x] !=0 :
        aPossible.append(aFoundColumn[x])
        aPossible.append(aFoundRow[x])
        

aPossible = list(set(aPossible))   
aPossible.sort()
print(aPossible)

for x in range(9):
    for row in range(9):
        for column in range(9):
            if Matrix[column][row] == 0:# Fills in the current value of the matrix
                Matrix[column][row] = aPossible[x]

for x in range(9): # Prints table
    for y in range(9):
        print(Matrix[x][y], end = "")
