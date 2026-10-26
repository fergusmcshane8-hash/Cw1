from tabnanny import check
import time 

start = time.perf_counter()

file_input = open("Input.txt") #Opens the file 

w, h = 9, 9 
Matrix = [[0 for x in range(w)] for y in range(h)] 
aValues=["1","2","3","4","5","6","7","8","9"] #Creates an array of possible values to input into the table
vRow=0
vColumn=0
#MATRIX[row][column] # Note of Values of a Matrix
while vColumn != 9:
    while vRow != 9: # loops until the Matrix is 9x9
        Matrix[vColumn][vRow] = file_input.read(2).strip() # Fills in the current value of the matrix
        vRow = vRow + 1 #iterates through the columns 
    vRow = 0 # resets the column so next row is able to be read
    vColumn = vColumn + 1 #slowly goes through it all
file_input.close() # Closes the file after reading it 

def Print(Matrix): # A Function that is called when the Matrix has been correctly filled 
    
    for row in range(9): # loops for the length of the table
        for col in range(9):
            print(Matrix[row][col], end = " ") # Prints the values in the Matrix 
        print() # creates a new line after 9 values so the table maintains the correct structure 
    end = time.perf_counter()
    vTimetaken = end - start
    print(vTimetaken)
def check(Matrix, row, col, aValues):
    
    aFound = set(Matrix[row])# sets the Array of found values to the row of the Matrix
    aFound.update(Matrix[r][col]    for r in range(9)) # updates the array with the values of the rows with the values in the columns 
    rowStart = 3 * (row // 3)
    colStart = 3 * (col // 3) #Creates the 3 by 3 to check for values in the space by dividing the row + column into 3 separate parts
    for rows in range(rowStart,rowStart + 3): # this loops for the 3 parts of the 9x9 
        for columns in range(colStart, colStart + 3): 
            aFound.add(Matrix[rows][columns]) #Adds the values at the current positions to the found values 
    return set(aValues) - aFound #Returns the values it cannot be minus any duplicates  

def FindEmpty(Matrix): # A function to find empty position in the Matrix and return none if the matrix is full
    for row in range(9):
        for col in range(9):#Loops for the length of the Matrix
            if Matrix[row][col] == "0": # if the current position is empty 
                return row, col #returns the position 
    return None  # if the board is full returns none

def Input(Matrix): #Creates the Function to input values
    
    vPosition =FindEmpty(Matrix) #Gets the position of the empty spots in the sudoku puzzles
    if vPosition is None: # if the position is empty
        return True #returns true which will end the check as the table is now full
    else:
        row,col  = vPosition #if the position isn't none then the current position that isn't empty is set to the current position 
    
    for vAmount in check(Matrix, row, col,aValues): # will loop for the amount of possible values
        Matrix[row][col] = vAmount # sets the position thats 0 to the first value of the possible 
        if Input(Matrix):# This calls it's self back to double back in case any values are currently in the wrong place 

            return True # if the function calls itself back and returns true then the 
        Matrix[row][col] = "0"
    return False   




if Input(Matrix):
    Print(Matrix)
else:
    print("No solution exists.")
