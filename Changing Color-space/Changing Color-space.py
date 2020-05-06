import cv2 as cv
import numpy as np


def main():
    camera = cv.VideoCapture(0)

    while camera.isOpened():

        ret, frame = camera.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        low_yellow = np.array([20, 100, 100])

        upper_yellow = np.array([30, 255, 255])

        mask = cv.inRange(hsv, low_yellow, upper_yellow)

        res = cv.bitwise_and(frame, frame, mask=mask)

        key = cv.waitKey(1)

        cv.imshow("frame", frame)
       # cv.imshow("mask", mask)
        cv.imshow("res", res)

        if key == 32:
            cv.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
