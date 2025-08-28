import pyautogui
import pyperclip
import time

# Step 1: Click on the chrome icon at (1639, 1412)
pyautogui.click(224, 73)
time.sleep(1)  # Wait for any UI response

# Step 2: Drag from (1003, 237) to (2187, 1258) to select text
pyautogui.moveTo(1003, 237)
pyautogui.mouseDown()
pyautogui.moveTo(1446, 926, duration=1)  # drag smoothly over 1 second
pyautogui.mouseUp()

time.sleep(0.5)  # Wait a moment for selection

# Step 3: Copy the selected text (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Allow time for clipboard to update

# Step 4: Retrieve text from clipboard
text = pyperclip.paste()

print(text)
