import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Sorting Visualizer")
WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
CLOCK = pygame.time.Clock()
LIST_LENGTH = 500
COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)


class DropDown():

    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1

class Button():

    def __init__(self, color_menu, x, y, w, h, font, label):
        self.color_menu = color_menu
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.label = label
        self.menu_active = False
        self.clicked = False
        self.hasClicked = False

    def draw(self, surf):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.label, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))
        
    def update(self, event_list):
        if self.clicked:
                self.clicked = False 
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.menu_active:
                self.clicked = True
            
        return self.clicked

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    50, 50, 200, 50, 
    pygame.font.SysFont(None, 30), 
    "Select Algorithm", ["BubbleSort", "MergeSort", "InsertionSort", "CountingSort", "SelectionSort", "CombSort", "HeapSort"])

sortButton = Button(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    300, 50, 200, 50, 
    pygame.font.SysFont(None, 30), 
    "Sort")

shuffleButton = Button(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    550, 50, 200, 50, 
    pygame.font.SysFont(None, 30), 
    "Shuffle")



functionDic = {
    "BubbleSort" : 0,
    "MergeSort" : 1,
    "InsertionSort" : 2,
    "CountingSort" : 3,
    "SelectionSort" : 4,
    "CombSort" : 5,
    "HeapSort" : 6

}

startList = [i for i in range(LIST_LENGTH)]



def printList(l):
    for i, x in enumerate(l):
        print(x)

def BubbleSort(l):
    indexLen = len(l)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexLen):
            UpdateDisplay()
            if (i < indexLen):
                if (l[i] > l[i + 1]):
                    l[i], l[i + 1] = l[i + 1], l[i]
                    sorted = False
    return l

def MergeSort(l):
    
    
    def merge(left, right, merged):
        
        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
        
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor+right_cursor]=left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1
                
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
            
            
        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]
        
        return merged
    
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left, right = MergeSort(l[:mid]), MergeSort(l[mid:])
    UpdateDisplay(l)
    return merge(left, right, l)

def InsertionSort(l):
    for i in range(1, len(l)):
        while l[i-1] > l[i] and i > 0:
            UpdateDisplay()
            l[i-1], l[i] = l[i], l[i-1]
            i -= 1
    return l

def CountingSort(l):
    size = len(l)
    output = [0] * size

    # count array initialization
    count = [0] * size

    # storing the count of each element 
    for m in range(0, size):
        count[l[m]] += 1
        UpdateDisplay()

    # storing the cumulative count
    for m in range(1, size):
        count[m] += count[m - 1]
        UpdateDisplay()

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        UpdateDisplay()
        output[count[l[m]] - 1] = l[m]
        count[l[m]] -= 1
        m -= 1

    for m in range(0, size):
        l[m] = output[m]
        UpdateDisplay()

def SelectionSort(l):
    for i in range(0,len(l)-1):
        p=0
        mini=l[-1]
        for j in range(i,len(l)):
            if l[j]<=mini:
                mini=l[j]
                p=j
                UpdateDisplay()
        l[i],l[p]=l[p],l[i]
        UpdateDisplay()
    return l

def CombSort(l):
    def getNextGap(gap):
        gap = (gap * 10)/13
        if gap < 1:
            return 1
        return int(gap)
    n = len(l)
 
    gap = n
    swapped = True
 
    while gap !=1 or swapped == 1:
        UpdateDisplay()
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            UpdateDisplay()
            if l[i] > l[i + gap]:
                l[i], l[i + gap]=l[i + gap], l[i]
                swapped = True
    return l

    return l

def HeapSort(l):

    def heapify(l, n, i):
        UpdateDisplay(l)
        largest = i  
        left = (2 * i) + 1    
        right = (2 * i) + 2 

        if left < n and l[largest] < l[left]:
            largest = left

        if right < n and l[largest] < l[right]:
            largest = right

        if largest != i:
            l[i], l[largest] = l[largest], l[i] 
            heapify(l, n, largest)

    def buildHeap(lista, n):
        for i in range(n//2 - 1, -1, -1):
            heapify(lista, n, i)

    n = len(l)
    buildHeap(l, n)
    
    for i in range(n-1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)

def CaseMachine(value, l):
    if (value == 0):
        BubbleSort(l)
    elif (value == 1):
        MergeSort(l)
    elif (value == 2):
        InsertionSort(l)
    elif (value == 3):
        CountingSort(l)
    elif (value == 4):
        SelectionSort(l)
    elif (value == 5):
        CombSort(l)
    elif (value == 6):
        HeapSort(l)

def Sort(function, l):
    CaseMachine(functionDic[function], l)

def UpdateDisplay(lst = startList): 
    SCREEN.fill((0,0,0))      
    for i, x in enumerate(lst):
        pygame.draw.line(SCREEN, (255,255,255), (i * (WIDTH/LIST_LENGTH),HEIGHT), (i * (WIDTH/LIST_LENGTH), HEIGHT - x*(HEIGHT/LIST_LENGTH)))
    list1.draw(SCREEN) 
    sortButton.draw(SCREEN)
    shuffleButton.draw(SCREEN)
    pygame.display.update()

def RandomizeList(l):
    for x in range(0,len(l)):
        randomInteger = random.randrange(0,len(l))
        l[x], l[randomInteger] = l[randomInteger], l[x]
        UpdateDisplay()
    return l

startList = RandomizeList(startList)

while 1:
    UpdateDisplay()
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            sys.exit()  
    selected_option = list1.update(event_list)
    if selected_option >= 0:
        list1.main = list1.options[selected_option]
    
    if sortButton.update(event_list):
        Sort(list1.main, startList)
    if shuffleButton.update(event_list):
        RandomizeList(startList)
