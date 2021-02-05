#!/usr/bin/env python
# coding: utf-8

# In[9]:


# X's are 1s and Os are 2s, emtpy is 0s
possible3s = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
def DoMove(position, move):
    return move


# In[10]:


def GenerateMoves(position):
    possibleMoves = []
    board = convertToBoard(position)
    if not isValidBoard(board):
        return []
    playerType = findPlayer(board)
    availablePositions = findAvailablePositions(board)
    for pos in availablePositions:
        newBoard = board[:]
        newBoard[pos] = playerType
        possibleMoves += [convertFromBoardToDecimal(newBoard)]
    return possibleMoves  


# In[11]:


def PrimitiveValue(position):
    board  = convertToBoard(position) 
    for pot in possible3s:
        toCheck = []
        for x in pot:
            toCheck += [board[x]]
        if toCheck == [1, 1, 1] or toCheck == [2, 2, 2]:
            return "lose"
    if isFull(board):
        return "tie"
    return "not_primitive"


# In[14]:


def findPlayer(board):
    numX = 0
    num0 = 0
    for pos in board:
        if pos == 1:
            numX += 1
        elif pos == 2:
            num0 += 1
    if numX == num0:
        return 1
    elif numX - 1 == num0:
        return 2
    else:
        return 0
def hasThreeInRow(pos):
    board = convertToBoard(pos)
    found3inrow = False
    playerType = 0
    for pot in possible3s:
        toCheck = []
        for x in pot:
            toCheck += [board[x]]
        if toCheck == [1, 1, 1]:
            found3inrow = True
            playerType = 1
        elif toCheck == [2, 2, 2]:
            found3inrow = True
            playerType = 2
    return (found3inrow, playerType)
def hasThreeInRowOrFull(pos):
    board = convertToBoard(pos)
    found3inrow = False
    for pot in possible3s:
        toCheck = []
        for x in pot:
            toCheck += [board[x]]
        if toCheck == [1, 1, 1] or toCheck == [2, 2, 2]:
            found3inrow = True
    if found3inrow:
        return True
    elif not found3inrow and isFull(board):
        return True
    return False
    
def isValidBoard(board):
    found3inrow = False
    for pot in possible3s:
        toCheck = []
        for x in pot:
            toCheck += [board[x]]
        if toCheck == [1, 1, 1] or toCheck == [2, 2, 2]:
            if found3inrow:
                return False
            found3inrow = True
    if found3inrow:
        return False
    numX = 0
    num0 = 0
    for pos in board:
        if pos == 1:
            numX += 1
        elif pos == 2:
            num0 += 1
    if numX == num0:
        return True
    elif numX - 1 == num0:
        return True
    else:
        return False
            
def isFull(board):
    if findAvailablePositions(board) == []:
        return True
    return False
def findAvailablePositions(board):
    result = []
    for i in range(len(board)):
        if board[i] == 0:
            result += [i]
    return result
def convertToTernary(N):
    ternary = 0
    iteration = 0
    while N:
        x = N % 3
        N //= 3
        ternary += (10**iteration) * x
        iteration += 1
    return ternary
#converts a decimal number to ternary represented as array
def convertToBoard(N):
    board = []
    iteration = 0
    while iteration < 9:
        if N == 0:
            board += [0]
            iteration += 1
            continue
        x = N % 3
        N //= 3
        board += [x]
        iteration += 1
    return board

def convertFromBoardToDecimal(board):
    decimal = 0
    place = 0
    for pos in board:
        decimal += 3**place*pos
        place += 1
    return decimal
    

def convertToDecimal(N):
    decimal = 0
    place = 0
    while N:
        x = N % 10
        N //= 10
        decimal += 3**place*x
        place += 1
    return decimal

        
    


# In[15]:


def getPositions():
    validPositions = [0]
    startingPosition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    validBoards = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    toConsider = GenerateMoves(convertFromBoardToDecimal(startingPosition))
    while toConsider:
        toConsiderCopy = []
        for x in toConsider:
            if convertToBoard(x) not in validBoards:
                validBoards += [convertToBoard(x)]
                validPositions += [x]
            toConsiderCopy += GenerateMoves(x)
        toConsider = toConsiderCopy
    return validPositions
    

    


# In[ ]:




