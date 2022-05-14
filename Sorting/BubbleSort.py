import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Sorting Visualizer")
WIDTH = 2000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 30)
listLength = 500
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

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (COLOR_INACTIVE)
        self.text = text
        self.txt_surface = FONT.render(text, True, (0,0,0))
        self.active = False
        self.list = []

    def handle_event(self, event):
        global listLength
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    listLength = int(self.text)
                    print(int(self.text))
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, (0,0,0))

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    50, 50, 200, 50, 
    pygame.font.SysFont(None, 30), 
    "Select Algorithm", ["BubbleSort", "MergeSort", "InsertionSort", "CountingSort", "SelectionSort", "CombSort", "HeapSort", "CycleSort"])

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

inputBox = InputBox(800, 50, 200, 50)

functionDic = {
    "BubbleSort" : 0,
    "MergeSort" : 1,
    "InsertionSort" : 2,
    "CountingSort" : 3,
    "SelectionSort" : 4,
    "CombSort" : 5,
    "HeapSort" : 6,
    "CycleSort" : 7

}

startList = [i for i in range(listLength)]



def printList(l):
    for i, x in enumerate(l):
        print(x)

def BubbleSort(l):
    indexLen = len(l)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexLen):
            UpdateDisplay(l)
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
            UpdateDisplay(l)
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
        UpdateDisplay(l)

    # storing the cumulative count
    for m in range(1, size):
        count[m] += count[m - 1]
        UpdateDisplay(l)

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        UpdateDisplay(l)
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
                UpdateDisplay(l)
        l[i],l[p]=l[p],l[i]
        UpdateDisplay(l)
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
        UpdateDisplay(l)
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            UpdateDisplay(l)
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

def CycleSort(l):
  writes = 0
    
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(l) - 1):
    item = l[cycleStart]
      
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(l)):
      if l[i] < item:
        pos += 1
      
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
      
    # Otherwise, put the item there or right after any duplicates.
    while item == l[pos]:
      pos += 1
    l[pos], item = item, l[pos]
    UpdateDisplay(l)
    writes += 1
      
    # Rotate the rest of the cycle.
    while pos != cycleStart:
        
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(l)):
        if l[i] < item:
          pos += 1
        
      # Put the item there or right after any duplicates.
      while item == l[pos]:
        pos += 1
      l[pos], item = item, l[pos]
      UpdateDisplay(l)
      writes += 1
    
  return l

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
    elif (value == 7):
        CycleSort(l)

def Sort(function, l):
    if (function == 'Select Algorithm'):
        return
    CaseMachine(functionDic[function], l)

def UpdateDisplay(lst = startList): 
    SCREEN.fill((0,0,0))      
    for i, x in enumerate(lst):
        pygame.draw.line(SCREEN, (255,255,255), (i * (WIDTH/listLength) + WIDTH//listLength//2 ,HEIGHT), (i * (WIDTH/listLength) + WIDTH//listLength//2 , HEIGHT - x*(HEIGHT/listLength)), WIDTH//listLength)
    list1.draw(SCREEN) 
    sortButton.draw(SCREEN)
    shuffleButton.draw(SCREEN)
    inputBox.draw(SCREEN)
    pygame.display.update()

def RandomizeList(l):
    for x in range(0,len(l)):
        randomInteger = random.randrange(0,len(l))
        l[x], l[randomInteger] = l[randomInteger], l[x]
        UpdateDisplay(l)
    return l

startList = RandomizeList(startList)

def CheckListLenChange(old, new):
    if (old != new):
        return True
    return False

oldLen = listLength

while 1:
    newLen = listLength
    if (oldLen != newLen):
        startList = [i for i in range(listLength)]
        startList = RandomizeList(startList)
    oldLen = listLength
    UpdateDisplay(startList)
    event_list = pygame.event.get()
    for event in event_list:
        inputBox.handle_event(event)
        if event.type == QUIT:
            sys.exit()  
    selected_option = list1.update(event_list)
    if selected_option >= 0:
        list1.main = list1.options[selected_option]
    
    if sortButton.update(event_list):
        Sort(list1.main, startList)
    if shuffleButton.update(event_list):
        RandomizeList(startList)
    inputBox.update()
