
import keyboard
import pyautogui
import mouse
import time
import webbrowser


from connect4 import Connect4
from mcts import ucb2_agent


start_button = 'p'


keyboard.wait(start_button)

def get_grid_coords(grid):

    xs = [int(grid.left + grid.width // 14 + i * grid.width // 7) for i in range(7)]
    ys = [int(grid.top + grid.height // 12 + i * grid.height // 6) for i in range(6)]

    coords = []
    for y in ys:
        row = []
        for x in xs:
            row.append((x, y))
        coords.append(row)
    return coords

def turn_first(grid, coords):

    mouse.move(coords[3][3][0], coords[3][3][1])
    time.sleep(0.1)
    mid_x = (coords[3][3][0] + coords[4][3][0]) // 2
    mid_y = (coords[3][3][1] + coords[4][3][1]) // 2
    pixel = pyautogui.pixel(mid_x, mid_y)
    

    light_gray = pix_equal(pixel, (206, 212, 218))  
    return not light_gray


def pix_equal(pixel, goal):
    return pixel[0] == goal[0] and pixel[1] == goal[1] and pixel[2] == goal[2]


def board_move(board, loc, turn):
    for i in range(len(board)-1, -1, -1):
        if board[i][loc] == 0:
            board[i][loc] = 1 if turn == 0 else 2
            break


def run(grid):    

     coords = get_grid_coords(grid)
     
          

     pos = Connect4().get_initial_position()
     board = [[0 for _ in range(7)] for _ in range(6)]
     
     

     first_player = turn_first(grid, coords)


     strategy = ucb2_agent(7)

     while not pos.terminal:

        if (first_player and pos.turn == 0) or (not first_player and pos.turn == 1):

            move = strategy(pos)
            

            mouse.move(coords[0][move][0], coords[0][move][1])
            mouse.click()
            

            board_move(board, move, pos.turn)
            pos = pos.move(move)

        else:

             found_move = False
             for i in range(len(coords)):
                 for j in range(len(coords[0])):
                     if found_move: continue
                     pix = pyautogui.pixel(coords[i][j][0], coords[i][j][1])
                     

                     if not pix_equal(pix, (255, 255, 255)) and board[i][j] == 0:
                         board_move(board, j, pos.turn)
                         pos = pos.move(j)
                         found_move = True
     return board, pos
 
grid = None
while grid is None:            
    grid = pyautogui.locateOnScreen('grid.png', confidence = 0.95)
print("Found grid")
board, pos = run(grid)