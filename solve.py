from stockfish import Stockfish

stockfish = Stockfish("stockfish_20011801_x64.exe")

print(stockfish.get_board_visual())

def process_pieces(piece_strings):
    pieces = []

    for piece in piece_strings:
        piece_type, piece_position = "", -1
        proc = piece.split(" ")[1:]

        if(len(proc) == 0):
            continue

        if(len(proc[0]) == 2):
            piece_type = proc[0]
            piece_position = proc[1]
        else:
            piece_type = proc[1]
            piece_position = proc[0]
        
        pieces.append((int(piece_position.split("-")[1]), piece_type))
    return pieces

def get_fen(pieces, side):
    fen = ""

    if(side == "b"):
        for p in range(len(pieces)):
            pieces[p] = (10*(9-pieces[p][0]//10) + pieces[p][0]%10, pieces[p][1])

    row_pieces = [[] for _ in range(8)]
    pieces.sort()

    for p in pieces:
        row_pieces[p[0]%10 - 1].append(p)

    for row in range(8):
        row_fen = ""

        if(side == "w"):
            row_pieces[row] = row_pieces[row][::-1]
        c = 0
        lp = 0

        for p in range(len(row_pieces[row])):

            if(row_pieces[row][p][0]//10 - lp > 1):
                row_fen += str(row_pieces[row][p][0]//10 - lp - 1)

            piece_string = str(row_pieces[row][p][1])
            if(piece_string[0] == 'w'):
                row_fen += str(row_pieces[row][p][1][1]).upper()
            elif(piece_string[0] == 'b'):
                row_fen += str(row_pieces[row][p][1][1])

            lp = (row_pieces[row][p][0]//10)

        if(8 - lp >= 1):
            row_fen += str(8 - lp)
        
        fen += row_fen + "/"
    fen = fen[:-1]
        
    return fen + f" {side} KQkq - 0 0"




