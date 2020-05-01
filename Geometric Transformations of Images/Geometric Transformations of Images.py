import cv2 as cv
import numpy as np


def main():
    image = cv.imread("image.jpg", 0)

    rows, cols = image.shape

    range = np.float32([[1, 0, 200], [0, 1, 50]])
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)

    res = cv.warpAffine(image, M, (cols, rows))

    cv.imshow("res", res)

    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
