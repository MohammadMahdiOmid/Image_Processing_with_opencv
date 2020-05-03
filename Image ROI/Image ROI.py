import cv2
import numpy as np


def main():
    img = cv2.imread("image.jpg")

    ball = img[280:340, 330:390]
    img[0:60, 100:160] = ball

    cv2.imshow("image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
