import cv2
from matplotlib import pyplot as plt


def main():

    image = cv2.imread("roi.jpg")

    edges = cv2.Canny(image, 100, 200)

    # cv2.imshow("image", image)

    # cv2.imshow("edges", edges)

    plt.subplot(121), plt.imshow(image, cmap='gray')

    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(edges, cmap='gray')

    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

