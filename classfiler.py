import cv2

if __name__ == '__main__':

    img = cv2.imread("image1.jpg")

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()
