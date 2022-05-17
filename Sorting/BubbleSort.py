#------------------------------------Boilerplate-------------------------------------#
#region

import pygame, sys, random, time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Sorting Visualizer")
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 30)
listLength = WIDTH
oldLen = listLength
COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)
COLOR_CHECKING = (0, 255, 0)
COLOR_BASE = (255, 255, 255)
COLOR_CURRENT = (255, 255, 255)
speedMultiplier = 5
iteration = 0
maxValue = 0
coloringIndex = 0
startList = []
algorithms = ["PythonSort", "BubbleSort", "QuickSort", "InsertionSort", "CountingSort", "SelectionSort", "CombSort", "HeapSort", "CycleSort", "RadixSort", "RadixSortLSD", "MergeSort"]

#endregion
#-------------------------------------UI classes-------------------------------------#
#region

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
                    self.text = ''
                    self.active = False
                    self.color = COLOR_INACTIVE
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
        screen.blit(self.txt_surface, self.txt_surface.get_rect(center = self.rect.center))
        if(self.active == False):
            self.txt_surface = FONT.render("- - - - - - - - -", True, (0,0,0))
            screen.blit(self.txt_surface, self.txt_surface.get_rect(center = self.rect.center))

#endregion
#----------------------------------General Functions---------------------------------#
#region

def Sigmoid(x):
    return (1/(1 + 2.71828182846**(-x/(listLength/10))))*HEIGHT

def GenerateList(len):
    startList.clear()
    global maxValue
    for i in range(1,len):
        startList.append(round(Sigmoid(i-(len/2))))#+ (math.sin((i/(len/4)))+1)*100)
        #startList.append(i)
    maxValue = max(startList)
    return startList

def printList(l):
    for i, x in enumerate(l):
        print(x)

