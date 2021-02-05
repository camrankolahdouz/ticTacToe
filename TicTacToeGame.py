#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from ticTacToe import *
from solver import *


# In[ ]:


def toString(board):
    copyBoard = board[:]
    for i in range(len(board)):
        if board[i] == 0:
            copyBoard[i] = '*'
        elif board[i] == 1:
            copyBoard[i] = 'X'
        else:
            copyBoard[i] = 'O'
    strBoard = ''
    x = 0
    for i in range(-1,6):

        if i%2==0:
            strBoard += '|       ' * 4
            strBoard += '\n|   ' + (copyBoard[x])+ '   |   ' + (copyBoard[x + 1]) + '   |   ' + (copyBoard[x + 2]) + '   |'
            x += 3

        else:
            strBoard += ' _____  ' * 3

        strBoard += '\n'
    print(strBoard)

def toStringStart(board):
    copyBoard = board[:]
    strBoard = ''
    x = 0
    for i in range(-1,6):

        if i%2==0:
            strBoard += '|       ' * 4
            strBoard += '\n|   ' + str(copyBoard[x])+ '   |   ' + str(copyBoard[x + 1]) + '   |   ' + str(copyBoard[x + 2]) + '   |'
            x += 3

        else:
            strBoard += ' _____  ' * 3

        strBoard += '\n'
    print(strBoard)


# In[ ]:


def makeHalMove(pos, positionMap):
    possibleMoves = GenerateMoves(pos)
    foundTie = False
    tieState = 0
    winState = 0
    for i in possibleMoves:
        if positionMap[str(i)] == "lose":
            return i
        elif positionMap[str(i)] == "tie":
            foundTie= True
            tieState = i
        else:
            winState = i
            
    if foundTie:
        return tieState
    return winState
            
    


# In[ ]:


def onePlayerGame(pos, positionMap):
    i = 0
    board = convertToBoard(pos)
    while not hasThreeInRowOrFull(pos):
        board = convertToBoard(pos)
        toString(board)
        if i % 2 == 0:
            print("Player 1's turn, please place an X in an empty square by inputting that tile number, starting at the top left corner as 0, ex: Input 0 for the top left")
            move = int(input())
            while move < 0 or move > 8:
                print("This is not a valid move, try again")
                move = int(input())
            while board[move] != 0:
                print("This is not a valid move, try again")
                move = int(input())
            pieceType = 1
            board[move] = pieceType
            pos = convertFromBoardToDecimal(board)
            
        else:
            print("Hal's Turn!!")
            pos = makeHalMove(pos, positionMap)
        i += 1
    if not hasThreeInRow(pos)[0] and isFull(board):
        print("Game Over, ended as a Tie")
        toString(board)
        
    elif hasThreeInRow(pos)[0]:
        if hasThreeInRow(pos)[1] == 2:
            print("Game Over, Hal is the winner!")
            board = convertToBoard(pos)
            toString(board)
            return
            
        print("Game Over, player " + str(hasThreeInRow(pos)[1]) + " is the winner!")
        toString(board)
        
    return
        
    


# In[ ]:


def twoPlayerGame(pos):
    i = 0
    board = convertToBoard(pos)
    while not hasThreeInRowOrFull(pos):
        board = convertToBoard(pos)
        toString(board)
        if i % 2 == 0:
            print("Player 1's turn, please place an X in an empty square by inputting that tile number, starting at the top left corner as 0, ex: Input 0 for the top left")
            move = int(input())
            while move < 0 or move > 8:
                print("This is not a valid move, try again")
                move = int(input())
            pieceType = 1
        else:
            print("Player 2's turn, please place an O in an empty square by inputting that tile number, starting at the top left corner as 0, ex: Input 0 for the top left")
            move = int(input())
            while move < 0 or move > 8:
                print("This is not a valid move, try again")
                move = int(input())
            pieceType = 2
        while board[move] != 0:
            print("This is not a valid move, try again")
            move = int(input())
        board[move] = pieceType
        pos = convertFromBoardToDecimal(board)
        i += 1
    if not hasThreeInRow(pos)[0] and isFull(board):
        print("Game Over, ended as a Tie")
        toString(board)
        main()
    elif hasThreeInRow(pos)[0]:
        print("Game Over, player " + str(hasThreeInRow(pos)[1]) + " is the winner!")
        toString(board)
        main()
    return
        
            
            
        
    


# In[ ]:


def main():
    with open('positionMap.json', 'r') as fp:
        positionMap = json.load(fp)
    with open('primPositionMap.json', 'r') as fp:
        primPositionMap = json.load(fp)
    a = """
    Welcome to a game of TicTacToe, written by Camran Kolahdouz-Isfahani.
    To make a move, for instance to place the first X at the bottom left tile, you should input 6. The top right 
    square is 2. The top left is 0, the bottom right is 8.
    The game is easily solveable, so good luck. Note if you are playing Hal you get first move, just so you sorta 
    have a chance.  
    """
    print(a)
    toStringStart([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print("Input 1 if you want to play one player (against Hal), or a 2 if you have a human friend")
    resp = int(input())
    if resp == 1:
        onePlayerGame(convertFromBoardToDecimal([0, 0, 0, 0, 0, 0, 0, 0, 0]), positionMap)
    else: 
        twoPlayerGame(convertFromBoardToDecimal([0, 0, 0, 0, 0, 0, 0, 0, 0]))
    
    
    
    
    

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




