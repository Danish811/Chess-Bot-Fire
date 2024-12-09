import numpy as np
from chess import Board

def board_to_matrix(board: Board):
    """ First 12 layers (indices 0-11):
        Each corresponds to a specific piece type for each player:
        0 to 5: Pawn, Knight, Bishop, Rook, Queen, King (White).
        6 to 11: Pawn, Knight, Bishop, Rook, Queen, King (Black).
        Layer 12: Encodes the legal moves that are possible on the board at a given state. """

    matrix = np.zeros((13,8,8))
    piece_map = board.piece_map()

    for square, piece in piece_map.items():
        row,col = divmod(square, 8)
        piece_type = piece.piece_type - 1
        piece_color = 0 if piece.color else 6
        matrix[piece_type + piece_color, row, col] = 1
    
    legal_moves = board.legal_moves
    for move in legal_moves:
        to_square = move.to_square
        row_to, col_to = divmod(to_square, 8)
        matrix[12, row_to, col_to] = 1
    
    return matrix

def create_input_for_nn(games):
    X = []
    Y = []