import cv2 as cv
import numpy as np
import serial

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=2)
cap = cv.VideoCapture(1)

while True:
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    frame = cv.resize(frame, (320, 240))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    red_lower = np.array([105, 100, 125], np.uint8)
    red_upper = np.array([130, 255, 230], np.uint8)
    mask = cv.inRange(hsv, red_lower, red_upper)
    contours ,_ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)
    rows, cols, _ = frame.shape
    center_x = int(rows / 2)
    center_y = int(cols / 2)

    for cnt in contours:
        (x, y, w, h) = cv.boundingRect(cnt)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # text = "x = "+str(x)+"y = "+str(y)
        # cv.putText(frame, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255))

        medium_x = int((x + x + w) / 2)
        medium_y = int((y + y + h) / 2)
        obj_x = round(medium_x / 10)
        obj_y = round(medium_y / 10)
        cv.line(frame, (medium_x, 0), (medium_x, 480), (0, 255, 0), 2)
        text2 = "mediumX = " + str(obj_x)
        cv.putText(frame, text2, (0, 100), cv.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255))

        cv.line(frame, (0, medium_y), (640, medium_y), (0, 255, 0), 2)
        text3 = "mediumY = " + str(obj_y)
        cv.putText(frame, text3, (0, 50), cv.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255))

        string = 'X{0:d}Y{1:d}'.format((obj_x), (obj_y))
        print(string)
        arduino.write(string.encode('utf-8'))
        break

    cv.imshow("Output", frame)
    key = cv.waitKey(1)
    cv.waitKey(1)
    cv.waitKey(1)
    cv.waitKey(1)
    cv.waitKey(1)
    if key == ord("q"):
        break

cv.destroyAllWindows()
cv.waitKey(1)
cv.waitKey(1)
