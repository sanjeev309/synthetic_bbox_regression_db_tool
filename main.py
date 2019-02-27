import numpy as np
import cv2

TOTAL_IMAGES = 1000
STORE_IMAGES = False
IMAGE_DIMENSION = 100
NUM_CHANNELS = 1
PADDING_MIN = 10
PADDING_MAX = 20
MIN_BOX_DIM = 40


def return_random_bbox_value(start, end, num_values=4):
    x, y = np.random.randint(start, end - 60, size=num_values - 2)
    gap_w, gap_h = np.random.randint(PADDING_MIN, PADDING_MAX, size=num_values - 2)
    w = MIN_BOX_DIM + gap_w
    h = MIN_BOX_DIM + gap_h
    return [x, y, w, h]


def main():
    data = np.empty([0, IMAGE_DIMENSION, IMAGE_DIMENSION, NUM_CHANNELS], dtype=np.int64)
    target = np.empty([0, 4], dtype=np.int64)

    for i in range(TOTAL_IMAGES):
        x, y, w, h = return_random_bbox_value(0, IMAGE_DIMENSION)
        image = np.zeros([IMAGE_DIMENSION, IMAGE_DIMENSION])
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)

        if STORE_IMAGES:
            cv2.imwrite("db/" + str(i) + ".jpg", image)

        cv2.imshow("data", image)
        cv2.waitKey(1)

        image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        data = np.vstack((data, [np.expand_dims(image, axis=2)]))
        target = np.vstack((target, [x, y, x + w, y + h]))

        print(str(i) + ": %f, %f , %f , %f , %f , %f" % (x, y, x + w, y + h, w, h))

    target = target / IMAGE_DIMENSION
    np.save("data", data)
    np.save("target", target)
    print("Done!")


if __name__ == "__main__":
    main()
