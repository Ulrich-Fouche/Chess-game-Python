from sqlite3 import Row
from Chess_Game.Pieces import Piece
from .board import newBoard
from .constants import *

class Game:
    def __init__(self, Width, Height, Rows, Cols, Square, Win):
        self.Win = Win
        self.Board = newBoard(Width, Height, Rows, Cols, Square, Win)
        self.Square = Square
        self.selected = None
        self.turn = White
        self.valid_move = []
        self.Black_pieces_left = 16
        self.White_pieces_left = 16
        
    def update_window(self):
        self.board.draw_board()
        self.board.draw_piece()
        self.draw_available_moves()
        
    def reset(self):
        self.board = newBoard(Width, Height, Rows, Cols, Square, Win)
        self.selected = None
        self.Black_pieces_left, self.White_pieces_left = 16,16
        self.valid_move = []
        
    def change_turn(self):
        if self.turn == White:
            self.turn = Brown 
            
        else:
            self.turn = White  
            
    def select(self, Row, Col):
        if self.selected:
            move = self.move(Row, Col)
            
            if not move:
                self.selected = None
                self.selected(Row, Col)
                
        Piece = self.Board.get_piece(Row, Col)
        
        if Piece != 0 and self.turn == Piece.color:
            self.selected = Piece
            
            self.valid_move = Piece.get_available_moves(Row, Col, self.Board.Board)
            
    def _move(self, Row, col):
        Piece = self.Board.get_piece(Row, col)
        
        if self.selected and (Row, col) in self.valid_move:
            if Piece == 0 or Piece.color != self.selected.color:
               if self.simulate_move(self.selected, Row, col):
                   self.remove(self.selected,Row,col)
                       
                   self.Board.move(self.Board.Board, Piece, Row, col)
                   self.change_turn()
                   self.valid_move = []
                   self.selected = None
                   return True
               return False
           
        return False
    
    def remove(self, Board, Piece, Row, Col):
        if Piece != 0:
            Board[Row][Col] = 0
            if Piece.color == White:
                self.White_pieces_left -= 1
            else:
                self.Black_pieces_left -= 1
                
    def draw_available_moves(self):
        if len(self.valid_move) > 0:
            for pos in self.valid_move:
                Row, col = pos[0], pos[1]
                pygame.draw.circle(self.Win, Green, (col*self.Square + self.Square//8))
                
                
                        