def UpdateDisplay(lst = startList, additionalMultiplier = 1): 
    global iteration, COLOR_CURRENT, coloringIndex, _sorted
    thickness = 1
    iteration += 1
    if (iteration % (speedMultiplier * additionalMultiplier) == 0):
        SCREEN.fill((0,0,0))      
        if (WIDTH//listLength < 1):
            thickness = 1
        else:
            thickness = WIDTH//listLength
        for i, x in enumerate(lst):
            pygame.draw.line(SCREEN, COLOR_BASE, (i * (WIDTH/listLength) + WIDTH//listLength*(3/2) ,HEIGHT), (i * (WIDTH/listLength) + WIDTH//listLength*(3/2) , HEIGHT - (x*(HEIGHT/maxValue))), thickness)
    selectionDropDown.draw(SCREEN) 
    sortButton.draw(SCREEN)
    shuffleButton.draw(SCREEN)
    listSizeInputBox.draw(SCREEN)
    pygame.display.update()

def CheckListSorted():
    global COLOR_CURRENT
    sorted = True
    lastVal = 0
    for i in range(0, listLength-1):
        if (lastVal > startList[i]):
            sorted = False
        lastVal = startList[i]
    if (sorted):
        if (WIDTH//listLength < 1):
            thickness = 1
        else:
            thickness = WIDTH//listLength
        for i, x in enumerate(startList):
            pygame.draw.line(SCREEN, COLOR_CHECKING, (i * (WIDTH/listLength) + WIDTH//listLength*(3/2) ,HEIGHT), (i * (WIDTH/listLength) + WIDTH//listLength*(3/2) , HEIGHT - (x*(HEIGHT/maxValue))), thickness)
            pygame.display.update()
    return sorted

def Sort(function, l):
    if CheckListSorted():
        return
    global startList
    if (function == 'Select Algorithm'):
        return
    startList = eval(function + "(l)")
    UpdateDisplay(l)
    print(CheckListSorted())

def RandomizeList(l):
    for x in range(0,len(l)):
        randomInteger = random.randrange(0,len(l))
        l[x], l[randomInteger] = l[randomInteger], l[x]
        if (x % 5 == 0):
            UpdateDisplay(l)
    return l

#endregion
#---------------------------------Sorting Algorithms---------------------------------#
#region

def PythonSort(l):
    l.sort()
    UpdateDisplay(l, 0.1)
    return l

def BubbleSort(l):
    indexLen = len(l)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexLen):
            if (i < indexLen):
                if (l[i] > l[i + 1]):
                    l[i], l[i + 1] = l[i + 1], l[i]
                    sorted = False
        UpdateDisplay(l)
    return l

def QuickSort(l):
    if len(l) < 2:                      # if nothing to sort, return
        return
    stack = []                          # initialize stack
    stack.append([0, len(l)-1])
    while len(stack) > 0: 
        lo, hi = stack.pop()            # pop lo, hi indexes
        p = l[(lo + hi) // 2]           # pivot, any a[] except a[hi]
        i = lo - 1                      # Hoare partition
        j = hi + 1
        while(1):
            UpdateDisplay(l)
            while(1):                   #  while(a[++i] <; p)
                i += 1
                if(l[i] >= p):
                    break
            while(1):                   #  while(a[--j] <; p)
                j -= 1
                if(l[j] <= p):
                    break
            if(i >= j):                 #  if indexes met or crossed, break
                break
            l[i],l[j] = l[j],l[i]       #  else swap elements
        if(j >  lo):                     # push indexes onto stack
            stack.append([lo, j])
        j += 1
        if(hi >  j):
            stack.append([j, hi])
    return(l)

def InsertionSort(l):
    for i in range(1, len(l)):
        UpdateDisplay(l)
        while l[i-1] > l[i] and i > 0:
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
        count[l[m]-1] += 1

    # storing the cumulative count
    for m in range(1, size):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[l[m]-1] - 1] = l[m]
        count[l[m]-1] -= 1
        UpdateDisplay(output)
        m -= 1

    
    for m in range(0, size):
        l[m] = output[m]

    return l

def SelectionSort(l):
    for i in range(0,len(l)-1):
        p=0
        mini=l[-1]
        for j in range(i,len(l)):
            if l[j]<=mini:
                mini=l[j]
                p=j
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
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            if l[i] > l[i + gap]:
                UpdateDisplay(l)
                l[i], l[i + gap]=l[i + gap], l[i]
                swapped = True
    return l

    return l

def HeapSort(l):
    def heapify(l, n, i):
        UpdateDisplay(l, 4)
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
    
    return l

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

def RadixSort(l):
    def countingSortForRadix(l, placeValue):
        # We can assume that the number of digits used to represent
        # all numbers on the placeValue position is not grater than 10
        countArray = [0] * 10
        inputSize = len(l)

        # placeElement is the value of the current place value
        # of the current element, e.g. if the current element is
        # 123, and the place value is 10, the placeElement is
        # equal to 2
        for i in range(inputSize): 
            placeElement = int((l[i] // placeValue) % 10)
            countArray[placeElement] += 1

        for i in range(1, 10):
            countArray[i] += countArray[i-1]

        # Reconstructing the output array
        outputArray = [0] * inputSize
        i = inputSize - 1
        while i >= 0:
            currentEl = l[i]
            placeElement = int((l[i] // placeValue) % 10)
            countArray[placeElement] -= 1
            newPosition = countArray[placeElement]
            outputArray[newPosition] = currentEl
            UpdateDisplay(outputArray)
            i -= 1
            
        return outputArray
    # Step 1 -> Find the maximum element in the input array
    # Step 2 -> Find the number of digits in the `max` element
    D = len(str(max(l)))
    
    # Step 3 -> Initialize the place value to the least significant place
    placeVal = 1

    # Step 4
    outputArray = l
    while D > 0:
        #l = outputArray
        UpdateDisplay(outputArray)
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        D -= 1
        if (outputArray == l.sort()):
            D = 0
    l = outputArray
    return l

def RadixSortLSD(l):
    RADIX = 10
    buckets = [[] for i in range(RADIX)]

    # sort
    tmp = -1; placement = 1
    for i in range(len(str(max(l)))):

		# split input between lists
        for i in l:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)

		
		# empty lists into input array
        a = 0
        for bucket in buckets:
            for i in bucket:
                l[a] = i
                a += 1
                display = []
                display.append(i)
                UpdateDisplay(l)       
            bucket.clear()
		
		# move to next digit
        placement *= RADIX
    return l

def MergeSort(l):

    def join(l1, l2):
        i = 0
        j = 0
        outputvetor = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                outputvetor.append(l1[i])
                i = i + 1
            else:
                outputvetor.append(l2[j])
                j = j + 1
        
        if(i < len(l1)):
            for x in range (i, len(l1)):
                outputvetor.append(l1[x])

        if(j < len(l2)):
            for x in range (j, len(l2)):
                outputvetor.append(l2[x])
        return outputvetor

    block = 1
    n = len(l)
    while block < n:
        output = []
        i1 = 0
        i2 = block
        while i2 < n:
            outPutList = join(l[i1:i2], l[i2:(i2 + block)])
            output += outPutList
            i = 0
            x = i1
            while x < i2 + block and i < len(outPutList) :
                UpdateDisplay(l, 3)
                l[x] = outPutList[i]
                i = i + 1
                x = x + 1
            i1 = i2 + block
            i2 = i1 + block
        block = block * 2
    return l

#endregion
#-----------------------------------Initialization-----------------------------------#
#region

selectionDropDown = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    50, 50, 200, 50, 
    pygame.font.SysFont(None, 30), 
    "Select Algorithm", algorithms)

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

listSizeInputBox = InputBox(
    800, 
    50, 
    200, 
    50)

GenerateList(
    listLength)

#endregion
#------------------------------------Program Loop------------------------------------#
#region

while 1:

    #List length change event handler
    newLen = listLength
    if (oldLen != newLen):
        GenerateList(listLength)
        startList = RandomizeList(startList)
        maxValue = max(startList)
    oldLen = listLength

    #Input handler
    event_list = pygame.event.get()
    for event in event_list:
        listSizeInputBox.handle_event(event)
        if event.type == QUIT:
            sys.exit()  

    #Update chosen algorithm
    selected_option = selectionDropDown.update(event_list)
    if selected_option >= 0:
        selectionDropDown.main = selectionDropDown.options[selected_option]
    
    #Detect 'Sort' and 'Shuffle' button presses
    if sortButton.update(event_list):
        Sort(selectionDropDown.main, startList)
    if shuffleButton.update(event_list):
        RandomizeList(startList)

    #General update
    UpdateDisplay(startList)
    listSizeInputBox.update()

#endregion