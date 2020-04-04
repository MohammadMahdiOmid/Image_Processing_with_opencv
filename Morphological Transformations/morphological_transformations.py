import cv2
import numpy as np


def main():
    image = cv2.imread("j.jpg", 0)
    image2 = cv2.imread("opening.jpg", 0)
    image3 = cv2.imread("closing.jpg", 0)

    kernel = np.ones((5, 5), np.float32)

    eroising = cv2.erode(image, kernel, iterations=1)
    dilation = cv2.dilate(image, kernel, iterations=1)
    oppening = cv2.morphologyEx(image2, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(image3, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow("orginal", image)
    cv2.imshow("eroising", eroising)
    cv2.imshow("dilation", dilation)
    cv2.imshow("orginal2", image2)
    cv2.imshow("oppening", oppening)
    cv2.imshow("orginal3", image3)
    cv2.imshow("closing", closing)
    cv2.imshow("gradient", gradient)
    cv2.imshow("top_hat", top_hat)
    cv2.imshow("black_hat", black_hat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
