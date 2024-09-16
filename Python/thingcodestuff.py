import math
import sys

def new_board(): 
    return {}

# Initialize an empty board
board = new_board()

# Function to place a piece on the board at the specified (x_cord, y_cord) for a given player.
# If the spot is free, the piece is added to the player's list of coordinates in the board.
def place_piece(board, x_cord, y_cord, player): 
    # Check if the position is free
    free_place = is_free(board, x_cord, y_cord)
    
    # If the place is free, add the piece
    if free_place is True:
        # Get the list of coordinates for the player
        cords = board.get(player, [])
        cords.append((x_cord, y_cord))  # Add the new coordinates
        board[player] = cords  # Update the board with the new coordinates
        return True
    else:
        # If not free, do nothing and return False 
        return False

# Function to move a piece from one position to another
def move_piece(board, x_cord, y_cord, new_x_cord, new_y_cord):  
    # Check if there's a piece at the original position
    player = get_piece(board, x_cord, y_cord)
    # Get player list of cords, find the index of old cords, replaced old cords, update board with new cords
    if player:              
        cords=board[player]
        index =cords.index((x_cord,y_cord))
        cords[index] = (new_x_cord, new_y_cord)
        board[player] = cords
        return True
    else:
        return False
   

# Function to check if a given position (x_cord, y_cord) is free
def is_free(board, x_cord, y_cord): 
    # Iterate over all players in the board
    for player in board:
        # Check if any player has a piece at the given coordinates
        if (x_cord, y_cord) in board[player]:
            return False  # Position is occupied
    # If no piece was found at that position, return True
    return True

# Function to retrieve the player who owns the piece at the specified position
def get_piece(board, x_cord, y_cord):  
    for player, cords in board.items():
        if (x_cord, y_cord) in cords:
            return player  # Return the player who has the piece
        else:
            return None

# Function to remove a piece from the board at the specified position
def remove_piece(board, x_cord, y_cord):  
    # Check if the position is occupied
    player = get_piece(board, x_cord, y_cord)
    # Get player list of cords, find the index of old cords, replaced old cords, update board with new cords
    if player:              
        cords=board[player]
        if (x_cord, y_cord) in cords:
            cords.remove((x_cord,y_cord))
            board[player] = cords
            return True
        else:
            return False
    else:
        return False

# Function to find the nearest piece to a given position
def nearest_piece(board, x_cord, y_cord):
    player = get_piece(board, x_cord, y_cord)
    if player:
        cords=board[player]
        #Behöver något för att jämnföra till närmsta pjäs
        # Vet inte riktigt vad jag ska göra för det      
        # Pythagoras  

# Function to count how many pieces a player has in a given row/column
def count(board, thing, nr, player):
    # Get the list of moves for the player, assumed to be a list of (row, column) tuples
    player_moves = board.get(player, [])
    
    # Debug: Print player moves to ensure they are correct
    print(f"Player {player} moves: {player_moves}")
    
    res = 0

    # Check if we are counting occurrences in a specific column
    if thing == "column":
        for move in player_moves:
            row, col = move
            if col == nr:
                res += 1

    # Check if we are counting occurrences in a specific row
    elif thing == "row":
        for move in player_moves:
            row, col = move
            if row == nr:
                res += 1

    # Invalid value for 'thing'
    else:
        print("You can't spell. Please specify either 'row' or 'column'.")
    
    return res


sys.setrecursionlimit(1000000)
def choose(n,k):
    värde_n=factorial(n)
    värde_k=factorial(k)
    värde_nk=factorial(n-k)
    return värde_n/(värde_k*värde_nk)

#REKURSION
def factorial(n):  #funkar
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
    
def factorial2(n): #Funkar ej men är rekursivt
    resultat = 1
    for i in range(n):
        resultat *= n-i
    return resultat
    
def factorial3(n):   #Funkar
    return math.factorial(n) 



print("{:.0f}".format(choose(1000,800))) #För att formatera det från t.ex 6.6171555606593036e+215
print(choose(1000,800))
#Rekursivt skriv ut exempel och hitta sätt att förenkla det på 
#Symetri i biminolsatsen
#Chooose i coose och itne använda factorial för är ligger problemet



place_piece(board, 1, 1, "Fe1ixJ")
print(is_free(board, 1, 1))  
move_piece(board, 1, 1, 2, 2)
print(is_free(board, 1, 1))  
print(get_piece(board, 2, 2))
#remove_piece(board, 2, 2)
print(get_piece(board, 2, 2))
place_piece(board, 1, 1, "Fe1ixJ")
place_piece(board, 1, 2, "Fe1ixJ")
#NEAREST
print(count(board,"row",1,"Fe1ixJ"))

