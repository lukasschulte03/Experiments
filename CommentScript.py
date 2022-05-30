'''''
screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    >>> currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    >>> pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    >>> pyautogui.click() # Click the mouse at its current location.
    >>> pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    >>> pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    >>> pyautogui.doubleClick() # Double click the mouse at the
    >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    >>> pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    >>> pyautogui.press('esc') # Simulate pressing the Escape key.
    >>> pyautogui.keyDown('shift')
    >>> pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
    >>> pyautogui.keyUp('shift')
    >>> pyautogui.hotkey('ctrl', 'c')
'''''


import pyautogui, time, pygame, keyboard, random
pygame.init()

listOfComments = [
"Top Tier!", 
"Banger", 
"Nothing Happened...", 
#"Can't wait for wano arc", 
"best anime out there!", 
"Finna finish this in 4 weeks!", 
"Awesome!", "Actual good anime", 
"Why though...?", 
"Bruh", 
"Bruh", 
"This is guuuud!", 
"Absolute menace!", 
"One Piece>Seven Deadly Sins",
"One Piece>Naruto",
"One Piece>DBZ",
"One Piece>Bleack",
"One Piece is the best of the big 3",
"Best shonen out there!",
"Damn...",
"How many episodes will there be?",
"Is One Piece still airing?"
]

running = True

def checkQuit():
    global running
    if keyboard.is_pressed('+'):
            print('Shutdown')
            running = False
            return running

# comment box: Point(x=1215, y=627)
# send comment: Point(x=2160, y=697)
# prev button: Point(x=1810, y=951)

while running:


    pyautogui.press('pagedown')

    checkQuit()
    if running == False:
        break

    time.sleep(1)
    pyautogui.click(1215, 627)

    checkQuit()
    if running == False:
        break

    time.sleep(1)
    pyautogui.write(listOfComments[random.randrange(0, len(listOfComments))])

    checkQuit()
    if running == False:
        break

    time.sleep(1)

    checkQuit()
    if running == False:
        break

    pyautogui.click(2160, 697)

    checkQuit()
    if running == False:
        break

    time.sleep(1)
    pyautogui.press('pageup')
    pyautogui.press('pageup')

    checkQuit()
    if running == False:
        break  

    time.sleep(1)

    pyautogui.click(1810, 951)

    checkQuit()
    if running == False:
        break

    time.sleep(30)


    print(pyautogui.position())



    


