###  The SUDOKU Solver Using Backtracking  ###

#This is the sudoku to be solved
sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

#This is the solved sudoku -- it will be used to verify the answer
sudoku_solved = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]]

#Function to print the sudoku board
def printSudoku(sudoku):
     for i in range(len(sudoku)):
          if i % 3 == 0:
               print('--------------------------')
          for j in range(len(sudoku[0])):
               if j % 3 == 0 and j != 0:
                    print (' | ', end = " ")
               print(sudoku[i][j], end = " ")
          print()

#check if the number to be inserted is allowed
def valid(sudoku, row, col, num):
     #check same row
     for i in range(len(sudoku[0])):
          if sudoku[row][i] == num:
               return False
     #check same column
     for i in range(len(sudoku)):
          if sudoku[i][col] == num:
               return False                   
     #check same box
     boxY = row // 3
     boxX = col // 3
     for i in range(3):
          for j in range(3):
               if sudoku[(boxY * 3) + i][(boxX * 3) + j] == num:
                    return False
     return True

#Function to check if there empty (0) positions on the board
def solved(sudoku):
     for i in sudoku:
          for j in i:
               if j == 0:
                    return False
     return True

#Main function
def solve(sudoku):
     if solved(sudoku):
          return True
     #Loop through every position on the board and look for empty positions
     for i in range(len(sudoku)):
          for j in range(len(sudoku[0])):
               if sudoku[i][j] == 0:
                    for k in range(1, 10):
                         if valid(sudoku, i, j, k):
                              sudoku[i][j] = k
                              #Recursive call for next empty position
                              if solve(sudoku):
                                   return True
                    #If all values of k fail, this means we need to backtrack
                    #to previous position (which will get a new value for k)
                    #and continue with the recursive call till validity
                    sudoku[i][j] = 0 #set the current position's value back to 0
                    return False

#Function to verify if the answer matches the expected result
def checkResult(s, s_solved):
     for i in range(len(s)):
          for j in range(len(s[0])):
               if s[i][j] != s_solved[i][j]:
                    return False
     return True

printSudoku(sudoku)
print()#Leave some space to print the solved board
solve(sudoku)
printSudoku(sudoku)
print(checkResult(sudoku, sudoku_solved)) #print True if answer correct
