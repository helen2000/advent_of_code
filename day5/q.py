import re

input = open("input.txt", "r")
board = []

def setup_board():
    '''
        setup the board
    '''
    board = []
    for i in range(0, 1000):
        board.append(['.'] * 1000) 
    co_arr= []
    for each in input:
        line = each.split("\n")[0]
        cood = line.split(" -> ")
        co_arr.append((cood[0].split(","), cood[1].split(",")))
    
    for pair in co_arr:
        if pair[0][1] == pair[1][1]:
            #y is constant so place x line
            y = int(pair[1][1])
            x1 = int(pair[1][0]) if int(pair[1][0])<int(pair[0][0]) else int(pair[0][0])
            x2 = int(pair[1][0]) if int(pair[1][0])>int(pair[0][0]) else int(pair[0][0])
            for i in range(x1, x2+1):
                if board[y][i] == ".":
                    board[y][i]= 1
                else:
                    board[y][i] +=1
        elif pair[0][0]==pair[1][0]:
            # y is contant so place x line
            x = int(pair[0][0])
            y1 = int(pair[0][1]) if int(pair[0][1])<int(pair[1][1]) else int(pair[1][1])
            y2 = int(pair[0][1]) if int(pair[0][1])>int(pair[1][1]) else int(pair[1][1])
            for i in range(y1, y2+1):
                if board[i][x] == ".":
                    board[i][x] = 1
                else:
                    board[i][x] +=1
        else:
            # diagonal line
            y1 = int(pair[0][1]) if int(pair[1][0])>int(pair[0][0]) else int(pair[1][1])
            y2 = int(pair[1][1]) if int(pair[1][0])>int(pair[0][0]) else int(pair[0][1])
            x1 = int(pair[1][0]) if int(pair[1][0])<int(pair[0][0]) else int(pair[0][0])
            x2 = int(pair[1][0]) if int(pair[1][0])>int(pair[0][0]) else int(pair[0][0])
            mod = 1
            if y1>=y2:
                mod = -1
            for i in range(x1, x2+1):
                if board[y1][i] == ".":
                    board[y1][i]= 1
                else:
                    board[y1][i] +=1
                y1+=mod
                
    return board 

def count_board(count):
    for row in board:
        for value in row:
            if type(value) == int and value>1:
                count +=1
    return count

def print_board():
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if type(board[i][j]) == int:
                board[i][j]= str(board[i][j])
    for row in board:
        print(row)
        
count = 0
board = setup_board()
count = count_board(count)
print_board()
print("overlapping is: ", count)