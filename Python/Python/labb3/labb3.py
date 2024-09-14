def new_board(): #Klar
    return {}
board = new_board()

def place_piece(board, x_cord, y_cord, player):   #FUNKAR EJ Lägger inte till något i Listan
    free_place=is_free(board, x_cord,y_cord)
    if free_place is True:
        cords = board.get(player)
        cords.append((x_cord,y_cord))
        board.update{player: cords}
        return True
    else:
        False

def move_piece(board, x_cord, y_cord, new_x_cord, new_y_cord):  #EJ KLAR
    free_place = is_free(x_cord,y_cord)
    if free_place is False:
        cords = board.get()
        cords.append((x_cord,y_cord))
        board.update()


def is_free(board, x_cord, y_cord): #Klar
    for i in board:
        if(x_cord,y_cord) in board[i]:
            return False
        else: 
            return True

def get_piece(board, x_cord, y_cord):   #Klar
    free_place = is_free(x_cord,y_cord)
    if free_place is False:
        for player, cords in board.items():
            if (x_cord, y_cord) in cords:
                return player
            else: return False
    else: 
        return "No piece occupies this spot"


def remove_piece(board, x_cord, y_cord):   #funkar EJ med tanke på att ADD inte funkar
    free_place=is_free(x_cord,y_cord)
    if free_place is True:
        cords = board.get
        cords.append((x_cord,y_cord))
        board.pop({cords})
        return True
    else:
        False


def nearest_piece(board, x_cord, y_cord):
    x=x #Return Cords

def count(board, colum_row, nr, player):
    x=x # returna hur många som finns på den raden

place_piece(board, 1, 1, "Fe1ixJ")
print(is_free(board,1,1))
    #ASSÅ JAG HATAR DETTA