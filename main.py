file_input = open("Input.txt")

w, h = 9, 9 
Matrix = [[0 for x in range(w)] for y in range(h)] 
aValues=[1,2,3,4,5,6,7,8,9]
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

i=0


while i < len(Matrix):
    j=0
    while j < len(Matrix[i]):
        for row in range(9):
            if Matrix[0][row] != 0:# Fills in the current value of the matrix
                aFoundRow.append(Matrix[0][row])
        for column in range(9):
            if Matrix[column][0] != 0:# Fills in the current value of the matrix
                aFoundColumn.append(Matrix[column][0])

        aFound = []
            
        for x in range(0, len(aFoundRow)):
            if aFoundRow[x] !=0 and aFoundColumn[x] !=0 :
                aFound.append(aFoundColumn[x])
                aFound.append(aFoundRow[x])
                

        aFound = list(set(map(int, aFound)))

        aPossible=[]
        aPossible = list(set(aValues) - set(aFound))#
        aPossible.sort()
        aPossible= list(map(str, aPossible))

        print(aPossible)

        
        if Matrix[i][j] != 0:
            Matrix[i][j] = aPossible[i] + " "# Fills in the current value of the matrix
            aPossible.pop(0)
            
        j = j + 1
    i = i + 1
    
print("breaks")

for x in range(9): # Prints table
    for y in range(9):
        print(Matrix[x][y], end = "")
