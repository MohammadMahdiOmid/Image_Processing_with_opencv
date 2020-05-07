import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def main():
    image = cv.imread("image.jpg")
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv.getPerspectiveTransform(pts1, pts2)

    dst = cv.warpPerspective(image, M, (300, 300))

    plt.subplot(121), plt.imshow(image), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


if __name__ == '__main__':
    main()
