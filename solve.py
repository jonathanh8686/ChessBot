from stockfish import Stockfish

stockfish = Stockfish("./stockfish")

print(stockfish.get_board_visual())

def process_pieces(piece_strings):
    pieces = []

    for piece in piece_strings:
        piece_type, piece_position = "", -1
        proc = piece.split(" ")[1:]

        if(len(proc[0]) == 2):
            piece_type = proc[0]
            piece_position = proc[1]
        else:
            piece_type = proc[1]
            piece_position = proc[0]
        
        pieces.append((int(piece_position.split("-")[1:]), piece_type))
    return pieces

def get_fen(pieces):
    fen = ""
    pieces.sort()

    row_pieces = [[] for _ in range(8)]

    current_line = 1
    for p in pieces:
        row_pieces[p[0]//10].append(p)

    print(row_pieces)

    for row in range(1, 9):
        c = 0
        lp = 0
        for p in range(len(row_pieces[row])):
            if(row_pieces[row][p][0]%10 - lp > 1):
                c += 1
            else:
                if(c != 0):
                    fen += str(c)
                    c = 0
                if(row_pieces[row][p][1][0] == "w"):
                    fen += row_pieces[row][p][1][1]



            lp = row_pieces[row][p][0]

            
            
    return pieces




