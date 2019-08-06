"""
 *****************************************************************************
   FILE:        wordfind.py

   AUTHOR: Amin Babar

   ASSIGNMENT: Project 5 - Wordfind

   DATE: 05/10/17

   DESCRIPTION: Wordfind takes 2 paprameters. A grid of lowercase letters and
   lowercase words. It then finds the words in the grid, if possible, and
   prints out the entire grid with the found words in upper case letters. It
   also returns the total count of words found in the grid.

 *****************************************************************************
"""


def printGrid(grid):
    """ Display the grid in a nice way """
    for row in grid:
        print(row)


# Takes every letter in the direction travelled and capitalizes it. The function
# takes the row and col, moves it in direction dr or dc for the length of the
# word. 
# DETAILS: Discussed multiplying by i to save the spot the function is at 
def capitalize(grid, word, r, c, dr, dc):
  for i in range(len(word)):
    grid[r + dr * i][c + dc * i] = word[i].upper()
  return grid
  

# Looks for letters in every one of the possible 8 directions. The first
# portion accounts for if the word happens to be only one letter and 
# capitalizes it. 
# DETAILS: Discussed creating for loops and if statements to look for rest of
# the word after ascertaining the correct direction. 
def search(grid, word, r, c):
  num = 0
  directions = [(0,1), (0, -1), (1,0), (1,1), (1,-1), (-1, 0), (-1, 1), (-1,-1)]
  for direct in directions:
    found = word[0]
    if found == word:
            num += 1
            grid = capitalize(grid, word, r, c, direct[0], direct[1])
            return num
    # Takes the letters after the first one and adds the rows part of the 
    # direction tuple to the row part of the coordinate of the letter and so
    # forth. It also sets conditions for the parameters that the search cannot
    # violate (not going beyond the scope of the grid). If a word is found,
    # it is counted and every letter is capitalized. 
    # DETAILS: Donald helped me figure out the problem with the submission error
    # that wasn't counting the number of words. Sofia discussed what Prof.
    # Campbell had told her about the conditions of the parameters of the grid.      
    for letter in range(1, len(word)):
      newr = r + direct[0] * letter
      newc = c + direct[1] * letter
      if 0 <= newr and newr < len(grid) and 0 <= newc and newc < len(grid[0]):
        if word[letter] == grid[newr][newc].lower():
          found = found + grid[newr][newc].lower()
          if found == word:
            num += 1
            grid = capitalize(grid, word, r, c, direct[0], direct[1])
  return num


# This function calls the previous functions and finds the first letter for 
# every word in the grid. 
def wordfind(grid, words):
   num = 0
   cols = len(grid[0])
   rows = len(grid)
   for r in range (rows):
     for c in range (cols):
       for word in words:
         if grid[r][c].lower() == word[0]:
           num += search(grid, word, r, c)
   return num


def main():
    """ The main program is just for your own testing purposes.
        Modify this in any way you wish.  It will not be graded. """
    
    myGrid = [['j', 'm', 'w', 'e'],
              ['e', 'e', 'p', 'p'],
              ['q', 'o', 'x', 'u'],
              ['w', 'w', 'e', 'd'],
              ['w', 'g', 'j', 'o']]
    words = ['meow', 'wed', 'do', 'justice']
    count = wordfind(myGrid, words)
    printGrid(myGrid)
    print(count)

if __name__ == "__main__":
    main()
