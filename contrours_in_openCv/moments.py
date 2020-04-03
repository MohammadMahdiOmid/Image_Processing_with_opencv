import cv2 as cv
import numpy as np


def main():
    image = cv.imread("sudoku.jpg", 0)

    ret, thresh = cv.threshold(image, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, 1, 2)

    cnt = contours[0]
    M = cv.moments(cnt)

    print(M)

    area = cv.contourArea(cnt)

    print(area)

    perimeter = cv.arcLength(cnt, True)

    print(perimeter)


if __name__ == '__main__':
    main()

