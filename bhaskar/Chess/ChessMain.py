# This is the main driver code responsible of user input


import pygame as p
import ChessEngine
import random

# from Chess import ChessEngine  #this is not working

WIDTH = HEIGHT = 800  # 400 is another option
DIMENSION = 8  # CHESSBOARD 8*8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # FOR ANIMATION LATER ON
IMAGES = {}
# some colors
green = (0, 255, 0) 
blue = (0, 0, 128) 

p_image = p.image.load("images/b.png")
p_image = p.transform.scale(p_image, (850, 850))
c_image = p.image.load("images/cross.png")
c_image = p.transform.scale(c_image, (70, 70))
background2 = p.image.load("images/background2.jpg")

# load image will initialize a global dictionary of images only once in a code


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK',
              'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        # IMAGES[piece] =p.image.load("./"+piece+".png" )
        IMAGES[piece] = p.transform.scale(p.image.load(
            "images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))

#for diplaying text on the screen

def show_text(x, y, font_size, color, screen,msg_string):
    font = p.font.Font('freesansbold.ttf', font_size)
    startq = font.render(msg_string, True, color)
    screen.blit(startq, (y, x))

def show_text1(x, y, font_size, color, screen,msg_string):
    font = p.font.Font('font/Ubuntu-Medium.ttf', font_size)
    startq = font.render(msg_string, True, color)
    screen.blit(startq, (y, x))

def acknowledge_screen(clock):
    flag_start = True
    time_elapsed = 0

    while flag_start:
        screen = p.display.set_mode((WIDTH+50, HEIGHT+50))
        screen.fill(p.Color(0x000F0F))
        screen.blit(background2, (0, -16))
        
        for e in p.event.get():
            if e.type == p.QUIT:
                flag_start = False

            if e.type == p.KEYUP:
                if e.key == ord('q') or e.key == ord('Q'):
                    flag_start = False

        dt = clock.tick()
        time_elapsed = time_elapsed + dt

        # write what you want to write in aknowleddge screen
        show_text1(0,246,64,0x5B84B1FF,screen,'Chess Game')
        show_text(200,300,24,0x4b878bff,screen,'Team : Well Forked')

        show_text(820,10,20,0xFC766AFF,screen,'Press q to move to main menu')
        
        if time_elapsed > 1000 :
            flag_start = False

        clock.tick(MAX_FPS)
        p.display.flip()

def show_startscreen(clock):
    start_screen = True
    while start_screen:

        screen = p.display.set_mode((WIDTH+50, HEIGHT+50))
        screen.fill(p.Color(0x000F0F))
        screen.blit(p_image,(0,0))
        screen.blit(c_image,(780,0))
        
        for e in p.event.get():
            if e.type == p.QUIT:
                #start_screen = False
                #running = False
                return [False,False]

            if e.type == p.MOUSEMOTION:
                x, y = e.pos
                if x >=780 and y <=70:
                    #print("Hovering over the item!")
                    p.mouse.set_cursor(*p.cursors.broken_x)
                elif(x in range(240,600)) and (y in range(550,580)) :
                    p.mouse.set_cursor(*p.cursors.broken_x)
                elif(x in range(240,600)) and (y in range(600,630)) :
                    p.mouse.set_cursor(*p.cursors.broken_x)
                elif(x in range(235,605)) and (y in range(650,680)) :
                    p.mouse.set_cursor(*p.cursors.broken_x)
                else: 
                    p.mouse.set_cursor(*p.cursors.arrow)

            if e.type == p.MOUSEBUTTONDOWN:
                loc_mouse = p.mouse.get_pos()
                #screen.blit(cursor, cursor_rect)
                col = loc_mouse[0]
                row = loc_mouse[1]
                if col>=780 and row <= 70:
                    return [False,False,False]
                elif (col in range(240,600)) and (row in range(550,580)) :
                    return [True,False,False]
                elif (col in range(240,600)) and (row in range(600,630)) :
                    return [True,True,False]
                elif (col in range(235,605)) and (row in range(650,680)) :
                    return [True,False,True]

            if e.type == p.KEYUP:

                if e.key == ord('q') or e.key == ord('Q'):
                    return [False,False,False]

                if e.key == ord('n') or e.key == ord('N'):
                    return [True,False,False]
                
                if e.key == ord('f') or e.key == ord('F'):
                    return [True,True,False]
                
                if e.key == ord('g') or e.key == ord('G'):
                    return [True,False,True]

        show_text1(0,246,64,0x5B84B1FF,screen,'Chess Game')
        """ show_text(30,10,24,blue,screen,'Team : Well Forked')
        show_text(60,10,24,blue,screen,'1) Member')
        show_text(90,10,24,blue,screen,'2) Member')
        show_text(120,10,24,blue,screen,'3) Member')
        show_text(150,10,24,blue,screen,'4) Member')
        show_text(180,10,24,blue,screen,'5) Member')
        show_text(210,10,24,blue,screen,'6) Member') """
        show_text(550,240,28,green,screen,'for Normal Chess Press n')
        show_text(600,240,28,green,screen,'for Fischer Chess Press f')
        show_text(650,218,28,green,screen,'to make Chess board Press g')
        show_text(820,10,20,0xFC766AFF,screen,'Press q to exit')

        clock.tick(MAX_FPS)
        p.display.flip()
    
    #screen.fill(p.Color(0x000F0F))
    return [True,False,False]

def show_endscreen(clock,msg):
    flag_start = True
    time_elapsed = 0

    while flag_start:
        screen = p.display.set_mode((WIDTH+50, HEIGHT+50))
        screen.fill(p.Color(0x000F0F))
        screen.blit(p_image,(0,0))
        screen.blit(c_image,(780,0))
        for e in p.event.get():
            if e.type == p.QUIT:
                flag_start = False
                return False
            
            if e.type == p.MOUSEMOTION:
                x, y = e.pos
                if x >=780 and y <=70:
                    p.mouse.set_cursor(*p.cursors.broken_x)
                elif (x in range(235,605)) and (y in range(650,680)) :
                    p.mouse.set_cursor(*p.cursors.broken_x)
                else: 
                    p.mouse.set_cursor(*p.cursors.arrow)

            if e.type == p.MOUSEBUTTONDOWN:
                loc_mouse = p.mouse.get_pos()
                col = loc_mouse[0]
                row = loc_mouse[1]
                if col>=780 and row <= 70:
                    flag_start = False
                    return False
                elif (col in range(235,605)) and (row in range(650,680)) :
                    flag_start = False
                    return True

            if e.type == p.KEYUP:
                if e.key == ord('q') or e.key == ord('Q'):
                    flag_start = False
                    return False

            if e.type == p.KEYUP:
                if e.key == p.K_KP_ENTER:
                    flag_start = False
                    return True

        dt = clock.tick()
        time_elapsed = time_elapsed + dt
        show_text1(0,246,64,0x5B84B1FF,screen,'Chess Game')
        #msg = "nikal be"
        show_text(100,240,24,0x4b878bff,screen,msg)
        show_text(650,235,28,green,screen,'Press Enter for Main menu')
        show_text(820,10,20,0xFC766AFF,screen,'Press q to exit')
        
        if time_elapsed > 6000 :
            flag_start = False
            return True

        clock.tick(MAX_FPS)
        p.display.flip()
    
    return True

def is_random_function():
    old_board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    random.shuffle(old_board[0])
    random.shuffle(old_board[7])
    return old_board

def is_fischer_function():
    old_board = is_random_function()
    rook_flag = 0
    idx = 0
    rookies=["bR","wR"]
    for x in rookies :
        rook_flag = 0
        if x == "wR":
            idx = 7
        for i in range(8):
            if old_board[idx][i] == x and not rook_flag:
                rook_flag = 1
                if i == 0:
                    continue
                chang = [0,7]
                val = random.choice(chang)
                old_board[idx][i] = old_board[idx][val]
                old_board[idx][val]= x
                break
    idx = 0
    kings = ["bK","wK"]
    for x in kings :
        if x == "wK":
            idx = 7
        for i in range(8):
            if old_board[idx][i] == x :
                if i == 4:
                    continue
                old_board[idx][i] = old_board[idx][4]
                old_board[idx][4]= x
                break
    
    return old_board
        

def is_fill_function():
    old_board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    black_pawns = ["bR", "bN", "bB", "bQ", "bK"]
    black_pawns_num = [2,2,2,1,1]
    str_color = 'b'
    i = 0
    print("Enter Black Pawns")
    print("Enter N,B,R,K,Q")
    while i < 8 :
        input_str = input("Enter :")
        s = str_color + input_str
        old_board[0][i] = s
        index = -1
        for j in black_pawns:
            if s == j:
                index = black_pawns.index(j)
        if index == -1:
            print("Enter correct values")

        if black_pawns_num[index] != 0:
            black_pawns_num[index] -=1
            i+=1          
        else:
            print("Enter correct values")
    white_pawns = ["wR", "wN", "wB", "wQ", "wK"]
    white_pawns_num = [2,2,2,1,1]
    str_color = 'w'
    i = 0
    print("Enter White Pawns")
    print("Enter N,B,R,K,Q")
    while i < 8 :
        input_str = input("Enter :")
        s = str_color + input_str
        old_board[7][i] = s
        index = -1
        for j in white_pawns:
            if s == j:
                index = white_pawns.index(j)
        if index == -1:
            print("Enter correct values")

        if white_pawns_num[index] != 0:
            white_pawns_num[index] -=1
            i+=1          
        else:
            print("Enter correct values")
    
    return old_board
 
# this will be main driver it will handle
# user input and update the graphics

def main():
    p.init()
    clock = p.time.Clock()
    start_screen = True
    end_screen = False
    running = True
    is_fischer = False
    is_random = False
    acknowledge_screen(clock)
    screen = p.display.set_mode((WIDTH+50, 50+HEIGHT))
    screen.fill(p.Color(0x000F0F))
    gs = ChessEngine.GameState()
    # print(gs.board)

    validMoves = gs.getValidMoves()
    moveMade = False  # flag variable when a move is made
    animate = False #flag variable for when we should animate a move
    loadImages()
    initial = ()
    final = ()
    sqSelected = ()  # keeps track of last call of user
    playerClicks = []  # keeps track of players click
    gameOver = False
    msg = ''
    while running:
        if start_screen:
            return_val = show_startscreen(clock)
            screen = p.display.set_mode((WIDTH+50, 50+HEIGHT))
            screen.fill(p.Color(0x000F0F))
            running = return_val[0]
            is_fischer = return_val[1]
            is_random = return_val[2]
            if is_random:
                gs.board = is_fill_function()
                is_random = False
            if is_fischer:
                gs.board = is_fischer_function()
                is_fischer = False
            #print(gs.board)
            start_screen = False
            continue
        
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            
            # mouse handler

            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver:
                    location = p.mouse.get_pos()  # get mouse coordinates
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if sqSelected == (row, col):  # reset if clicked on same block
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        # append for both first and second clicks
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:  # after 2nd click
                        move = ChessEngine.Move(
                            playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelected = ()  # reset user clicks
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]

            # key handler

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo a move by pressing z
                    # need to implement this using undo button also %%
                    gs.undoMove()
                    moveMade = True
                    animate = False
                if e.key == p.K_r: #reset the board when 'r' is pressed
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    final = ()
                    initial = ()
                    sqSelected = ()
                    final=()
                    initial=()
                    playerClicks = []
                    moveMade = False
                    animate = False
                if e.key == p.K_m:
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    final = ()
                    initial = ()
                    sqSelected = ()
                    final=()
                    initial=()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    start_screen = True
                    continue

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False
            # if(gs.moveLog[-1]):
            if(len(gs.moveLog)>=1):
                final = (gs.moveLog[-1].endRow, gs.moveLog[-1].endCol)
                initial = (gs.moveLog[-1].startRow, gs.moveLog[-1].startCol)
            else:
                initial = ()
                final = ()

        drawGameState(screen, gs, validMoves, sqSelected, initial ,final)
        if gs.checkMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, 'Black wins by checkmate')
                msg = 'Black wins by checkmate'
            else:
                drawText(screen, 'White wins by checkmate')
                msg = 'White wins by checkmate'
            end_screen = True
        elif gs.staleMate:
            gameOver = True
            drawText(screen, 'Stalemate')
            msg = 'Draw'
            end_screen = True
        
        if end_screen:
            return_val = show_endscreen(clock,msg)
            if not return_val:
                running = False
            gs = ChessEngine.GameState()
            validMoves = gs.getValidMoves()
            final = ()
            initial = ()
            sqSelected = ()
            final=()
            initial=()
            playerClicks = []
            moveMade = False
            animate = False
            end_screen = False
            start_screen = True

        clock.tick(MAX_FPS)
        p.display.flip()

#highlight last move made by opponent
def lastMove(screen, gs, initial, final):
    if initial != () and final != ():
        ri, ci = initial
        rf, cf = final
        si = p.Surface((SQ_SIZE, SQ_SIZE))
        si.set_alpha(100)
        si.fill(p.Color('green'))
        sf = p.Surface((SQ_SIZE, SQ_SIZE))
        sf.set_alpha(100)
        sf.fill(p.Color('purple'))
        # print(initial, final)
        screen.blit(si, (ci*SQ_SIZE, ri*SQ_SIZE))
        screen.blit(sf, (cf*SQ_SIZE, rf*SQ_SIZE))

# Highlight square selected and moves for piece selected
def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'): # square selected is a piece that can be moved
            # highlight selected square
            s = p.Surface((SQ_SIZE,SQ_SIZE))
            s.set_alpha(100) # transparency value (0,255)
            s.fill(p.Color('blue'))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            #highlight moves from that square
            s.fill(p.Color('yellow'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol*SQ_SIZE, move.endRow*SQ_SIZE))



# Responsible for all the graphics within a current game state

def drawGameState(screen, gs, validMoves, sqSelected, initial ,final):
    drawBoard(screen)  # drawa sqares on board
    # add in piece highlighting or move suggestion (later)
    lastMove(screen, gs,initial ,final)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


# Draw the squares on the board top left is always white

def drawBoard(screen):
    global colors
    colors = [p.Color(202,164,114), p.Color(93,67,44)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            # color = colors[((1) % 2)]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    for r in range(1,9):
        var=chr(96+r)
        drawText2(screen,var,r*100-50,825)
    for r in range(1,9):
        var=chr(48-r+9)
        drawText2(screen,var,825,r*100-50)
    


# Draw the pieces on the board using the current GameState.board

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(
                    c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Animating a move
def animateMove(move, screen, board, clock):
    global colors
    coords = [] # list of coords that the animation will move through
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10 #frames to move one square
    frameCount = (abs(dR) + abs(dC))*framesPerSquare
    for frame in range(frameCount + 1):
        r, c = ((move.startRow + dR*frame/frameCount, move.startCol + dC*frame/frameCount))
        drawBoard(screen)
        drawPieces(screen, board)
        #erase the pice moved from its ending swuare
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = p.Rect(move.endCol*SQ_SIZE, move.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, color, endSquare)
        # draw captured piece onto rectangle
        if move.pieceCaptured != '--':
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        #draw moving piece
        screen.blit(IMAGES[move.pieceMoved], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)


def drawText(screen, text):
    font = p.font.SysFont("Helvitca", 32, True, False)
    textObject =  font.render(text, 0, p.Color('Gray'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, 0, p.Color("Black"))
    screen.blit(textObject, textLocation.move(2,2))

def drawText2(screen, text ,a,b):
    font = p.font.SysFont("Helvitca", 50, True, False)
    textObject =  font.render(text, 0, p.Color('Gray'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(a - textObject.get_width()/2, b - textObject.get_height()/2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, 0, p.Color("white"))
    screen.blit(textObject, textLocation.move(2,2))




if __name__ == "__main__":
    main()
