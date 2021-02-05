#!/usr/bin/env python
# coding: utf-8

# In[4]:

from ticTacToe import *
import json

LOSE, WIN, TIE = "lose", "win", "tie"
positionMap = {}
def solve(position):
    if position in positionMap:
        return positionMap[position]
    if PrimitiveValue(position) != "not_primitive":
        return PrimitiveValue(position)
    children = GenerateMoves(position)
    foundTie = False
    for move in children:
        toConsider = solve(DoMove(position, move))
        if toConsider == LOSE:
            positionMap[position] = WIN
            return WIN
        elif toConsider == TIE:
            foundTie = True
        else:
            continue
    if foundTie:
        positionMap[position] = TIE
        return TIE     
    positionMap[position] = LOSE
    return LOSE
            
    
        


# In[5]:


def solveIt():
    validPositions = getPositions()
    primitivePositionMap = {}
    positionMap = {}
    for pos in validPositions:
        primitiveValue = PrimitiveValue(pos)
        if primitiveValue == TIE:
            primitivePositionMap[pos] = TIE
        elif primitiveValue == LOSE:
            primitivePositionMap[pos] = LOSE
        elif primitiveValue == WIN:
            primitivePositionMap[pos] = WIN
        if solve(pos) == WIN:
            positionMap[pos] = WIN
        elif solve(pos) == LOSE:
            positionMap[pos] = LOSE
        elif solve(pos) == TIE:
            positionMap[pos] = TIE
    with open('positionMap.json', 'w') as fp:
        json.dump(positionMap, fp)
    with open('primPositionMap.json', 'w') as fp:
        json.dump(primitivePositionMap, fp)
    print("success")
    return
    


# In[6]:





# In[ ]:





# In[ ]:




