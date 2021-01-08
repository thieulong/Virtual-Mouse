import cv2
import pyautogui
import keyboard
import sys

sys.path.append("/usr/local/lib/python3.8/dist-packages")

hand_cascade = cv2.CascadeClassifier('mouse.xml')
fist_cascade = cv2.CascadeClassifier('click.xml')

camera = cv2.VideoCapture(1)
width, height = pyautogui.size()

print("Screen resolution:", width, "x", height)

while True:

    ret, frame = camera.read()

    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        drive = hand_cascade.detectMultiScale(gray, 1.2, 4, minSize=(300, 300))
        reverse = fist_cascade.detectMultiScale(gray, 1.2, 4, minSize=(300, 300))

        cv2.line(frame, (int(width / 3), 0), (int(width / 3), height), (0, 255, 0), 2)
        cv2.line(frame, (int(width / 6), 0), (int(width / 6), height), (0, 255, 0), 2)

        for (x, y, w, h) in drive:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            center_x = int((x + w) - (w / 2))
            center_y = int((y + h) - (h / 2))
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
            # pyautogui.press('w')
            keyboard.write('w', delay=0)

            if center_x > width / 3:
                # pyautogui.press('a')
                keyboard.write('a',delay=0)
            elif center_x < width / 6:
                # pyautogui.press('d')
                keyboard.write('d', delay=0)

        for (x, y, w, h) in reverse:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
            center_x = int((x + w) - (w / 2))
            center_y = int((y + h) - (h / 2))
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            # pyautogui.press('s')
            keyboard.write('s',delay=0)

            if center_x > width / 3:
                # pyautogui.press('a')
                keyboard.write('a', delay=0)
            elif center_x < width / 6:
                # pyautogui.press('d')
                keyboard.write('d', delay=0)

        cv2.namedWindow("Virtual Mouse", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Virtual Mouse", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 32:
        break

camera.release()
cv2.destroyAllWindows()