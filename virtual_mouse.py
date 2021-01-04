import cv2
import pyautogui

hand_cascade = cv2.CascadeClassifier('mouse.xml')
fist_cascade = cv2.CascadeClassifier('click.xml')

camera = cv2.VideoCapture(1)
width, height = pyautogui.size()

print("Screen resolution:", width, "x", height)

while True:

    ret, frame = camera.read()


    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mouse = hand_cascade.detectMultiScale(gray, 1.2, 4, minSize=(300, 300))
        click = fist_cascade.detectMultiScale(gray, 1.2, 4, minSize=(300, 300))

        for (x, y, w, h) in mouse:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            center_x = int((x + w) - (w / 2))
            center_y = int((y + h) - (h / 2))
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
            pyautogui.moveTo(1920-center_x, center_y)

        for (x, y, w, h) in click:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
            center_x = int((x + w) - (w / 2))
            center_y = int((y + h) - (h / 2))
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            pyautogui.click(1920-center_x, center_y)

        cv2.namedWindow("Virtual Mouse", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Virtual Mouse", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Virtual Mouse", frame)


    if cv2.waitKey(1) & 0xFF == 32:
        break

camera.release()
cv2.destroyAllWindows()