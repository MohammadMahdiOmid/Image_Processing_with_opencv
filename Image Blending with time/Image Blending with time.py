import cv2
import numpy as np


def main():
    e1 = cv2.getTickCount()

    first_image = cv2.imread("image/writong code.jpg")
    secend_image = cv2.imread("image/call of duty.jpg")

    dst = cv2.addWeighted(first_image, 0.21, secend_image, 0.3, 0)

    cv2.imshow("image blending", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    e2 = cv2.getTickCount()

    time = (e2 - e1) / cv2.getTickFrequency()
    time = float(time)
    print(time)


if __name__ == '__main__':
    main()
