import numpy as np
import cv2

TOTAL_IMAGES = 1000
STORE_IMAGES = False
IMAGE_DIMENSION = 160
PADDING = 100


def return_random_bbox_value(start,end, num_values = 4):
    x, y = np.random.randint(start, end, size=num_values - 2)
    w, h = np.random.randint(start/2 + PADDING, end/2 + PADDING, size=num_values-2)
    return [x, y, w, h]


def main():
    data = np.empty([0, IMAGE_DIMENSION, IMAGE_DIMENSION], dtype=np.int64)
    target = np.empty([0, 4], dtype=np.int64)

    for i in range(TOTAL_IMAGES):
        x, y, w, h = return_random_bbox_value(0, IMAGE_DIMENSION - PADDING)
        image = np.zeros([IMAGE_DIMENSION,IMAGE_DIMENSION])
        cv2.rectangle(image, (x,y), (w,h), (255,255,255), -1)

        if STORE_IMAGES:
            cv2.imwrite(str(i) + ".jpg", image)

        data = np.vstack((data, [image]))
        target = np.vstack((target, [x,y,w,h]))
        print(i)

    np.save("data",data)
    np.save("target",target)
    print("Done!")


if __name__ == "__main__":
    main()
