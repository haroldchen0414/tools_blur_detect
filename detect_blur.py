# 示例
# python detect_blur.py --images images
from imutils import paths
import argparse
import cv2

def variant_of_laplacian(image):
    # 计算图像的拉普拉斯算子, 返回焦点度量(方差)
    return cv2.Laplacian(image, cv2.CV_64F).var()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0, help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

for imagePath in paths.list_images(args["images"]):
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (600, 800))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variant_of_laplacian(gray)
    text = "Not Blurry"

    if fm < args["threshold"]:
        text = "Blurry"

    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)