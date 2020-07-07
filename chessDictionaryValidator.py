
def isValidChessBoard(chessDict):
    # checking for a total of 16 pieces per player
    bPieces=0
    wPieces=0

    for total in chessDict.values():
        if total[0]=='b':
            bPieces+=1
        elif total[0]=='w':
            wPieces+=1
    if bPieces >= 17 or wPieces >= 17:
        return False
    
    # checking for the white and the black king
    if 'bking' not in chessDict.values() or 'wking' not in chessDict.values():
        return False  

    bKing=0
    wKing=0

    for king in chessDict.values():
        if king=='bking':
            bKing+=1
        elif king=='wking':
            wKing+=1
    if bKing != 1 or wKing != 1:
        return False
    
    #checking for 8 pawns per player
    blackpawn=0
    whitepawn=0

    for pawn in chessDict.values():
        if pawn=='bpawn':
            blackpawn+=1
        if pawn=='wpawn':
            whitepawn+=1
    if blackpawn >= 9 or whitepawn >= 9:
        return False
    #if sum(i == "bpawn" for i in board_dict.values()) >= 9 or sum(i == "wpawn" for i in board_dict.values()) >= 9:
    #    return False


    #checking if the piece is on valid space
    board_keys = list(chessDict.keys())
    y = ["1", "2", "3", "4", "5", "6", "7", "8"]
    board_keys_1st_digit = [s[:1] for s in board_keys] #creates a list of only digits by removing letters
    if not all(q in y for q in board_keys_1st_digit): #all returns True if all elements in the given iterable are true
        return False
    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board_x = [s[1:] for s in board_keys]  # removes numbers from list. eg: ['h', 'c', 'g', 'h', 'e']
    if not all(elem in x for elem in board_x):  # checks if all values from board_x are in the x-list
        return False
    
    #checking for a valid name    
    for l in chessDict.values():
        if l[0] != 'w' and l[0] != 'b':
            return False

    # check if the piece name is valid
    piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for names in chessDict.values():
        if names[1:] not in piece_names:
            return False

    return True


chess={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(chess))