from re import X
from tkinter import Y
import pygame

from main import Win
from.Pieces import *
from.constants import *

class newBoard:
    def __init__(self, width, height, rows, cols, square, win):
        self.width = width
        self.height = height
        self.square = square
        self.win = win
        self.rows = rows
        self.cols = cols
        self.board = []
        self.create_board()

    def create_board(self):
        for row in range(self.rows):
            self.board.append([0 for i in range(self.cols)])

            for col in range(self.cols):
                if row == 1:
                    self.board[row][col] = pawn(self, Square, Black_pawn, Brown, "Pawn", row, col)
                    
                if row == 6:
                    self.board[row][col] = pawn(self, Square, White_pawn, White, "Pawn", row, col)
                    
                if row == 0:
                    if col == 0 or col == 7:
                        self.board[row][col] = Rook(self.square, Black_Rook, Brown, "Rook", row, col)
                        
                    if col == 1 and col == 6:
                        self.board[row][col] = Knight(self.square, Black_Knight, Brown, "Knight", row, col)
                        
                    if col == 2 and col == 5:
                        self.board[row][col] = Bishop(self.square, Black_Bishop, Brown, "Bishop", row, col)
                           
                    if col == 3:
                        self.board[row][col] = Queen(self.square, Black_Queen, Brown, "Queen", row, col)
                        
                    if col == 4:
                        self.board[row][col] = King(self.square, Black_king, Brown, "King", row, col)            
                    
                if row == 7:
                    if col == 0 or col == 7:
                        self.board[row][col] = Rook(self.square, White_Rook, White, "Rook", row, col)
                        
                    if col == 1 and col == 6:
                        self.board[row][col] = Knight(self.square, White_Knight, White, "Knight", row, col)
                        
                    if col == 2 and col == 5:
                        self.board[row][col] = Bishop(self.square, White_Bishop, White, "Bishop", row, col)
                           
                    if col == 3:
                        self.board[row][col] = Queen(self.square, White_Queen, White, "Queen", row, col)
                        
                    if col == 4:
                        self.board[row][col] = King(self.square, White_king, White, "King", row, col)
                       
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        
        piece.piece_move(row,col)
        
        if piece.type == "Pawn":
            if piece.first_move:
                piece.first_move = False
                
    def draw_board(self):
        self.win.fill(Brown)
        
        for row in range(self.rows):
            for col in range(row%2, Cols, 2):
                pygame.draw.rect(self.win, White, (Square*(row), Square*(col), Square, Square))
    
    def draw_piece(self, piece, Win):
        Win.blit(piece.image, (piece.x, piece.y))
        
    def draw_pieces(self):
        for row in range(self.Rows):
            for col in range(self.Cols):
                if self.board[row][col] != 0:
                    self.draw_piece(self.board[row][col], self.win)
                    
                                   
                    
                
