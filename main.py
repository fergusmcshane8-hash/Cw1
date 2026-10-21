from tabnanny import check


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
    
def Print(Matrix):
    for x in range(9): # Prints table
        for y in range(9):
            print(Matrix[x][y], end = "")
            

def search(Matrix, aValues):
    aFound = []

    
    for row in range(len(Matrix)):
        for column in range(len(Matrix)):
            if Matrix[column][row] != str(0) + " " :# Fills in the current value of the matrix
                aFound.append(Matrix[column][row])
            
    aFound = list(set(map(int, aFound)))
    print(aFound)
    aPossible=[]
    aPossible = list(set(aValues) - set(aFound))
    aPossible.sort()
    aPossible= list(map(str, aPossible))
    return aPossible

aPossible = search(Matrix, aValues)
print(aPossible)
def Check(Matrix):
    tester = True
    if tester == True:
        for row in range(len(Matrix)):
            if Matrix[0][row] == str(0) + " ":
                row = row + 1
                search(Matrix, aValues)
                for column in range(len(Matrix)):
                    if Matrix[column][0] == str(0) + " ":
                        column = column + 1
                        search(Matrix, aValues)
            else:
                Print(Matrix)
                tester = False



def Input(Matrix, aPossible):
    
    """        
    if Matrix[0][0] == str(0) + " ":
        Matrix[0][0] = aPossible[0] + " "# Fills in the current value of the matrix
        aPossible.pop(0)
    """
    for row in range(len(Matrix)):
        for column in range(len(Matrix)):
            if Matrix[column][row] == str(0) + " " :# Fills in the current value of the matrix
                Matrix[column][row] = aPossible[0] + " "# Fills in the current value of the matrix
                aPossible.pop(0)
    Check(Matrix)
    return(Matrix)

Input(Matrix, aPossible)


#Print(Matrix)
