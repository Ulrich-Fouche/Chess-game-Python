Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows
Game_Over = False
Win = False

Brown = (87,16,16)
White = (255,255,255)
Green = (0, 255, 0)


Path = "Chess_Game\Chess_image"

#black pieces
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bkN.png")),(Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bB.png")),(Square, Square))
Black_king = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bK.png")),(Square, Square))
Black_pawn = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bP.png")),(Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bQ.png")),(Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bR.png")),(Square, Square))
#white
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wKN.png")),(Square, Square))
White_Bishop = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wB.png")),(Square, Square))
White_king = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wK.png")),(Square, Square))
White_pawn = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wP.png")),(Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wQ.png")),(Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wR.png")),(Square, Square))



