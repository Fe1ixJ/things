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
        index =cords.index((x_cord,y_cord))
        cords[index] = ()
        board[player] = cords
        return True
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
    # X_VÄRDE ÄR ROW
    # Y_värde är Column fast
    # Tänker alltså att man låser X värdet och kolla alla yvärden uppåt till då 100k
    # Alternativt att man kör något med att kolla board[player] och hitta Dem där t.ex 
    # då Row 1 då x-värdet är 1 och yvärdet kollas
    # Sedan returna på hurmånga värden som matchar med typ en loop som kör i++ elr något. 
    # Adderar varje for case typ idk
    if thing == "column":
        print("C")
        pass
    elif thing == "row":
        pass
        print("R")
    else: print("You cant spell")




place_piece(board, 1, 1, "Fe1ixJ")
print(is_free(board, 1, 1))  
move_piece(board, 1, 1, 2, 2)
print(is_free(board, 1, 1))  
print(get_piece(board, 2, 2))
remove_piece(board, 2, 2)
print(get_piece(board, 2, 2))
#NEAREST
print(count(board,"row",2,"Fe1ixJ"))
#COUNT

