import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    image = cv2.imread("roi.jpg", cv2.IMREAD_COLOR)

    kernel = np.ones((5, 5), np.float32) / 25

    dst = cv2.filter2D(image, -1, kernel)

    cv2.imshow("orginal", image)
    cv2.imshow("dst", dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
