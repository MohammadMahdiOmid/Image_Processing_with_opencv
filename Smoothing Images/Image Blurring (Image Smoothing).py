import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    image = cv2.imread("roi.jpg", cv2.IMREAD_COLOR)
    image2 = cv2.imread("blure.jpg")

    blur = cv2.blur(image, (5, 5))
    blur2 = cv2.GaussianBlur(image, (5, 5), 0)
    mdian_blure = cv2.medianBlur(image2, 19)
    Bilateral_Filtering = cv2.bilateralFilter(image2, 9, 75, 75)

    cv2.imshow("orginal", image)
    cv2.imshow("blur", blur)
    cv2.imshow("blur2", blur2)
    cv2.imshow("mdian_blure", mdian_blure)
    cv2.imshow("Bilateral_Filtering", Bilateral_Filtering)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
