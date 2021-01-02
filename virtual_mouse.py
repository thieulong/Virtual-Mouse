import cv2
import pyautogui

hand_cascade = cv2.CascadeClassifier('mouse.xml')
fist_cascade = cv2.CascadeClassifier('click.xml')

camera = cv2.VideoCapture(3)

while True:

    ret, frame = camera.read()
    cv2.flip(frame, 0)

    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mouse = hand_cascade.detectMultiScale(gray, 1.15, 12)
        click = fist_cascade.detectMultiScale(gray, 1.15, 12)

        for (x, y, w, h) in mouse:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            center_x = 1920-int(x+(w/2))
            center_y = int(y+(h/2))
            print(center_x, center_y)
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
            pyautogui.moveTo(center_x, center_y)

        for (x, y, w, h) in click:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
            center_x = 1920-int(x+(w/2))
            center_y = int(y+(h/2))
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            pyautogui.click(center_x, center_y)

        cv2.imshow("Virtual mouse", frame)

    if cv2.waitKey(1) & 0xFF == 32:
        break

camera.release()
cv2.destroyAllWindows()