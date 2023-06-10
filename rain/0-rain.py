#!/bin/python3
def rain(walls):
    if len(walls) == 0:
        return 0
    for i in range(1, len(walls)):
        if (walls[i] >= walls[i-1]):
            amount += walls[i-1]
        else:
            amount += walls[1]
        i+=1
    return amount
