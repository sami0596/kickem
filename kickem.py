import time
import pyautogui
usernames = []
amounts = 0;
pause = 5;

while True:
    user_input = input("How many do you want to kick?: ")
    try:
        amounts = int(user_input)
        break
    except:
        print("please, enter a number")
        continue

order = 0;
for user in range(amounts):
    order += 1;
    name = str(input(str(order) + ": "))

    usernames.append(name)
print(usernames)


while True:
    user_input = input("When should the program run (in seconds)?: ")
    try:
        pause = int(user_input)
        break
    except:
        print("please, enter a number")
        continue


input("The program will begin to execute in " + str(pause) + " seconds, from the moment you press Enter")

time.sleep(pause)
for x in usernames:
    pyautogui.typewrite('/kick ' + x)
    pyautogui.press('enter')
    pyautogui.press('enter')
