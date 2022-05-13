
import pygame


startList = [i for i in range(100)]

def printList(l):
    for i, x in enumerate(l):
        print(x)

def BubbleSort(l):
    print(l)

functionDic = {
    "BubbleSort" : 0
}

def CaseMachine(value, l):
    match value:
        case 0:
            BubbleSort(l)

def Sort(function, l):
    CaseMachine(functionDic[function],l)


Sort("BubbleSort", startList)