import cv2
import numpy as np


def main():
    image = cv2.imread("approx.jpg")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, threshold = cv2.threshold(image_gray, 127, 255, 0)

    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.drawContours(image, contours, -1, (0, 255, 255), 1)
    img2 = cv2.drawContours(image, contours, 3, (0, 0, 0), 1)
    cnt = contours[4]
    # cv2.drawContours(image, [cnt], 0, (0, 255, 0), 3)
    # cv2.imshow("img2", img2)
    # cv2.imshow("countours", img)
    epsilon = 0.1 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    cv2.imshow("image", image_gray)
    cv2.imshow("img", img)
    cv2.imshow("img2", img2)
    #cv2.imshow("EPSILON", epsilon)
    # cv2.imshow("approx", approx)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

