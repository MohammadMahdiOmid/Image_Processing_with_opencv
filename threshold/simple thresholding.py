import cv2


def main():
    image = cv2.imread("image.jpg")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, threshold1 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
    ret, threshold2 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY_INV)
    ret, threshold3 = cv2.threshold(image_gray, 127, 255, cv2.INTER_CUBIC)
    ret, threshold4 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TOZERO)
    ret, threshold5 = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TOZERO_INV)

    img = [image_gray, threshold1, threshold2, threshold3, threshold4, threshold5]

    cv2.imshow("frame0", image_gray)
    cv2.imshow("frame1", threshold1)
    cv2.imshow("frame2", threshold2)
    cv2.imshow("frame3", threshold3)
    cv2.imshow("frame4", threshold4)
    cv2.imshow("frame5", threshold5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
